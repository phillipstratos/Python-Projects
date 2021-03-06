#!/usr/bin/python
# This is server.py file 
import socket		 	 # Import socket module 
s = socket.socket() 	  		 # Create a socket object 
host = socket.gethostname()                     # Get local machine name
port = 5555 			 # Reserve a port for your service
s.bind((host, port)) 			 # Bind to the port 
s.listen(5) 			 # Now wait for client connection
c, addr = s.accept() 		# Establish connection with client
print ('Got connection from', addr) 
c.send('Thank you for connecting'.encode()) 
while True:
	equation=c.recv(1024).decode()
	print(equation)
	if equation == 'exit' or equation == 'Exit':
		c.close 		        # Close the socket when done
		exit()
	result=eval(equation)
	print(result)
	c.send(str(result).encode())
