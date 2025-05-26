# Installs a Nginx server with custome HTTP header

exec {'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['install Nginx'],
}

exec {'install Nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  before   => Exec['add_header'],
}

exec { 'add_header':
  provider    => shell,
  environment => ["HOST=${hostname}"],
  command     => 'sed -i "/sites-enabled/a\\tadd_header X-Served-By \"$HOSTNAME\";" /etc/nginx/nginx.conf',
  before      => Exec['restart Nginx'],
}

exec { 'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
