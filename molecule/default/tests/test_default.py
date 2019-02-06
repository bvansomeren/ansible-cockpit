import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_package_is_installed(host):
    p = host.package('cockpit')

    assert p.is_installed


def test_service_enabled(host):
    s = host.service('cockpit.socket')

    assert s.is_running
    assert s.is_enabled


def test_listening(host):
    s = host.socket('tcp://0.0.0.0:9090')

    assert s.is_listening
