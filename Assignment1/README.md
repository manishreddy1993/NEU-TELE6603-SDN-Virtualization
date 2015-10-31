# NEU-TELE6603-SDN-Virtualization
##Assignments of TELE 6603 : Software defined Networking and Network Function Virtualization

####Assignment 1

#####Question 1
Test the basic operations and messages of OpenFlow and then write a brief report of your efforts and learning.
For example, you can use Mininet and Wireshark platforms.

As a part of the assignment, I have made use of Mininet emulator, Oracle VM VirtualBox, and wireshark dissector, and xming for windows.The controller that is used is a POX controller and OpenFlow 1.0 standard is used.
For the later part of the assignment, RYU controller was used and OpenFlow 1.3 standard was followed. It was also run Oracle VM VirtualBox. 

####The steps that were followed during the setup are:
 
1. Download the Mininet VM image: [https://github.com/mininet/mininet/wiki/Mininet-VM-Images](https://github.com/mininet/mininet/wiki/Mininet-VM-Images) . 
This image comes with pox controller installed along with openvswitch. Wireshark is also installed by default.
2. Download the virtualization tool called VirtualBox: [https://www.virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads)
3. Download XMing for X11 forwarding: [http://sourceforge.net/projects/xming/](http://sourceforge.net/projects/xming/)

The following openFlow 1.0 messages are found when the openvswitch and controller were up.

[Features Request Message](https://github.com/manishreddy1993/NEU-TELE6603-SDN-Virtualization/issues/1)

[Features Reply Message](https://github.com/manishreddy1993/NEU-TELE6603-SDN-Virtualization/issues/2)

Features - Upon TLS(Transport Layer Security) session establishment, the controller sends a features request message to the switch. The switch must reply with a features reply that specifies the capabilities supported by the switch.  

[Hello Message](https://github.com/manishreddy1993/NEU-TELE6603-SDN-Virtualization/issues/3)

Hello - Hello messages are exchanged between the switch and controller upon connection startup. Hello is used by either controller or switch during connection setup. It is used for version negotiation. When the connection is established, each side must immediately send a Hello message with the version field set to the highest version supported by the sender. If the version negotiation fails, an Error message is sent with type HelloFailed and code Incompatible. The Hello message has no body, it is comprised of only a header. However, uninterpreted data is allowed in the payload for future and proprietary development.

[Echo Request and Reply Messages](https://github.com/manishreddy1993/NEU-TELE6603-SDN-Virtualization/issues/4)

Echo - Echo request/reply messages can be sent from either the switch or the controller, and must return an echo reply. They can be used to indicate the latency, bandwidth, and/or liveness of a controller-switch connection.

[Barrier Request and Reply Messages](https://github.com/manishreddy1993/NEU-TELE6603-SDN-Virtualization/issues/5) 

Barrier - Barrier request/reply messages are used by the controller to ensure message dependencies have been met or to receive notifications for completed operations. This message is initiated by the controller. The OpenFlow controller sends a Barrier Request message to request that the OpenFlow-enabled switch complete processing of all messages sent before the Barrier Request message before processing any messages sent after the Barrier Request message. This ensures that the virtual switch processes all message dependencies and sends all notifications for completed operations before proceeding with new requests.
When the OpenFlow virtual switch receives a Barrier Request message, it queues all subsequent incoming messages, with the exception of echo request and reply messages, until processing of all prior messages is complete. Echo request and reply messages are required to maintain connectivity to the controller.
When the switch completes an operation, it sends a reply message back to the controller. Only after the reply is sent to the controller does the switch mark the message or operation as processed. After the switch completes processing for all operations requested prior to the Barrier Request message, the switch sends a Barrier Reply (OFPT_BARRIER_REPLY) message, which includes the ID of the original request message, to the OpenFlow controller. At that point, the switch resumes processing of the queued messages.

[FlowMod Message](https://github.com/manishreddy1993/NEU-TELE6603-SDN-Virtualization/issues/6)

FlowMod Message - This is one of the main messages, it allows the controller to modify the state of an OpenFlow switch; All FlowMod messages begin with the standard OpenFlow header, containing the appropriate version and type values, followed by the FlowMod structure. This message begins with the standard header and is followed by match, a cookie, which is an opaque field set by the controller, and command which specifies the type of flow table modification. This is followed by idle_timeout, hard_timeout and priority. Idle_timeout and hard_timeout represent number of seconds since packet inactivity and creation since expiration, respectively. Priority implies an order for matches that overlap with higher numbers representing higher priorities. Next in the FlowMod are buffer_id, out_port and flags. Buffer_id is the id of buffered packet that created a packet_in, make FlowMod and then reprocess the packet. Flag is set whether the flow can: send FlowRemoved, send Error if overlap, or function only if controller connectivity is lost. Finally, actions specifies what actions should be taken for matching packets.

[Set Configuration Message](https://github.com/manishreddy1993/NEU-TELE6603-SDN-Virtualization/issues/7)

SetConfiguration - The controller sends the OFPT_SET_CONFIG message to the switch. This includes the set of flags and Max bytes of packet that datapath should send to the controller.

Report:

1. Hello:	Controller->Switch	following the TCP handshake, the controller sends its version number to the switch.

2. Hello:	Switch->Controller	the switch replies with its supported version number.

3. Features Request:	Controller->Switch	the controller asks to see which ports are available.

4. Set Config:	Controller->Switch	in this case, the controller asks the switch to send flow expirations.

5. Features Reply:	Switch->Controller	the switch replies with a list of ports, port speeds, and supported tables and actions.

6. Packet-In:	Switch->Controller	a packet was received and it didn't match any entry in the switch's flow table, causing the packet to be sent to the controller.

7. Packet-Out:	Controller->Switch	controller send a packet out one or more switch ports.

8. Flow-Mod:	Controller->Switch	instructs a switch to add a particular flow to its flow table.

9. Flow-Expired:	Switch->Controller	a flow timed out after a period of inactivity.

OpenFlow Protocol supports three types of messages. These are Controller-to-Switch, Asynchronous and Symmetric.

Controller-to-Switch messages are always initiated by the Controller.Switch initiates the asynchronous messages. Either controller or Switch can initiate symmetric messages.

Controller-to-Switch Messages

Once an OpenFlow channel is established, a Controller can communicate with the switch per request/reply protocol.

A Controller can request supported features from a switch. The switch must reply with supported features and capabilities.

A Controller can inquire current configuration state of a switch and then modify it through controller-to-switch messages.

A Controller can send packet-out messages through a specified port on a switch, as well as forward packets received by a switch.

A Controller can use Barrier request/reply messages to ensure that message dependencies have been met or receive notifications of completed operations.

A Controller can set and query filters on asynchronous messages from a switch using Asynchronous-Configuration message type.

In a multi-controller environment, a controller can request its role from a switch.

A Switch can only respond to a Controller query.


#####Question 2

#####Develop and test an OpenFlow 1.5.1 based SDN controller.
Since OpenFlow 1.5.1 enable vSwitch was not found, I have implemented on 1.1

####a. Take the code of a simple hub

[Simple hub in pox controller](https://github.com/manishreddy1993/NEU-TELE6603-SDN-Virtualization/blob/master/Assignment1/SimpleHub.py)

The mininet topology that is used is a switch that is connected to three hosts to test the functionality.

Enter these commands on the mininet emulator to create the topology.

 $ sudo mn -c
 
 $ sudo mn --topo single,3 --mac --switch ovsk --controller remote

Wait until the application indicates that the OpenFlow switch has connected. When the switch connects, POX will print something like this:

----------
ubuntu@sdnhubvm:~/pox$ cd /home/ubuntu/pox && ./pox.py log.level --DEBUG forwarding.hub

POX 0.5.0 (eel) / Copyright 2011-2014 James McCauley, et al.

INFO:forwarding.hub:Proactive hub running.

DEBUG:core:POX 0.5.0 (eel) going up...

DEBUG:core:Running on CPython (2.7.6/Jun 22 2015 18:00:18)

DEBUG:core:Platform is Linux-3.13.0-27-generic-i686-with-Ubuntu-14.04-trusty

INFO:core:POX 0.5.0 (eel) is up.

DEBUG:openflow.of_01:Listening on 0.0.0.0:6633

INFO:openflow.of_01:[00-00-00-00-00-01 1] connected

INFO:forwarding.hub:Hubifying 00-00-00-00-00-01

---------- 
To test the functionality, just enter the command >pingall 

*** Ping: testing ping reachability

h1 -> h2 h3 

h2 -> h1 h3 

h3 -> h1 h2 

*** Results: 0% dropped (6/6 received)

The command to start the controller and wireshark image can be seen here:
[Pingall in hub](https://github.com/manishreddy1993/NEU-TELE6603-SDN-Virtualization/issues/8)

#####Verify Hub Behavior with tcpdump

Now we verify that hosts can ping each other, and that all hosts see the exact same traffic - the behavior of a hub. To do this, we'll create xterms for each host and view the traffic in each. In the Mininet console, start up three xterms:

 mininet> xterm h1 h2 h3

In the xterms for h2 and h3, run tcpdump, a utility to print the packets seen by a host:

 # tcpdump -XX -n -i h2-eth0

and respectively:

 # tcpdump -XX -n -i h3-eth0

In the xterm for h1, send a ping:

 # ping -c1 10.0.0.2

The ping packets are now going up to the controller, which then floods them out all interfaces except the sending one. You should see identical ARP and ICMP packets corresponding to the ping in both xterms running tcpdump. This is how a hub works; it sends all packets to every port on the network.

[Tcpdump at h2 and h3 showing identical ARP and ICMP requests](https://github.com/manishreddy1993/NEU-TELE6603-SDN-Virtualization/issues/13)

#####b. Modify the above code in order to turn the hub into a learning switch

[Learning switch](https://github.com/manishreddy1993/NEU-TELE6603-SDN-Virtualization/blob/master/Assignment1/LearningSwitch.py)

  When we see a packet, we'd like to output it on a port which will
  eventually lead to the destination.  To accomplish this, we build a
  table that maps addresses to ports.
  We populate the table by observing traffic.  When we see a packet
  from some source coming from some port, we know that source is out
  that port.
  When we want to forward traffic, we look up the desintation in our
  table.  If we don't know the port, we simply send the message out
  all ports except the one it came in on.  (In the presence of loops,
  this is bad!).
  In short, our algorithm looks like this:
  For each packet from the switch:
 
 1) Use source address and switch port to update address/port table
  
 2) Is transparent = False and either Ethertype is LLDP or the packet's destination address is a Bridge Filtered address?
  
 If yes,Drop packet -- don't forward link-local traffic (LLDP, 802.1x)
  
 3) Is destination multicast?
  
 If yes, Flood the packet

 4) Port for destination address in our address/port table?
  
 If No, Flood the packet

 5) Is output port the same as input port?
  
 If yes, Drop packet and similar ones for a while
  
 6) Install flow table entry in the switch so that this
 
 Flow goes out the appopriate port and  Send the packet out appropriate port

[Snapshots and Packet Captures Learning Switch](https://github.com/manishreddy1993/NEU-TELE6603-SDN-Virtualization/issues/9)

#####Question 3

#####Develop and test an SDN-enabled IPv4 router:

#####a. Write and test(by writing router application) the TTL decrement(vendor extension) to beacon

#####b. For example, you can implement LPM, ARP and ping handling

An IP router can be distinguished from other sorts of packet switching devices in that a router examines the IP protocol header as part of the switching process. It generally removes the Link Layer header a message was received with, modifies the IP header, and replaces the Link Layer header for retransmission. Each network node will have a configured subnet. If a packet is destined for a host within that subnet, the node acts as a switch and forwards the packet with no changes, to a known port or broadcast, just like in the previous exercise. If a packet is destined for some IP address for which the router knows the next hop, it should modify the layer-2 destination and forward the packet to the correct port.

The router application is run on a ryu controller. The topology that has been created is [Router Toplogy](https://github.com/manishreddy1993/NEU-TELE6603-SDN-Virtualization/issues/10)

####Steps to test the router application code on ryu controller are:

####1.Create the topology that is shown in the diagram on the mininet emulator 

ryu@ryu-vm:~$ sudo mn --topo linear,3 --mac --switch ovsk --controller remote -x

*** Creating network

*** Adding controller

Unable to contact the remote controller at 127.0.0.1:6633

*** Adding hosts:

h1 h2 h3

*** Adding switches:

s1 s2 s3

*** Adding links:

(h1, s1) (h2, s2) (h3, s3) (s1, s2) (s2, s3)

*** Configuring hosts

h1 h2 h3

*** Running terms on localhost:10.0

*** Starting controller

*** Starting 3 switches

s1 s2 s3

*** Starting CLI:
mininet>

####2.Delete the ip addresses that are automatically attached to each host.
host: h1:

root@ryu-vm:~# ip addr del 10.0.0.1/8 dev h1-eth0

root@ryu-vm:~# ip addr add 172.16.20.10/24 dev h1-eth0

host: h2:

root@ryu-vm:~# ip addr del 10.0.0.2/8 dev h2-eth0

root@ryu-vm:~# ip addr add 172.16.10.10/24 dev h2-eth0

host: h3:

root@ryu-vm:~# ip addr del 10.0.0.3/8 dev h3-eth0

root@ryu-vm:~# ip addr add 192.168.30.10/24 dev h3-eth0
[Snapshot of deleting the ip addresses on each host](https://github.com/manishreddy1993/NEU-TELE6603-SDN-Virtualization/issues/11)

####3.Start rest_router on xterm of controller.
[IPv4 Router Application](https://github.com/osrg/ryu/blob/master/ryu/app/rest_router.py)

Enter the following in the bin directory to start running the controller. 
ryu-manager ryu.app.rest_router

####4. Now, corresponding interface subnets have to be added to the openvswitch. This API makes use of restful services. Hence,simple HTTP POST commands are used to configure the subnets and gateways on the vswitch.

The commands are as follows:
1.On the controller, 

To set the addresses “172.16.20.1/24” and “172.16.30.30/24” for router s1

root@ryu-vm:~# curl -X POST -d '{"address":"172.16.20.1/24"}'http://localhost:8080/router/0000000000000001

root@ryu-vm:~# curl -X POST -d '{"address": "172.16.30.30/24"}' http://localhost:8080/router/0000000000000001

To set the addresses “172.16.10.1/24”, “172.16.30.1/24” and “192.168.10.1/24” for router s2.

root@ryu-vm:~# curl -X POST -d '{"address":"172.16.10.1/24"}' http://localhost:8080/router/0000000000000002

root@ryu-vm:~# curl -X POST -d '{"address": "172.16.30.1/24"}' http://localhost:8080/router/0000000000000002

root@ryu-vm:~# curl -X POST -d '{"address": "192.168.10.1/24"}' http://localhost:8080/router/0000000000000002

To set the addresses “192.168.30.1/24” and “192.168.10.20/24” for router s3.

root@ryu-vm:~# curl -X POST -d '{"address": "192.168.30.1/24"}' http://localhost:8080/router/0000000000000003

root@ryu-vm:~# curl -X POST -d '{"address": "192.168.10.20/24"}' http://localhost:8080/router/0000000000000003

2. Default gateways are added:

host: h1:

root@ryu-vm:~# ip route add default via 172.16.20.1

host: h2:

root@ryu-vm:~# ip route add default via 172.16.10.1

host: h3:

root@ryu-vm:~# ip route add default via 192.168.30.1

3.To set router s2 as the default route of router s1, and set router s1 as the default route of router s2, and router s2 as the default route of router s3, these commands are entered on the controller.

root@ryu-vm:~# curl -X POST -d '{"gateway": "172.16.30.1"}' http://localhost:8080/router/0000000000000001

root@ryu-vm:~# curl -X POST -d '{"gateway": "172.16.30.30"}' http://localhost:8080/router/0000000000000002

root@ryu-vm:~# curl -X POST -d '{"gateway": "192.168.10.1"}' http://localhost:8080/router/0000000000000003

4.To set the static route on s2,

root@ryu-vm:~# curl -X POST -d '{"destination": "192.168.30.0/24", "gateway": "192.168.10.20"}' http://localhost:8080/router/0000000000000002

5.Now verify if the router is performing the basc tasks and required tasks of ARP handling, LPM and ping handling.

The following image shows the wireshark capture of a host on one network pinging the host on another network. Also, it handles ARP for IP to MAC address resolution. A host of one network needs to know the MAC address of the other host it has to contact. This is provided with the help or ARP which broadcasts the IP address of the required MAC address' host. The host send it MAC address to the switch which then will be able to send the packets sent by the sender.

[IPV4 functionality](https://github.com/manishreddy1993/NEU-TELE6603-SDN-Virtualization/issues/12)


















