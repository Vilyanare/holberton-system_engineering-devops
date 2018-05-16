# Replaces the broken phpp string with php in /var/www/html/wp-settings.php
file { '/var/www/html/wp-settings.php':
  ensure => present,
}->
exec { 'sed command to replace phpp with php':
  command => "sed -i -e 's/phpp/php/g' /var/www/html/wp-settings.php",
  path => '/bin',
}
