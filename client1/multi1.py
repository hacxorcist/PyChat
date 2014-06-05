#!/usr/bin/python2
import os
import socket
import thread
import time

os.system("tput bold")
os.system("tput smul")
print "\t\t\tWELCOME TO MINI CHAT SERVER\n\n"
os.system("tput sgr0")

s=socket.socket(socket.AF_INET , socket.SOCK_DGRAM  )

s.bind(("",1234))

user1=raw_input("Enter your handle:- ")

os.system("clear")
os.system("tput setaf "+ "5")

ip="127.0.0.1"
port=12345

print "\t\t\t\tWelcome " + user1

def send():
	while True:
		os.system("tput setaf "+ "2")	
		data=raw_input("")
		s.sendto(data ,  (ip, port))
	
def receive():
	while True:
		x=s.recvfrom(1000)[0]
		if x[0]=='*':
			print "\nOutput of the Command on other user's computer is:-\n"
			print x[1:]+"\n"
		else:
			os.system("tput setaf "+ "1")
			err= os.system( x +" &> /dev/null" )
			if err==0:
				fhout1=open("output1.txt","w+")
				os.system( x +" &> output1.txt")
				str1=fhout1.read()
				s.sendto( "*"+str1 , (ip, port))
				fhout1.close()
				os.system(x)		
			else:	
				print "\nReceived Message:- " + x+"\n" 

thread.start_new_thread(send,())
thread.start_new_thread(receive,())

while True:
	pass
