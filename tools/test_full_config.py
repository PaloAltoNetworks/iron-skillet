# Copyright (c) 2018, Palo Alto Networks
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

# Author: Scott Shoaf <sshoaf@paloaltonetworks.com>

'''
Palo Alto Networks test_set_commands.py

configures the firewall using set commands
simple expect script model
has a start_row parameter to skip various sections in the conf file

This software is provided without support, warranty, or guarantee.
Use at your own risk.
'''

import argparse
import sys
import time
import pan.xapi

def get_job_id(s):
    '''
    extract job-id from pan-python string xml response
    regex parse due to pan-python output join breaking xml rules
    :param s is the input string
    :return: simple string with job id
    '''

    return s.split('<job>')[1].split('</job>')[0]

def get_job_status(s):
    '''
    extract status and progress % from pan-python string xml response
    regex parse due to pan-python output join breaking xml rules
    :param s is the input string
    :return: status text and progress %
    '''

    status = s.split('<status>')[1].split('</status>')[0]
    progress = s.split('<progress>')[1].split('</progress>')[0]
    result = s.split('<result>')[1].split('</result>')[0]
    details = ''
    if '<details>' in s:
        details = s.split('<details>')[1].split('</details>')[0]
    return status, progress, result, details

def check_job_status(fw, results):
    '''
    periodically check job status in the firewall
    :param fw is fw object being queried
    :param results is the xml-string results returned for job status
    '''

    # initialize to null status
    status = ''

    job_id = get_job_id(results)
    #print('checking status of job id {0}...'.format(job_id))

    # check job id status and progress
    while status != 'FIN':

        fw.op(cmd='<show><jobs><id>{0}</id></jobs></show>'.format(job_id))
        status, progress, result, details = get_job_status(fw.xml_result())
        if status != 'FIN':
            print('job {0} in progress [ {1}% complete ]'.format(job_id, progress), end='\r', flush=True)
            time.sleep(5)

    print('\njob {0} is complete as {1}'.format(job_id, result))
    print(details)

    if result == 'FAIL':
        print(details)


def commit(device):
    '''
    commit to device after config is complete
    :param device: device object being configured
    :return:
    '''

    # commit changes to the device to look for errors
    cmd = '<commit></commit>'
    print('commit config')
    device.commit(cmd=cmd)
    results = device.xml_result()

    if '<job>' in results:
        check_job_status(device, results)

#def import_conf(device, filename, file_dir):

    #import_file = '{0}/{1}'.format(file_dir, filename)


def load_conf(device, filename):
    '''
    load file in device as candidate config
    :param device: configuration device object (fw or panorama)
    :param filename: name of configuration file imported to the device
    :return:
    '''

    print('loading {0} as candidate config'.format(filename))
    device.op(cmd='<load><config><from>{0}</from></config></load>'.format(filename))
    results = device.xml_result()
    print(results)

if __name__ == '__main__':

    print('=' * 80)
    print(' ')
    print('Welcome to Iron-Skillet full xml config test'.center(80))
    print(' ')
    print('=' * 80)

    parser = argparse.ArgumentParser()
    parser.add_argument("-ip", "--ip_address", help="IP address of the device", type=str)
    parser.add_argument("-u", "--username", help="Firewall Username", type=str)
    parser.add_argument("-p", "--password", help="Firewall Password", type=str)
    parser.add_argument("-t", "--type", help="panorama or panos", type=str)
    args = parser.parse_args()

    if len(sys.argv) < 2:
        parser.print_help()
        parser.exit()
        exit(1)

    ip_addr = args.ip_address
    username = args.username
    password = args.password
    dev_type = args.type

    filename = 'iron_skillet_{0}_full.xml'.format(dev_type)
    file_dir = '../loadable_configs/sample-mgmt-dhcp/{0}/'.format(dev_type)

    # create panorama object using pan-python class
    device = pan.xapi.PanXapi(api_username=username, api_password=password, hostname=ip_addr)
    # get panorama api key
    api_key = device.keygen()

    # import config
    #import_conf(device, filename, file_dir)

    # load config
    load_conf(device, filename)

    # commit config
    commit(device)