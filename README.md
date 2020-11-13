# Raspberry Pi Home

this gives me a centralized place to put everything relating to raspberry pi
stuff

nodes.csv shows the network setup I have at 2841 w wildwood dr, but changes on
location

## Ideas

- kube cluster
- [use this to make a heater for mushrooms](https://twosortoftechguys.wordpress.com/2018/08/13/how-we-made-a-raspberry-pi-controlled-8-outlet-power-box/)
- the meater thing [from this](https://kyleflan.wordpress.com/2017/10/20/tempiture-a-raspberry-pi-powered-wireless-grilling-thermometer-system/)
- for both of these I wanna read a book like "Wiring Simplified" by Hartwell and Richter
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
