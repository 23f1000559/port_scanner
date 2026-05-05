import socket

ip = "127.0.0.1"
# if connection successful , port open , else not 
for port in [22, 80, 443, 3306, 8080]:
    # socket instance
    s = socket.socket()
    s.settimeout(1)
    out = s.connect_ex((ip,port))
    s.close()
    if out == 0:
        print(f"{port} is OPEN")
