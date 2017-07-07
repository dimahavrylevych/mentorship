Vagrant.configure("2") do |config|
  config.vm.provision "shell", inline: "echo Hello Ansible"
  config.ssh.insert_key = true

  config.vm.define "master" do |master|
  	master.vm.box = "mycentosbox"
	  master.vm.network "private_network", ip: "192.168.61.2"
	  master.vm.hostname = "master.mentorship"
	  master.vm.provision "shell", path: "vagrant/bootstrap_master.sh"
    master.vm.synced_folder "ansible-welcome/", "/etc/ansible/"
    master.vm.synced_folder "ansible-roles/", "/etc/ansible/roles"
    master.hostsupdater.aliases = ["master.mentorship"]
    master.vm.provision "file", source: "C:/Users/Dmytro_Havrylevych/.vagrant.d/insecure_private_key", destination: "/home/vagrant/.ssh/insecured"
    master.vm.provision "shell", inline: "sudo chmod 600 /home/vagrant/.ssh/insecured"
    #master.vm.provision "file", source: "C:/Users/Dmytro_Havrylevych/.vagrant.d/boxes/mycentosbox/0/virtualbox/vagrant_private_key", destination: "~/.ssh/id_rsa"
    #master.vm.provision "file", source: "C:/Users/Dmytro_Havrylevych/mentorship/hosts/.vagrant/machines/db/virtualbox/private_key", destination: "~/.ssh/db_id_rsa"
  end

end
