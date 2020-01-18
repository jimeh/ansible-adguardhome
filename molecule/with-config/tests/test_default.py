import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_adguardhome_config_dir(host):
    d = host.file('/opt/adguardhome/config')

    assert d.exists
    assert d.is_directory
    assert d.mode == 0o755
    assert d.user == 'root'
    assert d.group == 'root'


def test_adguardhome_config_file(host):
    f = host.file('/opt/adguardhome/config/AdGuardHome.yml')

    assert f.exists
    assert f.is_file
    assert f.mode == 0o644
    assert f.user == 'root'
    assert f.group == 'root'


def test_adguardhome_data_dir(host):
    d = host.file('/opt/adguardhome')

    assert d.exists
    assert d.is_directory
    assert d.mode == 0o755
    assert d.user == 'root'
    assert d.group == 'root'


def test_adguardhome_binary(host):
    f = host.file("/opt/adguardhome/bin/AdGuardHome")

    assert f.exists
    assert f.is_file
    assert f.mode == 0o755
    assert f.user == 'root'
    assert f.group == 'root'


def test_adguardhome_service(host):
    s = host.service('adguardhome.service')

    assert s.is_enabled
    assert s.is_running


def test_adguardhome_http_service(host):
    socket = host.socket('tcp://127.0.0.1:80')

    assert socket.is_listening


def test_adguardhome_dns_service(host):
    socket = host.socket('tcp://127.0.0.1:53')

    assert socket.is_listening
