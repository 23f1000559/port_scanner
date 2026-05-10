import socket

ip = input("Enter IP: ")
start = int(input("Start port: "))
end = int(input("End port: "))
# if connection successful , port open , else not 
for port in range(start,end):
    # socket instance
    s = socket.socket()
    s.settimeout(1)
    out = s.connect_ex((ip,port))
    s.close()
    if out == 0:
        print(f"{port} is OPEN")
