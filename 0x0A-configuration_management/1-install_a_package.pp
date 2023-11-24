#install flask 2.1.0 using pip3
package {'python3-pip':
  ensure => installed,
}

package {'Werkzeug':
  ensure => '2.2.2',
  provider => 'pip3',
  require => Package['python3-pip'],
}
