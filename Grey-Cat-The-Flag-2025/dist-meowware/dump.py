from scapy.all import *

packets = rdpcap('d:/CTF/dist-meowware/chall.pcap')

print(packets.show())