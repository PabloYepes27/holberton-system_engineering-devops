# install the package
exec { 'update':
  command => '/usr/bin/apt-get update',
}
package { 'nginx':
  ensure => 'installed',
  name   => 'nginx',
}
file_line { 'add_custom_header':
  path  => '/etc/nginx/sites-available/default',
  line  => "\tadd_header X-Served-By ${hostname};",
  after => 'server_name _;'
}
exec { 'restart':
  command => '/usr/sbin/service nginx restart',
}
