Ansible Molecule Role
=========

Ansible role to deploy Ansible Molecule on a CentOS 7 host for quick role testing.

Requirements
------------

Host that molecule will be deployed on is running CentOS 7.


Dependencies
------------

N/A

Example Playbook
----------------

    - hosts: molecule
      roles:
         - ansible-molecule-role

License
-------

MIT/BSD

Author Information
------------------

This role was created by [Michael Tipton](https://ibeta.org).
