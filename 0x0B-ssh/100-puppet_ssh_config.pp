exec {'echo':
    path => 'usr/bin/env bash',
    command => 'echo "    BatchMode yes\n    IdentityFile ~/.ssh/school" >> ~/.ssh/school",
    returns => [0, 1],
}
