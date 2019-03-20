import scapy.all as scapy
import sys

#Utilize Wake on Lan to turn your smartcast vizio t.v. on.
#The device expects a 6 byte broadcast address followed by the devices 6byte mac address repeated 16 times.

#replace the code below with your devices mac address and ip.
#ff:ff:ff:ff:ff:ff
#device mac: a0:6a:44:d5:63:2C
#device ip:

magic = b'\xFF\xFF\xFF\xFF\xFF\xFF'
magic += b'\xA0\x6A\x44\xD5\x63\x2C'
magic += b'\xA0\x6A\x44\xD5\x63\x2C'
magic += b'\xA0\x6A\x44\xD5\x63\x2C'
magic += b'\xA0\x6A\x44\xD5\x63\x2C'

magic += b'\xA0\x6A\x44\xD5\x63\x2C'
magic += b'\xA0\x6A\x44\xD5\x63\x2C'
magic += b'\xA0\x6A\x44\xD5\x63\x2C'
magic += b'\xA0\x6A\x44\xD5\x63\x2C'

magic += b'\xA0\x6A\x44\xD5\x63\x2C'
magic += b'\xA0\x6A\x44\xD5\x63\x2C'
magic += b'\xA0\x6A\x44\xD5\x63\x2B'
magic += b'\xA0\x6A\x44\xD5\x63\x2C'

magic += b'\xA0\x6A\x44\xD5\x63\x2C'
magic += b'\xA0\x6A\x44\xD5\x63\x2C'
magic += b'\xA0\x6A\x44\xD5\x63\x2C'
magic += b'\xA0\x6A\x44\xD5\x63\x2C'

scapy.send(scapy.IP(dst="IP Address of your smart cast TV")/scapy.UDP(dport=7)/magic)
