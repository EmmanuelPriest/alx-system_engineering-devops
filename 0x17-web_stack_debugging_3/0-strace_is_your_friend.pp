# Puppet manuscript that uses strace to find out why Apache is returning a 500 error

$file = '/var/www/html/wp-settings.php'

# Put "phpp" in place of "php" in any line it apears

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file}",
  path    => ['/bin','/usr/bin']
}
