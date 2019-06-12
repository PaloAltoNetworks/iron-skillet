import os
import sys
import oyaml
import requests
from xml.etree import ElementTree
from jinja2 import Template
from jinja2.exceptions import TemplateAssertionError
from create_loadable_configs import create_context
from colorama import init as colorama_init
from colorama import Fore, Back, Style
import getpass

"""
Create-and-push
Generates PANOS configuration from the XML snippets and adds to the PANOS device.

This way you can pick and choose the aspects of iron-skillet you want without removing your entire configuration.

Usage:
    python create_and_push.py
    With no arguments, lists all available snippets and their destination xpaths
    
    python create_and_push.py snippetname1 snippetname2 
    Push the listed snippetnames
"""

class Panos:
    """
    PANOS Device. Could be a firewall or PANORAMA.
    """
    def __init__(self, addr, user, pw):
        """
        Initialize a new panos object
        :param addr: NAME:PORT combination (ex. l72.16.0.1:443)
        :param user: username
        :param pw: password
        """
        self.url = "https://{}/api".format(addr)
        self.user = user
        self.pw = pw
        self.key = ''
        self.connect()

    def connect(self):
        """
        Connect to a PANOS device and retrieve an API key.
        :return: API Key
        """
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
        """
        Send a request to this PANOS device
        :param params: dict: GET parameters for query ({ "type": "op" })
        :return: GET Response type
        """
        url = self.url
        params["key"] = self.key
        r = requests.get(url, params=params, verify=False)
        return r

    def get_type(self):
        """
        Get the type of PANOS device using show system info
        :param panos: PANOS device object
        :return:
        """
        params = {
            "type": "op",
            "cmd": "<show><system><info></info></system></show>"
        }
        r = self.send(params)
        root = ElementTree.fromstring(r.content)
        elem = root.findall("./result/system/model")
        return elem[0].text

def set_at_path(panos, xpath, elementvalue):
    """
    Runs a "set" action against a given xpath.
    :param panos: .panos object
    :param xpath: xpath to set at
    :param elementvalue: Element value to set
    :return: GET Response page
    """
    params = {
        "type": "config",
        "action": "set",
        "xpath": xpath,
        "element": elementvalue,
    }
    r = panos.send(params)
    return r


def get_type(panos):
    """
    Get the type of PANOS device using show system info
    :param panos: PANOS device object
    :return:
    """
    params = {
        "type": "op",
        "cmd": "<show><system><info></info></system></show>"
    }
    r = panos.send(params)
    root = ElementTree.fromstring(r.content)
    elem = root.findall("./result/system/model")
    return elem[0].text


def generate_snippet(config_type, snippet_names=None):
    """
    Generate just a snippet for the given snippet_names, or all if asked.

    :param config_type: currently supported: 'panos' or 'panorama'
    :return: dict: {"name": snippet name, "element": string element value, "xpath": path to element (from metadata file)}
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
                # This is due to a missing filder (md5_hash) because of the altern method of templating
                # This should be fixed
                print("{} not currently supported.".format(xml_snippet["name"]))

    return result

def env_or_prompt(prompt, prompt_long=None, secret=False):
    k = "IS_{}".format(prompt).upper()
    e = os.getenv(k)
    if e:
        return e

    if secret:
        e = getpass.getpass(prompt + ": ")
        return e

    if prompt_long:
        e = input(prompt_long)
        return e

    e = input(prompt + ": ")
    return e

def check_resp(r):
    root = ElementTree.fromstring(r.content)
    status = root.attrib["status"]
    if status == "success":
        print("{}Success!".format(Fore.GREEN))
    else:
        print("{}Failed.".format(Fore.RED))

    print(Style.RESET_ALL)

def main():
    requests.packages.urllib3.disable_warnings()
    colorama_init()
    if len(sys.argv) == 1:
        print("printing available iron-skillet snippets")
        r = generate_snippet("panorama")
        for result in r:
            print("{} : {}".format(result["name"], result["xpath"]))
        exit()
    else:
        addr = env_or_prompt("address", prompt_long="address:port (localhost:9443) of PANOS Device to configure: ")
        user = env_or_prompt("username")
        pw = env_or_prompt("password", secret=True)
        fw = Panos(addr, user, pw)
        t = fw.get_type()
        # This is unneeded i think.
        if t != "Panorama":
            t = "panos"
        result = generate_snippet(t.lower(), sys.argv[1:])
        for r in result:
            print("Doing {} at {}...".format(r["name"], r["xpath"]))
            r = set_at_path(fw, r["xpath"], r["element"])
            check_resp(r)


if __name__ == '__main__':
    main()