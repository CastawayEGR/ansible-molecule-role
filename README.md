Ansible Molecule Role
=========
[![Build Status](https://travis-ci.org/CastawayEGR/ansible-molecule-role.svg?branch=master)](https://travis-ci.org/CastawayEGR/ansible-molecule-role)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![GitHub repo size in bytes](https://img.shields.io/github/repo-size/CastawayEGR/ansible-molecule-role.svg?logoColor=brightgreen)](https://github.com/CastawayEGR/ansible-molecule-role)
[![GitHub last commit](https://img.shields.io/github/last-commit/CastawayEGR/ansible-molecule-role.svg?logoColor=brightgreen)](https://github.com/CastawayEGR/ansible-molecule-role)


Ansible role to deploy Ansible Molecule on a Debian/Fedora/RHEL based hosts for quick role testing.

Requirements
------------

Host that molecule will be deployed on is running a Debian/Fedora/RHEL based OS.


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
