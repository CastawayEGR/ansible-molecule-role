import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('pkg', ['docker-ce'])
def test_package(host, pkg):
    package = host.package(pkg)
    assert package.is_installed


@pytest.mark.parametrize('svc', ['docker-ce'])
def test_service(host, svc):
    service = host.service(svc)
    assert service.is_enabled
