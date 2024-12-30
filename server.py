from socket import *
import sys

# Set up server socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Fill in start: Bind the server to a specific host and port
server_host = 'localhost'  # Replace with your host or IP
server_port = 8000  # Replace with the port you want to use
serverSocket.bind((server_host, server_port))
serverSocket.listen(1)
# Fill in end

print('Ready to serve...')

while True:
    # Establish the connection
    connectionSocket, addr = serverSocket.accept()

    try:
        # Receive the HTTP request message from the client
        message = connectionSocket.recv(1024).decode()
        print(message)  # For debugging

        # Get the filename from the request
        filename = message.split()[1]
        print(f"Requested filename: {filename}")

        # Try to open the requested file
        try:
            f = open(filename[1:])  # Remove leading '/'
            outputdata = f.read()  # Read the file content
            f.close()

            # Send HTTP response header
            connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
            connectionSocket.send("Content-Type: text/html\r\n\r\n".encode())

            # Send the content of the requested file to the client
            connectionSocket.send(outputdata.encode())
            connectionSocket.close()

        except IOError:
            # Send HTTP 404 error if file is not found
            connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
            connectionSocket.send("Content-Type: text/html\r\n\r\n".encode())
            connectionSocket.send("<html><body><h1>404 Not Found</h1></body></html>".encode())
            connectionSocket.close()

    except Exception as e:
        print(f"Error: {e}")
        connectionSocket.close()

# Close the server socket after finishing
serverSocket.close()
sys.exit()  # Terminate the program
