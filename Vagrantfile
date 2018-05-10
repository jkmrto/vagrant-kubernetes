require 'getoptlong'

opts = GetoptLong.new(
  [ '--custom-option', GetoptLong::OPTIONAL_ARGUMENT ]
)

customParameter=''

opts.each do |opt, arg|
  case opt
    when '--custom-option'
      customParameter=arg
  end
end

Vagrant.configure("2") do |config|
  config.vm.define "master" do |master|
    master.vm.box = "ubuntu/xenial64"
    master.vm.network :private_network, ip: "#{customParameter}"
    master.vm.provision "shell", path: "start.sh"
    master.vm.hostname = "master"
    master.ssh.insert_key = "true"
    master.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.memory = 1024
      v.name = "kube_master"
    end

  end

  config.vm.define "slave" do |slave|
    slave.vm.box = "ubuntu/xenial64"
    slave.vm.network :private_network, ip: "10.10.10.11"
    slave.vm.hostname = "slave"
    slave.ssh.insert_key = "true"

  #  slave.vm.provision "shell", path: "start.sh"
    slave.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.memory = 512
      v.cpus = 1
      v.name = "kube_slave"
    end
  end
end