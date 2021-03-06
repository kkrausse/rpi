#!/usr/local/bin/python3
#
# Run `./get_macs.py chicks.csv` and then enter the password for spicy.
#
# This looks at the ip field for each row and updates the
# columns for enp1s0 and enp2s0 or adds them if they dont already exist
# by sshing in and running `ip addr` and extracting the mac addresses
# for the interfaces.
#
# so you can put anything in chicks.csv as long as there is an ip field to
# use, this will just update the mac addresses
import sys
import csv
import paramiko
from getpass import getpass


# given output of running `ip addr` in the form of string
# gives the 'link/ether' of the given iface_name
def get_ether(ip_out, iface_name):
    beg = ip_out.find(iface_name)
    if beg < 0:
        return None
    start = ip_out.find('link/ether', beg)
    end = ip_out.find('\n', start)
    return ip_out[start:end].split()[1]

# executes the command on the given ip with the given ssh password to user spicy
# and returns the standard output of that command
def get_output(ip_addr, user, passwd, cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip_addr, username=user, password=passwd)
    inp, outp, errp = ssh.exec_command(cmd)
    return outp.read().decode('utf-8')

# given a csv with headers, this adds the interfaces as new columns
# passed as arguments
if __name__ == "__main__":
    user = raw_input('enter ssh username')
    passwd = getpass("enter ssh password")

    if len(sys.argv) < 3:
        print('usage: `./get_macs.py ips.csv iface1 iface2 ...`' +
                'where ips.csv has at leas an "ip" column')

    ifaces = sys.argv[2:]

    with open(sys.argv[1], 'r') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for iface in ifaces:
            if iface not in fieldnames:
                fieldnames.append(iface)
        rows = []
        for row in reader:
            ip_output = get_output(row['ip'], user, passwd, 'ip addr')
            for iface in ifaces:
                row[iface] = get_ether(ip_output, iface)
            rows.append(row)

    with open(sys.argv[1], 'w') as f:
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        writer.writerows(rows)

