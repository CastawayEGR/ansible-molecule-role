Ansible Molecule Role
=========
[![Build Status](https://travis-ci.org/CastawayEGR/ansible-molecule-role.svg?branch=master)](https://travis-ci.org/CastawayEGR/ansible-molecule-role)
[![License: MIT](https://img.shields.io/github/license/mashape/apistatus.svg)](https://opensource.org/licenses/MIT)

Ansible role to deploy Ansible Molecule on a Debian/RHEL based hosts for quick role testing.

Requirements
------------

Host that molecule will be deployed on is running a Debian/RHEL based OS.


Dependencies
------------

N/A

Example Playbook
----------------

    - hosts: molecule
      remote_user: castawayegr
      roles:
         - ansible-molecule-role

License
-------

MIT/BSD

Author Information
------------------

This role was created by [Michael Tipton](https://ibeta.org).
