import socket

def Main():
	#main constants and variables
	host = '127.0.0.1'
	port = 4998
	buffer =1024

	#creation of UDP socket
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host,port))


	print "Server Started."
	while True:
		#Recieve data & address it came from
		data, addr = s.recvfrom(buffer)
		print str(data) + ",  " + str(addr)
		#if the value recieved is 0 send back an acknowledgement of 1
		if str(data) == "0 ":
			s.sendto("1", addr)
		#else if the value recieved is 1 send back an acknowledgement of 0
		elif str(data) == "1 ":
			s.sendto("0", addr)
	s.close()

if __name__ == '__main__':
	Main()