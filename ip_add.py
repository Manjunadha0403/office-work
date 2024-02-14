import socket

url = "fastapi.tiangolo.com"
ip_address = socket.gethostbyname(url)

print(f"The IP address of {url} is {ip_address}")
