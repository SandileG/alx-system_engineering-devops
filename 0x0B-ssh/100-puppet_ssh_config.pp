#!/usr/bin/env bash
# Make config changes using Puppet

file { 'etc/ssh/ssh_config':
	ensure => present,

content =>"

	#SSH client configuration
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	",

}
