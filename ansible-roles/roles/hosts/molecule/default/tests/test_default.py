import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    print "stage 0"
    assert f.exists
    print "stage 1"
    assert f.user == 'root'
    print "stage 2"
    assert f.group == 'root'
    print "stage 3"
