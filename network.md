# Network Setup

## current configuration


| Subnet          | IP Range       |
|-----------------|----------------|
| wifi            | 192.168.1.0/24 |
| internal switch | 10.0.0.0/15    |
| pod network     | 10.1.0.0/16    |
| node network    | 10.0.0.0/24    |

see nodes.csv for ethernet addresses

node0 is the "management node"

the "management node"

  - runs a dhcp server for the internal switch network

  - routes from a public ip to internal to the network

### steps on management node

1. `sudo apt install isc-dhcp-server`

1. to `/etc/default/isc-dhcp-server` I added the line:

    INTERFACESv4="eth0"

  since enp3s0 is the interface that is hooked up to the management network.
  Here, we assume enp3s0 is the interface on the manager node that faces the
  internal kubernetes network.

1. to `/etc/network/interfaces`, add

    allow-hotplug eth0

    iface eth0 inet static
      address 10.0.0.100
      netmask 255.255.255.0
      so we get that management interface up

1. run `sudo ifconfig eth0 10.0.0.100`

1. make sure that `/etc/default/isc-dhcp-server` has the line

    INTERFACESv4="eth0"

1. before changing `/etc/dhcp/dhcpd.conf` copy the current one to
  `/etc/dhcp/dhcpd.conf.backup` and set it to this
  ```conf
# dhcpd.conf

# in this example, we serve DHCP requests from 10.0.0.(3 to 253) 
# and we have a router at 10.0.0.1
# these will be the name of the nodes.
subnet 10.0.0.0 netmask 255.255.255.0 {
  authoritative;
  range 10.0.0.3 10.0.0.99; # can't have 10.0.0.100 - 10.0.0.110 because we are
  option routers 10.0.0.100;     # this ends up being the default gateway router
  interface eth0;
  default-lease-time 600;
  max-lease-time 7200;
  option broadcast-address 10.0.0.255;
  option domain-name "pis";
  option domain-name-servers 8.8.8.8;
}

group {
  next-server 10.0.0.100;

  host node0 { hardware ethernet b8:27:eb:d9:2b:f5; fixed-address 10.0.0.100; }
  host node1 { hardware ethernet b8:27:eb:c5:a5:eb; fixed-address 10.0.0.101; }
  host node2 { hardware ethernet b8:27:eb:b6:51:f1; fixed-address 10.0.0.102; }
  host node3 { hardware ethernet b8:27:eb:17:2a:47; fixed-address 10.0.0.103; }
  host node4 { hardware ethernet b8:27:eb:d9:ab:47; fixed-address 10.0.0.104; }
}
  ```

1. `systemctl restart isc-dhcp-server`

1. checked the logs with `grep DHCP /var/log/syslog` and there were some
  requests and handouts, so thats good.

