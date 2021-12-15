######################## Mostafa Aboulezz  CU2000187  #########################

import socket # Importing socket as many commands are used from it.
import uuid   # Importing uuid as we will use command from it to get the mac address.

if __name__ == '__main__': # To run the code directly.
   print("Application started")
   s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # To connect the two nodes to be able to communicate and equaled to a variable named s and
   print('TCP socket created')                          # socket.SOCK_STREAM means that it is TCP.
   port = int(input('Please enter the port: ')) # Giving the option to choose which desired port number.
   ipAdrr = input('Please enter the ip: ')   # Giving the option to enter the ip address.
   s.bind((ipAdrr,port))     # To assign the ip address and the port number to a socket.
   p = s.getsockname() # This command gets the ip address followed by the port number.
   print('socket is bound to',p)
   log = 0  
   s.listen(log) # To start listening from the socket.
   print('Socket', p, 'is in listening state') # Print message to show that it is listening.
   client1_socket,client1_addr = s.accept() # Accepting packets from the client.
   print('new client connected from',client1_addr) 
   print ('local end-point socket bound on: ',client1_socket.getsockname())
   print('Client mac address is: ',hex(uuid.getnode())) # Command to get mac address.
   print('The IP Address: ',ipAdrr) # Printing the ip address.
   
   addr = str(client1_addr) # Client address equaled to a variable named addr.
   client1_socket.send(addr.encode()) # Sending client address back to the client.
   
   sockname = str(client1_socket.getsockname())# Client ip and port number equaled to a variable named sockname.
   client1_socket.send(sockname.encode()) # Sending ip followed by the port number to the client.
   
   sendmac = hex(uuid.getnode()) # Client mac address equaled to a variable named sendmac.
   client1_socket.send(sendmac.encode()) # Sending the mac address of the client back.
   
   respond1 = client1_socket.recv(1024).decode() # Recieving the first message.
   if respond1 != 'HELO': # Comparing the recieved message with this string.
       print("could not recieve first respond. *exiting* ")
       s.close() # Closing the socket.
       print("exiting")
   else:
        print(respond1) # Printing the message.
        
   client1_socket.send("250".encode()) # Sending 250 to the client.
   
   respond2 = client1_socket.recv(1024).decode() # Recieving data.
   if respond2 != 'MAIL FROM:<mostafa.akmal@hotmail.com>': # Comparing the recieved message with this string.
       print("email does not match.")
       print("exiting")
       s.close() # Closing the socket.
   else:
       print(respond2) # Printing the message.
       
   client1_socket.send("250".encode()) # Sending 250 to the client.
   
   respond3 = client1_socket.recv(1024).decode() # Recieving data.
   if respond3 != "RCPT TO:<mostafa1.akmal@gmail.com>": # Comparing the recieved message with this string.
       print("second email does not match.")
       print("exiting")
       s.close() # Closing the socket.       
   else:
       print(respond3) # Printing the message.
       
   client1_socket.send("250".encode()) # Sending 250 to the client.
   
   respond4 = client1_socket.recv(1024).decode() # Recieving data.
   if respond4 != "DATA": # Comparing the recieved message with this string.
      print("error recieving data")
      print("exiting")
      s.close() # Closing the socket.     
   else:
      print(respond4) # Printing the message.
       
   client1_socket.send("354".encode()) # Sending 354 to the client.
   
   respond5 = client1_socket.recv(1024).decode() # Recieving data.
   if respond5 != "QUIT": # Comparing the recieved message with this string.
      print("error when recieving.")
      print("exiting")
      s.close() # Closing the socket.   
   else:
      print(respond5) # Printing the message.
      
      client1_socket.send("221".encode()) # Sending 221 to the client.
   
   input('press enter to terminate...')
   client1_socket.close() # Closing the socket  .
   s.close() # Closing the socket.
   print('closed the client socket')
   print('Terminating...')