# Define a class for clarity
class { 'flask':
  # Ensure flask is installed with pip3
  package { 'flask':
    ensure => installed,
    provider => 'pip3',
    # Specify the exact version
    require => Class['python::pip3'],  # Make sure pip3 is installed first
  }

  # Specify the exact version (optional, for clarity)
  $flask_version = '2.1.0'
  # Enforce version using pip options (recommended)
  package { 'flask':
    ensure => $flask_version,
    provider => 'pip3',
    require => Class['python::pip3'],
  }
}
