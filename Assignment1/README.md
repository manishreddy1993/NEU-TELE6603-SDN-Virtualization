# NEU-TELE6603-SDN-Virtualization
##Assignments of TELE 6603 : Software defined Networking and Network Function Virtualization

####Assignment 1

#####Question 1
Test the basic operations and messages of OpenFlow and then write a brief report of your efforts and learning.
For example, you can use Mininet and Wireshark platforms.

As a part of the assignment, I have made use of Mininet emulator, Oracle VM VirtualBox, and wireshark dissector, and xming for windows.The controller that is used is a POX controller and OpenFlow 1.0 standard is used.

####The steps that were followed during the setup are:
 
1. Download the Mininet VM image: [https://github.com/mininet/mininet/wiki/Mininet-VM-Images](https://github.com/mininet/mininet/wiki/Mininet-VM-Images) . 
This image comes with pox controller installed along with openvswitch.
2. Download the virtualization tool called VirtualBox: [https://www.virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads)
3. Download XMing for X11 forwarding: [http://sourceforge.net/projects/xming/](http://sourceforge.net/projects/xming/)

The following openFlow messages are found when the openvswitch and controller were up.

1. Features - Upon TLS(Transport Layer Security) session establishment, the controller sends a features request message to the switch. The switch must reply with a features reply that specifies the capabilities supported by the switch.  

[Features Request Message](https://github.com/manishreddy1993/NEU-TELE6603-SDN-Virtualization/issues/1)
[Features Reply Message](https://github.com/manishreddy1993/NEU-TELE6603-SDN-Virtualization/issues/2)











