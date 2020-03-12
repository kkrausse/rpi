# Raspberry Pi Home

this gives me a centralized place to put everything relating to raspberry pi
stuff

nodes.csv shows the network setup I have at 2841 w wildwood dr, but changes on
location

## Kubernetes

right now, the goal is to deploy a working kubernetes cluster. The subdirectory
[metalc](https://github.com/LibreTexts/metalc) is dedicated to this.

goals:

  - expose multiple services to the outside world with only one IP somehow by
    routing based on the path. This could include using the internal kubernetes
    DNS to find services.

    - this could also use a load balancer thats internal to the network that
      routes based on path somehow? i.e. that cloud native thing thats in metalc

  - persitent volume provisioner
