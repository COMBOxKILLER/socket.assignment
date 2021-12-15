######################## Mostafa Aboulezz  CU2000187  #########################

import socket # Importing socket as many commands are used from it.

if __name__ == '__main__':
   print("Application started")
   s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # To connect the two nodes to be able to communicate and equaled to a variable named s and
   print('TCP socket created')                          #socket.SOCK_STREAM means that it is TCP.
   port = int(input('Please enter the port: ')) # Giving the option to choose which desired port number.
   ip = input('Please enter the ip: ') # Giving the option to enter the ip address.
   
   server_address =(ip,port) # The server address ip address and the port.
   s.connect(server_address) # Command to connect the client with the server.
   
   addr = s.recv(1024).decode() # Recieving message.
   print('socket connected to',addr) # Printing the message.
   
   sockrecv = s.recv(1024).decode() # Recieving message.
   print('local end-point is bound to',sockrecv) # Printing the message.
   
   sendmac = s.recv(1024).decode() # Recieving message.
   print('Mac address:',sendmac) # Printing the message.
       
   helomessage = 'HELO'
   s.send(helomessage.encode()) # Sending HELO to the server.
   
   recv1 = s.recv(1024).decode() # Recieving message.
   if recv1 != '250' : # Comparing the recieved message with this string.
       print ('250 reply not received from server.1')
       print("exiting")
       s.close() # Closing the socket .       
   else:
       print (recv1) # Printing the message.
       
   mailfromCommand = 'MAIL FROM:<mostafa.akmal@hotmail.com>'
   s.send(mailfromCommand.encode()) # Sending MAIL FROM:<mostafa.akmal@hotmail.com> to the server.
   
   recv2 = s.recv(1024).decode() # Recieving message.
   if recv2 != '250' : # Comparing the recieved message with this string.
       print ('250 reply not received from server.2')
       print("exiting")
       s.close() # Closing the socket    
   else:
       print (recv2) # Printing the message
       
   rcptToCommand = 'RCPT TO:<mostafa1.akmal@gmail.com>'
   s.send(rcptToCommand.encode())
   
   recv3 = s.recv(1024).decode() # Recieving message.
   if recv3 != '250' : # Comparing the recieved message with this string. 
       print ('250 reply not received from server.3')
       print("exiting")
       s.close() # Closing the socket.
   else:
       print (recv3) # Printing the message.
       
   dataCommand = 'DATA'
   s.send(dataCommand.encode()) # Sending DATA to the server.
   
   recv4 = s.recv(1024).decode() # Recieving message.
   if recv4 != '354' : # Comparing the recieved message with this string.
       print ('354 reply not received from server.4')
       print("exiting")
       s.close() # Closing the socket     .   
   else:
       print (recv4) # Printing message.
       
   quitCommand = "QUIT"
   s.send(quitCommand.encode()) # Sending QUIT to the server.
   
   recv5 = s.recv(1024).decode() # Recieving message.
   if recv5 != '221' : # Comparing the recieved message with this string.
       print ('221 reply not received from server.5')
       print("exiting")
       s.close() # Closing the socket.       
   else:
       print (recv5 ) # Printing message.
       
   input('Press enter to terminate...  ')
   s.close() # Closing the socket. 
   print('Terminating...')
   