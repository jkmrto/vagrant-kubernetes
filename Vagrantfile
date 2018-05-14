

Vagrant.configure("2") do |config|
  config.vm.define "master" do |master|
    master.vm.box = "kube_base"
    master.vm.network :private_network, ip: "10.10.10.10"
   # master.vm.provision "shell", path: "start.sh"
    master.vm.hostname = "master"
    master.ssh.insert_key = "true"
    master.ssh.private_key_path = .vagrant/machines/master/virtualbox/private_key
    master.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.memory = 1024
      v.name = "kube_master"
    end

  end

  config.vm.define "slave" do |slave|
    slave.vm.box = "kube_base"
    slave.vm.network :private_network, ip: "10.10.10.11"
    slave.vm.hostname = "slave"
    slave.ssh.insert_key = "true"
    master.ssh.private_key_path = .vagrant/machines/master/virtualbox/private_key

  #  slave.vm.provision "shell", path: "start.sh"
    slave.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.memory = 512
      v.cpus = 1
      v.name = "kube_slave"
    end
  end
end