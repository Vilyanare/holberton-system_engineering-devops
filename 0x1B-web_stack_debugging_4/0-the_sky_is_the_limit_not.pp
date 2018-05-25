# Increases the ulimit in the file /etc/default/nginx to 1000 from 15
file { '/etc/default/nginx':
  ensure    => present,
}->
exec { 'Sed command to replace 15 with 1000':
  command   => 'sed -i "s/15/1000/" /etc/default/nginx',
  path      => '/bin',
}
