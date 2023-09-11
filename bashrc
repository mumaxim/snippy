# Copy file/catalog to server
to_server() {    
    scp -r -P 8080 "$1" "USER@IP_ADDRESS:/home/USER/Downloads"
}

# Copy file/catalog from server
from_server() {
    scp -r -P 8080 "USER@IP_ADDRESS:/home/USER/$1" "~/Downloads"
}

# Nice terminal style
export PS1='\[\033[0;32m\]\[\033[0m\033[0;32m\]\u\[\033[0;36m\] @ \[\033[0;36m\]\h \w\[\033[0;32m\]$(__git_ps1)\n\[\033[0;32m\]└─\[\033[0m\033[0;32m\] \$\[\033[0m\033[0;32m\] ▶\[\033[0m\] '

# Mount remote catalog
alias mnt_remote="sudo sshfs -p 8080 USER@IP_ADDRESS:/home/USER /mnt/REMOTE/ -o IdentityFile=/home/maxim/.ssh/RSA_KEY,allow_other"

# Change the title of the current terminal window
title()
{
   echo -ne "\033]0;$*\007"
}

# SSH with terminal title
alias remote_ssh="title REMOTE ; ssh USER@IP_ADDRESS"

# SSH with tmux command
alias remote_ssh="title REMOTE ; ssh USER@IP_ADDRESS -t 'tmux attach; bash -l'"

# Last filename in catalog. Usage example: cd $(last)
alias last="ls -t | head -1"

