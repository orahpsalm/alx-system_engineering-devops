# Using Puppet, create a manifest that kills a process named killmenow.
exec { 'stop killmenow':
  command => 'pkill -f killmenow',
  path    => '/usr/bin',
}
