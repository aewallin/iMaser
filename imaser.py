# Simple utility for iMaser monitoring.
#
# Anders Wallin, anders.e.e.wallin "at" gmail.com, 2016-06-27
#
# GNU LESSER GENERAL PUBLIC LICENSE
#           Version 3, 29 June 2007
# see LICENSE.md

import socket

import imaser_parser

def get_reply(UDP_IP, UDP_PORT, MESSAGE):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.sendto(MESSAGE, (UDP_IP, UDP_PORT)) # send

	sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
	sock2.bind(("", UDP_PORT))
	data, addr = sock2.recvfrom(1024) # receive
	return data

def get_params():
	UDP_IP = "192.168.1.10" # The IP of the maser
	UDP_PORT = 14000
	data = get_reply(UDP_IP, UDP_PORT, 'MONIT;\r\n')
	print "received message:", data
	fieldDict = imaser_parser.imaser_parse(data)
	dds = get_reply(UDP_IP, UDP_PORT, 'RDFS;\r\n') # typical reply $RDFS;=1420405750.291768;
	dds = dds[7:-3]
	print "RDFS=", dds
	fieldDict['RDFS'] = float(dds)
	print fieldDict

if __name__ == "__main__":
	# example string for testing
	s = "$41203D4819F157B7882021A4C490CF0D70C01CC0D80EA08509A6900B18D6014CE4B44043B4403B0B29697FE016C5E9CAFDC8C18000CBDC011"
	d = imaser_parser.imaser_parse(s)
	print d
