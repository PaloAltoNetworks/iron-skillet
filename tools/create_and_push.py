import os
import sys
import oyaml
import requests
from xml.etree import ElementTree
from jinja2 import Template
from jinja2.exceptions import TemplateAssertionError
from passlib.hash import md5_crypt

def create_context(config_var_file):
    # read the metafile to get variables and values
    try:
        with open(config_var_file, 'r') as var_metadata:
            variables = oyaml.safe_load(var_metadata.read())

    except IOError as ioe:
        print(f'Could not open metadata file {config_var_file}')
        print(ioe)
        sys.exit()

    # grab the metadata values and convert to key-based dictionary
    jinja_context = dict()

    for snippet_var in variables['variables']:
        jinja_context[snippet_var['name']] = snippet_var['value']

    return jinja_context


class Panos:
    def __init__(self, addr, user, pw):
        self.url = "https://{}/api".format(addr)
        self.user = user
        self.pw = pw
        self.key = ''
        self.connect()

    def connect(self):
        url = self.url
        params = {
            "type": "keygen",
            "user": self.user,
            "password": self.pw,
        }
        r = requests.get(url, params=params, verify=False)
        root = ElementTree.fromstring(r.content)
        elem = root.findall("./result/key")
        self.key = elem[0].text
        return self.key

    def send(self, params):
        url = self.url
        params["key"] = self.key
        r = requests.get(url, params=params, verify=False)
        print(r.text)

def set_at_path(panos, xpath, elementvalue):
    params = {
        "type": "config",
        "action": "set",
        "xpath": xpath,
        "element": elementvalue,
    }
    panos.send(params)

def generate_snippet(config_type, snippet_names=None):
    """
    Generates the full configuration template for a given configuration type (panos or panorama).
    This will use the load order
    :param config_type: currently supported: 'panos' or 'panorama'
    :return: will print full configs to STDOUT and also overwrite the full/iron_skillet_<type>_full.xml
    """
    metadata_file = os.path.abspath(os.path.join('..', 'templates', config_type, 'snippets'.format(config_type), '.meta-cnc.yaml'))

    try:
        with open(metadata_file, 'r') as snippet_metadata:
            service_config = oyaml.safe_load(snippet_metadata.read())

    except IOError as ioe:
        print(f'Could not open metadata file {metadata_file}')
        print(ioe)
        sys.exit()

    config_path = os.path.abspath(os.path.join('..', 'templates', config_type))

    xml_snippets = []
    if snippet_names:
        for xml_snippet in service_config['snippets']:
            if xml_snippet['name'] in snippet_names:
                xml_snippets.append(xml_snippet)
    else:
        xml_snippets = service_config['snippets']

    result = []
    # iterator through the metadata snippets load order
    # parse the snippets into XML objects
    # attach to the full_config dom
    for xml_snippet in xml_snippets:
        # xml_snippet is a set of attributes in the .meta-cnc.yaml file
        # that includes the xpaths and files listed in the proper load order
        snippet_name = xml_snippet['file']
        snippet_path = os.path.join(config_path, 'snippets'.format(config_type), snippet_name)

        # skip snippets that aren't actually there for some reason
        if not os.path.exists(snippet_path):
            print(snippet_path)
            print('this snippet does not actually exist!')
            sys.exit()

        # read them in
        with open(snippet_path, 'r') as snippet_obj:
            snippet_string = snippet_obj.read()

        if type(snippet_string) is str:
            config_variables = 'config_variables.yaml'

            # create dict of values for the jinja template render
            context = create_context(config_variables)
            t = Template(xml_snippet["xpath"])
            xpath = t.render(context)

            try:
                t2 = Template(snippet_string)
                r = t2.render(context)
                result.append({"name": xml_snippet["name"], "element": r, "xpath": xpath})
            except TemplateAssertionError:
                print("{} not currently supported.".format(xml_snippet["name"]))

    return result

# define functions for custom jinja filters
def md5_hash(txt):
    '''
    Returns the MD5 Hashed secret for use as a password hash in the PanOS configuration
    :param txt: text to be hashed
    :return: password hash of the string with salt and configuration information. Suitable to place in the phash field
    in the configurations
    '''
    return md5_crypt.hash(txt)

if len(sys.argv) == 1:
    print("printing available iron-skillet snippets")
    r = generate_snippet("panorama")
    for result in r:
        print("{} : {}".format(result["name"],result["xpath"]))
    exit()
else:
    fw = Panos("localhost:9443", "admin", "admin")
    result = generate_snippet("panorama", sys.argv[1:])
    for r in result:
        print("Doing {} at {}...".format(r["name"],r["xpath"]))
        set_at_path(fw, r["xpath"], r["element"])