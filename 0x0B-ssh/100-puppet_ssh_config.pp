# using Puppet to make changes to our configuration file.
# so that you can connect to a server without typing a password.

include stdlib

file_line { 'SSH Private Key':
  ensure  => present,
  path	  => 'etc/ssh/ssh_config',
  line	  => '	  IdentityFile ~/.ssh/school',
  replace => true,
}

file_line { 'Deny Password Auth':
  ensure  => present,
  path	  => 'etc/ssh/ssh_config',
  line	  => '	  PasswordAuthentication no',
  replace => true,
}