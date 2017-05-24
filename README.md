# Ansible mentornship
### part 1

## Ad-hoc commands
* run **date** shell command on **dev** group with **sudo**(-b)
'''shell
$ ansible dev -b -m shell -a "date"
'''
