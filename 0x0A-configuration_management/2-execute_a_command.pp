# Using Puppet, create a manifest that kills a process named killmenow.

exec { 'conditions':
command => '/usr/bin/pkill killmenow',
}
