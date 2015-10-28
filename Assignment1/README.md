# NEU-TELE6603-SDN-Virtualization
##Assignments of TELE 6603 : Software defined Networking and Network Function Virtualization

####Assignment 1

#####Question 1
Test the basic operations and messages of OpenFlow and then write a brief report of your efforts and learning.
For example, you can use Mininet and Wireshark platforms.

As a part of the assignment, I have made use of Mininet emulator, Oracle VM VirtualBox, and wireshark dissector, and xming for windows.The controller that is used is a POX controller and OpenFlow 1.0 standard is used.

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

Summary:

1. Hello:	Controller->Switch	following the TCP handshake, the controller sends its version number to the switch.

2. Hello:	Switch->Controller	the switch replies with its supported version number.

3. Features Request:	Controller->Switch	the controller asks to see which ports are available.

4. Set Config:	Controller->Switch	in this case, the controller asks the switch to send flow expirations.

5. Features Reply:	Switch->Controller	the switch replies with a list of ports, port speeds, and supported tables and actions.

6. Packet-In:	Switch->Controller	a packet was received and it didn't match any entry in the switch's flow table, causing the packet to be sent to the controller.

7. Packet-Out:	Controller->Switch	controller send a packet out one or more switch ports.

8. Flow-Mod:	Controller->Switch	instructs a switch to add a particular flow to its flow table.

9. Flow-Expired:	Switch->Controller	a flow timed out after a period of inactivity.

#####Question 2

Develop and test an OpenFlow 1.5.1  (https://www.opennetworking.org/images/stories/downloads/sdn-resources/onf-specifications/openflow/openflow-switch-v1.5.1.pdf) based SDN controller 

a. Take the code of a simple hub

[Simple hub in pox controller](https://github.com/manishreddy1993/NEU-TELE6603-SDN-Virtualization/blob/master/Assignment1/SimpleHub.py)

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



b. Modify the above code in order to turn the hub into a learning switch

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

c. Modify the above code to develop an OpenFlow 1.5.1 based learning switch



#####Question 3

Develop and test an SDN-enabled IPv4 router:

a. Write and test(by writing router application) the TTL decrement(vendor extension) to beacon

b. For example, you can implement LPM, ARP and ping handling

An IP router can be distinguished from other sorts of packet switching devices in that a router examines the IP protocol header as part of the switching process. It generally removes the Link Layer header a message was received with, modifies the IP header, and replaces the Link Layer header for retransmission. Each network node will have a configured subnet. If a packet is destined for a host within that subnet, the node acts as a switch and forwards the packet with no changes, to a known port or broadcast, just like in the previous exercise. If a packet is destined for some IP address for which the router knows the next hop, it should modify the layer-2 destination and forward the packet to the correct port.

















