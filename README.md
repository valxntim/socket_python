# socket_python
Web Server Lab - Python Socket Programming
This project involves developing a simple web server and client in Python that handles HTTP requests and serves files over a TCP connection. The web server listens for incoming connections, parses HTTP GET requests, retrieves requested files from the server’s file system, and sends HTTP responses. If the requested file is not found, the server returns a "404 Not Found" error.

The client connects to the server via a TCP connection, sends an HTTP GET request for a specified file, and displays the server's response, including handling both valid file requests and error responses like "404 Not Found".

This project also provides insights into socket programming, HTTP request/response formatting, and network traffic analysis using Wireshark.

Key Features:
Server: Listens on a specified port, processes HTTP requests, and serves requested files with proper headers.
Client: Sends HTTP GET requests to the server, displays responses, and handles error cases.
Error Handling: Handles "404 Not Found" errors when a file is not available on the server.
Wireshark Analysis: Captures network traffic to monitor the communication between the client and server.
Usage:
Server: Run the server script and place an HTML file in the server's directory.
Client: Use command-line arguments to specify the server host, port, and filename.
