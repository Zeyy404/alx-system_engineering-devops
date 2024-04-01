# Configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02)

class { 'nginx':
  manage_repo     => true,
  package_ensure  => 'latest',
  default_vhost	  =>false,
  service_restart => true,
}

firewall { 'Allow Nginx HTTP':
  port   => 80,
  proto  => 'tcp',
  action => 'accept',
}

$file_content_index = "Hello World!\n"
$file_content_404 = "Ceci n'est pas une page\n"

nginx::resource::vhost { 'default':
  www_root       => '/var/www/html',
  listen_options => 'default_server',
  access_log     => true,
  error_log      => true,
}

nginx::resource::location { '/redirect_me':
  ensure      => present,
  vhost       => 'default',
  location    => '/redirect_me',
  return      => '301 https://youtube.com/watch?v=mLW35YMzELE',
}

nginx::resource::location { '/404.html':
  ensure      => present,
  vhost       => 'default',
  location    => '= /404.html',
  internal    => true,
  content     => '/var/www/html/404.html',
}

nginx::config { 'x-served-by-header':
  content => 'add_header X-Served-By "$HOSTNAME";',
  order   => '99',
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => $file_content_index,
}

file { '/var/www/html/404.html':
  ensure  => file,
  content => $file_content_404,
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => [
    Package['nginx'],
    Nginx::Resource::Vhost['default'],
    Nginx::Resource::Location['/redirect_me'],
    Nginx::Resource::Location['/404.html'],
    Nginx::Config['x-served-by-header'],
    File['/var/www/html/index.html'],
    File['/var/www/html/404.html'],
  ],
}