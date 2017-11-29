import socket
import time
from random import randint

def Main():
	#Main variables and constants 
	portGen = randint(5000, 30000)
	gatewayPort = 4999
	serverPort = 4998
	host = '127.0.0.1'
	port = portGen
	buffer = 1024
	gateway = ('127.0.0.1',gatewayPort)

	#creation of UDP socket
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))
	print "client started\n"
	#sending intial 0 to the gateway
	num = 0
	s.sendto(str(num)+" ," +str(serverPort), gateway)

	#wait 2 seconds before entering the loop
	time.sleep(2)
	while True:
		#current time + 10 seconds (for timeout)
		end= time.time() +10
		#Recieve data and split to data plus address it came from
		data, addr = s.recvfrom(buffer)
		#if acknowledgemnet is 1 send back 1
		if str(data) == "1":
			print "from server: " + str(data)
			s.sendto("1"+" ," +str(serverPort), gateway)
			time.sleep(2)
		#else if acknowledgemnet is 0 send back 0
		elif str(data) == "0":
			print "from server: " + str(data)
			s.sendto("0"+" ," +str(serverPort), gateway)
			time.sleep(2)
		#else if timer runs out and the data recieved is old acknowledgment or is null resend value
		elif (str(data) == ("1") or str(data) == (None)) and time.time() > end:
			print "Server not responding resending number"
			s.sendto("0"+" ," +str(serverPort), gateway)
		#else if timer runs out and the data recieved is old acknowledgment resend value
		elif (str(data) == ("0")) and time.time() > end:
			print "Server not responding resending number"
			s.sendto("1"+" ," +str(serverPort), gateway)

	s.close()

if __name__ == '__main__':
	Main()