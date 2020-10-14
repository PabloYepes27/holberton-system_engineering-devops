# task in debugging

exec { 'change ulimit':
    path    => '/bin',
    command => "sed -i 's/15/2000/g' /etc/default/nginx"
}

exec { 'nging restart':
    path    => '/etc/init.d',
    command => 'nginx restart'
}