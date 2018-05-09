Vagrant.configure("2") do |config|
  config.vm.define "master" do |master|
    master.vm.box = "ubuntu/xenial64"
    master.vm.network :public_network, bridge: "Intel(R) 82579LM Gigabit Network Connection"
    master.vm.provision "shell", path: "example.sh"

    master.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.memory = 2048
      v.name = "kube_master"
    end

  end

  config.vm.define "slave" do |slave|
    slave.vm.box = "ubuntu/xenial64"
    slave.vm.network :public_network, bridge: "Intel(R) 82579LM Gigabit Network Connection"
    slave.vm.provision "shell", path: "example.sh"
    slave.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.memory = 1024
      v.cpus = 1
      v.name = "kube_slave"
    end
  end
end