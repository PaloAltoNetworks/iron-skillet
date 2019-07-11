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
import pexpect
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

def test_set(ip_addr, user, mypassword, dev_type):
    '''
    expect style scripts to login and send set commands
    :param ip_addr: device ip address
    :param user: login username
    :param mypassword: login password
    '''

    # create fw object for pexpect scripting
    fw = pexpect.spawn('ssh {0}@{1}'.format(user, ip_addr), encoding='utf-8')
    fw.logfile = sys.stdout
    # see password and log in
    fw.expect('Password:')
    fw.sendline(mypassword)
    fw.expect('>')
    # turn off paging in the event of multi-line response
    fw.sendline('set cli pager off')
    fw.expect('>')
    fw.expect('\n')
    fw.expect('>')
    # go into configure mode
    fw.sendline('configure')
    fw.expect('#')

    # read in conf file and do line by line configuration looking for errors
    # start_row bypasses interface and admin configuration items to avoid errors
    read_file = '../loadable_configs/sample-mgmt-dhcp/{0}/iron_skillet_{0}_full.conf'.format(dev_type)
    start_row = 'set mgt-config password-complexity enabled yes\n'

    start = False

    with open(read_file) as fin:
        for line in fin:
            # use of start_row to start with a conf file line and skip others
            if line == start_row:
                start = True
                print('start set command sequence')

            # ignore conf file comments and start config at start_row line
            if not line.startswith('#') and start is True:
                fw.sendline(line)
                # not sure why pexpect needs this combo but works to get response
                fw.expect('#')
                fw.expect('\n')
                fw.expect('#')
                # pexpect before grabs last response from the device
                fw_response = fw.before

                # if starts with [edit] then no errors returned
                # otherwise stop the config showing CLI error message
                if not fw_response.strip().startswith('[edit]'):
                    print('error found in configuration')
                    print(line)
                    print(fw_response)
                    break

if __name__ == '__main__':

    print('=' * 80)
    print(' ')
    print('Welcome to Iron-Skillet set command test'.center(80))
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

    # this is the real work with device login and configuration
    test_set(ip_addr, username, password, dev_type)

    print('\n')
    print('=' * 80)
    print('set commands loaded')

    # create panorama object using pan-python class
    device = pan.xapi.PanXapi(api_username=username, api_password=password, hostname=ip_addr)
    # get panorama api key and commit
    api_key = device.keygen()
    #commit(device)