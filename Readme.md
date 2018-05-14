#PoC. 
## Kubernetes with Vagrant to deploy test environment

vagrant --custom-option=10.10.10.10 up


https://ruby-doc.org/stdlib-2.1.3/libdoc/getoptlong/rdoc/GetoptLong.html
https://gist.github.com/ruanbekker/38a38aea5f325f7fa4a19e795ef4f0d0

## To connect to your vm via ssh from host
ssh -i .vagrant/machines/master/virtualbox/private_key vagrant@10.10.10.10

ssh -i .vagrant/machines/slave/virtualbox/private_key vagrant@10.10.10.11

## venv
venv/bin/python3


vagrant resume


# Unpack vagrant box to local box usage
vagrant box add kube_base kube_base.box

# making box
vagrant package --base kube_master --output kube_base.box