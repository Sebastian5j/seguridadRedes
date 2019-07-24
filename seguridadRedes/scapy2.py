from scapy.all import *
#comentario mi ip gw era 192.168.3.1 /24
send(IP(dst="192.168.3.200")/ICMP()) #capa3
#sendp capa 2

