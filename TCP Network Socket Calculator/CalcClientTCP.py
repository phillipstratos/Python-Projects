#!/usr/bin/python
# This is client.py file 
import socket		 	 # Import socket module 
s = socket.socket() 	  		 # Create a socket object 
host = socket.gethostname()                     # Get local machine name 
port = 5555 			 # Reserve a port for your service
s.connect((host, port)) 
print (s.recv(1024).decode()) #Connected to server
while True:
	equation=input("Please give me an equation: ")
	print(equation)
	s.send(equation.encode())
	if equation == 'exit' or equation == 'Exit':	
		s.close 			# Close the socket when done
		exit()
	# Getting result
	result=s.recv(1024).decode()
	print(result)
