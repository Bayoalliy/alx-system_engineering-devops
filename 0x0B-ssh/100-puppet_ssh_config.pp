exec {'echo':
    path => 'usr/bin:/bin',
    command => 'echo "    BatchMode yes\n    IdentityFile ~/.ssh/school" >> ~/.ssh/ssh_config',
    returns => [0, 1],
}
