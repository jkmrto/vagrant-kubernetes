
def is_kubeadm_join_command(line):
 # print(line)
  try:
  #  print("{0}, {1}".format(line[0], line[1]))
    return line[0] == "kubeadm" and line[1] == "join"
  except:
    False

file_name = "ouptut_kubeadm.txt"
file_object = open(file_name)
content = [line.split() for line in file_object.readlines() if is_kubeadm_join_command(line.split())][0] 
#print(content)
token = content[content.index('--token') + 1]
discovery_token = content[content.index('--discovery-token-ca-cert-hash') + 1]
