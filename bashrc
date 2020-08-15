# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# User specific aliases and functions
set history = 1000
set complete = enhance
HISTSIZE=5000
HISTFILESIZE=10000
bind '"\e[A": history-search-backward'
bind '"\e[B": history-search-forward'

export PROMPT_COMMAND="history -a; history -c; history -r; $PROMPT_COMMAND"
# enable syntax highlighting

alias ls ="ls -larth"
alias l ="ls -larth"
