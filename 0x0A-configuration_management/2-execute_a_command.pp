# create a manifest that kills a process named killmenow.

exec { 'kill a process':
    command => 'killall killmenow',
    path    => ['/usr/bin', '/usr/sbin'],
}
