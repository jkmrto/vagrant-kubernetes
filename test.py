from lib import remote_ssh_command as ssh
import paramiko
from lib import kubeadm_init

pkey_path = ".vagrant/machines/master/virtualbox/private_key"
pkey = paramiko.RSAKey.from_private_key_file (pkey_path)
command = """sudo kubeadm init --pod-network-cidr 192.168.0.0/16 --service-cidr 10.96.0.0/12 --service-dns-domain "k8s" --apiserver-advertise-address $(ifconfig enp0s8 | grep 'inet addr'| cut -d':' -f2 | awk '{print $1}')"""
host = "10.10.10.10"
user = "vagrant"
simple_str = ssh.execute_and_return(command, host, user, pkey=pkey)


kubeadm_init.process_output(simple_str, dump_file = "result_real.json")