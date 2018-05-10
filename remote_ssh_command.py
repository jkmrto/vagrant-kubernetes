#!/usr/bin/python3
__author__ = "mendrugory"

import sys
import time
import select
import paramiko
import scp


def send_cmd_and_print_response(ssh, cmd):
    print("> {}".format(cmd))
    stdin, stdout, stderr = ssh.exec_command(cmd)
    print("\nResponse:\n")
    # Wait for the command to terminate
    while not stdout.channel.exit_status_ready():
        # Only print data if there is data to read in the channel
        if stdout.channel.recv_ready():
            rl, wl, xl = select.select([stdout.channel], [], [], 0.0)
            if len(rl) > 0:
                # Print data from stdout
                print(stdout.channel.recv(1024).decode('utf-8'))


def copy_file_and_print_response(scp, file_paths):
    (source, target) = file_paths
    print("> Source: {}".format(source))
    print("> Target: {}".format(target))
    return scp.put(source, target)


def send_cmd_and_return_response(ssh, cmd):
    """
    It is necessary to check that the method "stdout.channel.recv_ready()"
    is completely empty that is {stdout.channel.recv_ready() == False} even
    after checking stdout "channel.exit_status_ready()" because they are
    different channel (ctrl/data) so they could be no synchronized
    :param ssh:
    :param cmd:
    :return:
    """
    print("> {}".format(cmd))
    stdin, stdout, stderr = ssh.exec_command(cmd)
#    print("\nResponse:\n")
    simple_str = ""
    # Wait for the command to terminate
    stdout.channel.recv_exit_status()
    # Wait until the buffer is completely empty
    while stdout.channel.recv_ready():
        rl, wl, xl = select.select([stdout.channel], [], [], 0.0)
        if len(rl) > 0:
            # Print data from stdout
            simple_str += str(stdout.channel.recv(1024).decode('utf-8'))

    return simple_str


def ssh_execution(func):
    def wrapper(argument, host, user, password=None):
        i = 1
        ssh = None
        #
        # Try to connect to the host.
        # Retry a few times if it fails.
        #
        while True:
            print("Trying to connect to {} ({}/30)".format(host, i))

            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                if password:
                    ssh.connect(host, username=user, password=password, allow_agent=False,look_for_keys=False)
                else:
                    ssh.connect(host, username=user,allow_agent=True,look_for_keys=True)
                print("Connected to {}".format(host))
                break
            except paramiko.AuthenticationException as e:
                print(str(e))
                print("Authentication failed when connecting to {}".format(host))
                sys.exit(1)
            except Exception as e:
                print(str(e))
                print("Could not SSH to %s, waiting for it to start".format(host))
                i += 1
                time.sleep(2)

            # If we could not connect within time limit
            if i == 30:
                print("Could not connect to {}. Giving up".format(host))
                sys.exit(1)

        # Execute the arguments (non-blocking)
        simple_str = func(ssh, argument)

        #
        # Disconnect from the host
        #
        print("Command done, closing SSH connection")
        ssh.close()
        return simple_str
    return wrapper

@ssh_execution
def execute(ssh, cmd):
    send_cmd_and_print_response(ssh, cmd)

@ssh_execution
def copy(ssh, file_path):
    file_name = file_path.split("/")[-1]
    copy_file_and_print_response(scp.SCPClient(ssh.get_transport()), (file_path, file_name))

@ssh_execution
def execute_and_return(ssh, cmd):
    simple_str = send_cmd_and_return_response(ssh, cmd)
    return simple_str




























