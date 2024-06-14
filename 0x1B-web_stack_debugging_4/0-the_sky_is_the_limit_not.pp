# Fix high amount of request failing issue

class nginx_ulimit_fix {
  exec { 'replace_ulimit':
    command => 'sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
    path    => '/usr/bin:/bin:/usr/sbin:/sbin',
    onlyif  => 'grep -q "ULIMIT=\"-n 15\"" /etc/default/nginx',
    notify  => Exec['restart_nginx'],
  }

  exec { 'restart_nginx':
    command     => 'service nginx restart',
    path        => '/usr/bin:/bin:/usr/sbin:/sbin',
    refreshonly => true,
  }
}

include nginx_ulimit_fix