exec {'echo':
    path => 'usr/bin/env bash',
    command => 'echo "    BatchMode yes\n    IdentityFile ~/.ssh/school" >> ~/.ssh/ssh_config',
    returns => [0, 1],
}
