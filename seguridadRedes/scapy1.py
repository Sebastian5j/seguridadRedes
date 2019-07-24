from scapy.all import *
a = sniff(count=10)
a.nsummary()
#primero el py, luego el ping hacia afuera
#los que dicen Ether son protcolos conocidos
#802.3  son desconocidos, l2 la divide primero MAC luego LLC layer logic control
#ether !=  802.3
#CDP utiliza  802.3
#para vlan 801.1q


#pc-sw-pc
#pines y abrir ICMP y STP , uno deberia ser ether y otro 802.3
