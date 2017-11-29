import socket

def Main():
	#Main variables and constants 
	host = '127.0.0.1'
	port = 4999
	buffer =1024
	#creation of socket
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host,port))

	print "Gateway Started."
	while True:
		#recieve data and adress it came from
		data, addr = s.recvfrom(buffer)
		print "message From: " + str(addr)
		toSplit = str(addr)
		#split the address to port and host
		hostID,portStr = toSplit.split(",")
		portID = portStr.replace(")", "")
		portID = portID.replace(" ", "")
		toSplit = str(data)
		#split data recieved to message from client and server port number
		message,serverPort = toSplit.split(",")
		print "from connected user: " + message
		print "forwarding to port: " +serverPort +"\n"
		serverPortCast = (host,int(serverPort))
		#send message to server
		s.sendto(message, serverPortCast)
		#recieve acknowledgment from server
		ack,serverPort = s.recvfrom(buffer)
		print "from server " + str(serverPortCast) +" Acknowledgment: " + str(ack)
		print "forwarding to client at: " + str(addr)
		#send acknowledgment to client
		s.sendto(str(ack),addr)
	s.close()

if __name__ == '__main__':
	Main()