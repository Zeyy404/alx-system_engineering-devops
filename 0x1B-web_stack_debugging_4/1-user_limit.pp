# This class increases the file descriptor limits holberton user
# by modifying the /etc/security/limits.conf file. The limits are
# set to 2,500 for the hard limit and 25,000 for the soft limit.

exec { 'Fix Limit':
  command  => 'echo -e "holberton hard nofile 2500\nholberton soft nofile 25000" > /etc/security/limits.conf',
  provider => shell,
}