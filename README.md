# docker-ps
Add pretty print for docker container statuses `dpsa`
Add to .bashrc or .bash_profile
```bash
alias dpsa="python3 $HOME/dpsa.py"
```

Add stop all docker containers command `dstop`
Add to .bashrc or .bash_profile.
```bash
alias dstop=". $HOME/docker_stop.sh"
```

Add remove all docker containers command `drm`
Add to .bashrc or .bash_profile
```bash
alias drm=". $HOME/docker_rm_containers.sh"
```


Git custom commands.
Add to .gitconfig file
```bash
[alias]
    st = status
    co = checkout
    ci = commit
    br = branch
    hist = log --pretty=format:\"%h %ad | %s%d [%an]\" --graph --date=short
    bls = branch --sort=-committerdate
```
st - short command for status
co - short command for checkout
ci - short command for commit 
br - short command for branch
hist - short command for pretty print history
bls - sort command for list all branches
