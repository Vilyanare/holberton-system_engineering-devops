exec { 'pkill "killmenow"' :
  path     => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  cmd      => 'pkill killmenow',
  provider => 'shell',
}
