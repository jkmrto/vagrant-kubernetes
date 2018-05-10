#PoC. 
## Kubernetes with Vagrant to deploy test environment

vagrant --custom-option=10.10.10.10 up
https://ruby-doc.org/stdlib-2.1.3/libdoc/getoptlong/rdoc/GetoptLong.html

## To connect to your vm via ssh from host
ssh -i .vagrant/machines/master/virtualbox/private_key vagrant@10.10.10.10
ssh -i .vagrant/machines/slave/virtualbox/private_key vagrant@10.10.10.11

## venv
venv/bin/python3