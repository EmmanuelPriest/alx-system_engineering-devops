# @summary Creating a file in /tmp
#
# Creating a file in /tmp

file { '/tmp/school':
  owner => 'www-data',
  group => 'www-data',
  mode => '0744',
  path => '/tmp/school',
  content => 'I love Puppet',
}
