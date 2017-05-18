$masterIP = "10.0.0.2"
$slave1IP = "10.0.0.3"
$slave2IP = "10.0.0.4"

Vagrant.configure("2") do |config|
  config.ssh.insert_key = true
  config.vm.provision "shell", inline: "echo Hello Ansible"

  config.vm.define "master" do |master|
  	master.vm.box = "centos/7"
	master.vm.network "private_network", ip: $masterIP
	master.vm.hostname = "master.mentee"
	master.vm.provision "shell", path: "vagrant/bootstrap_master.sh"
	master.vm.provision "shell", inline: "echo 10.0.0.3 slave1 >> /etc/hosts"
	master.vm.provision "shell", inline: "echo 10.0.0.4 slave2 >> /etc/hosts"
	master.vm.provision "shell", inline: "echo [servers] > /etc/ansible/hosts"
	master.vm.provision "shell", inline: "echo slave[1:2] >> /etc/ansible/hosts"
  end

  config.vm.define "slave1" do |slave1|
  	slave1.vm.box = "centos/7"
	slave1.vm.network "private_network", ip: $slave1IP
	slave1.vm.hostname = "slave1.mentee"
	slave1.vm.provision "shell", inline: "echo 10.0.0.2 master >> /etc/hosts"
  end

  config.vm.define "slave2" do |slave2|
  	slave2.vm.box = "ubuntu/xenial64"
	slave2.vm.network "private_network", ip: $slave2IP
	slave2.vm.hostname = "slave2.mentee"
	slave2.vm.provision "shell", inline: "echo 10.0.0.2 master >> /etc/hosts"
  end
end
