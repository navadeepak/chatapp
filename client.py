import sys,socket,time
print("\n Welcome to chatting A pplication")
print("\n Starting..........")
time.sleep(1)
s=socket.socket()
shost=socket.gethostname()
ip=socket.gethostbyname(shost)
print(shost,"(",ip,")\n")
host=input("Enter the server address: ")
name=input("Enter Your Name: ")
port=1111
print("\n Connecting ",host)
time.sleep(1)
s.connect((host,port))
print("Connecting...............\n")
s.send(name.encode())
s_name=s.recv(1024)
s_name=s_name.decode()
print(s_name,"has Connected")
while True:
    message=s.recv(1024)
    message=message.decode()
    print(s_name,": ",message)
    message=input("Me: ")
    s.send(message.encode())

