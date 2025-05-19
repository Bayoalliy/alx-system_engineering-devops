

package {'nginx':
    ensure => installed,
}

service {'nginx':
    ensure => running,
    enable => true,
}

file {'/var/www/html/index.nginx-debian.html':
    ensure  => file,
    content => 'Hello World',
}

file {'/etc/nginx/sites-available/default':
    ensure => file,
}

exec {'adding redirectiom':
    command => "sed -i  '/server_name _/a\\trewrite ^\/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;' /etc/nginx/sites-available/default",
    path    => ['/usr/bin', '/usr/sbin'],
}

file {'/var/www/html/404.html':
    ensure  => file,
    content => "Ceci n'est pas une page.",
}

exec {'adding error endpoint':
    command => "sed -i '/# pass PHP/i\\terror_page 404 /404.html;\n\tlocation = /404.html {\n\t\tinternal;\n\t}' /etc/nginx/sites-available/default",
    path    => ['/usr/bin', '/usr/sbin'],
}

exec {'restart nginx':
    command => '/usr/sbin/service nginx restart',
}
