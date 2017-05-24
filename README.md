# Ansible mentornship
### part 1

# Ad-hoc commands
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
```
