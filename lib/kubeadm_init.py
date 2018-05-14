import json

def is_kubeadm_join_command(line):
 # print(line)
  try:
  #  print("{0}, {1}".format(line[0], line[1]))
    return line[0] == "kubeadm" and line[1] == "join"
  except:
    False

def process_output(output, dump_file = "result.json"):
  content = [line.split() for line in output if is_kubeadm_join_command(line.split())][0] 
  output_dict = {
    "token": content[content.index('--token') + 1], 
    "discovery_token": content[content.index('--discovery-token-ca-cert-hash') + 1]
  }

  fp = open(dump_file, 'w')
  json.dump(output_dict, fp)


def test():
  file_name = "ouptut_kubeadm.txt"
  file_object = open(file_name)
  process_output(file_object.readlines())
