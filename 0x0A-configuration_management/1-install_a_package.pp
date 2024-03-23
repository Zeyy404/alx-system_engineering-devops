# flask from pip3

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  unless   => '/usr/bin/pip3 show flask | grep -q "^Version: 2.1.0$"',
}
