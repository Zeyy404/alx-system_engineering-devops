# Configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02)

exec { 'update':
  command  => 'sudo apt-get update',
  provider => shell,
}

-> package {'nginx':
   ensure => present,
}
-> file_line { 'header line':
   ensure => present,
   path   => '/etc/nginx/sites-available/default',
   line   => "	location / {
   add_header X-Served-By ${hostname};",
   match  => '^\tlocation / {',
}
-> exec { 'restart service':
   command  => 'sudo service nginx restart',
   provider => shell,
}