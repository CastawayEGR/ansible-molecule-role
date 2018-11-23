Ansible Molecule Role
=========
[![Build Status](https://travis-ci.org/CastawayEGR/ansible-molecule-role.svg?branch=master)](https://travis-ci.org/CastawayEGR/ansible-molecule-role)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

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
      remote_user: root
      roles:
         - ansible-molecule-role

License
-------

MIT/BSD

Author Information
------------------

This role was created by [Michael Tipton](https://ibeta.org).
