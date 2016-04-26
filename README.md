bvansomeren.cockpit
=========

Installs `cockpit` a system made to easily control Linux systems: http://cockpit-project.org

Requirements
------------

No hard requirements, but you might want to put a reverse proxy in front of this, especially if you disable TLS

Role Variables
--------------

These are the limited variables and their default values as found in defaults/main.yml

	cockpit_disable_tls: no

Disables TLS. At the time of Role creation the GNUTLS version had issues with Safari and Chrome. Please think carefully about sending your root passwords in plain text!

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: bvansomeren.cockpit }

License
-------

BSD

Author Information
------------------

