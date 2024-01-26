# /etc/security/limits.conf
# Your Puppet manifest file (e.g., remove_limits.pp)

exec { 'remove_existing_holberton_limits':
  command => '/bin/sed -i "/^holberton\\s*\\(soft\\|hard\\)\\s*nofile\\s*[0-9]*$/d" /etc/security/limits.conf',
  onlyif  => '/bin/grep -q "^holberton\\s*\\(soft\\|hard\\)\\s*nofile\\s*[0-9]*$" /etc/security/limits.conf',
}

# Your Puppet manifest file (e.g., add_limits.pp)

exec { 'add_holberton_limits':
  command => '/bin/echo -e "\nholberton soft nofile 4096\nholberton hard nofile 4096" >> /etc/security/limits.conf',
  unless  => '/bin/grep -q "^holberton\\s*\\(soft\\|hard\\)\\s*nofile\\s*4096" /etc/security/limits.conf',
}

exec { 'reboot_after_modification':
  command     => '/usr/bin/sudo /sbin/reboot -f',
  refreshonly => true,
  subscribe   => Exec['add_holberton_limits'],
}
