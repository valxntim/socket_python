import sys
from socket import *

# Ensure the correct number of arguments are provided
if len(sys.argv) != 4:
    print("Usage: python client.py <server_host> <server_port> <filename>")
    sys.exit(1)  # Exit the script if arguments are incorrect

# Parse command-line arguments
server_host = sys.argv[1]
server_port = int(sys.argv[2])  # Convert port to an integer
filename = sys.argv[3]

# Print the parsed arguments for confirmation
print(f"Server Host: {server_host}")
print(f"Server Port: {server_port}")
print(f"Filename: {filename}")

# Step 2: Create a socket and connect to the server
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_host, server_port))

# Step 3: Prepare the HTTP GET request message
http_request = f"GET {filename} HTTP/1.1\r\nHost: {server_host}\r\n\r\n"
print(f"Sending HTTP request: {http_request}")

# Step 4: Send the request to the server
client_socket.send(http_request.encode())

# Step 5: Receive the response from the server
response = client_socket.recv(4096).decode()  # Receive the response in chunks

# Print the server's response (for debugging)
print("Server Response:")
print(response)

# Step 6: Close the socket after receiving the response
client_socket.close()
