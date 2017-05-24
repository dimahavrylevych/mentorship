# Ansible mentornship
### part 1

# Ad-hoc commands
<<<<<<< HEAD
* run **Shell command**
```shell
$ ansible dev -b -m shell -a "date"
$ ansible dev -a "date"
```

* install **YUM package**
```shell
$ ansible dev -b -m yum -a "name=mc state=present"
```

* start **Sevice**
```shell
$ ansible dev -b -m yum -a "name=tomcat state=started enabled=yes"
=======
* run **date** shell command on **dev** group with **sudo**(-b)

```shell
$ ansible dev -b -m shell -a "date"
>>>>>>> a9f264f5a349c75fe45530ac448a848e4d3828db
```
