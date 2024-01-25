# Change Max open file limit (soft/hard) to 4096

file { '/etc/default/nginx':
  ensure  => file,
  content => 'ULIMIT="-N 4096"',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure     => 'running',
  enable     => true,
  hasstatus  => true,
  hasrestart => true,
}
