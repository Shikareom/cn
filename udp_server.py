from socket import *

def receive_file():
    # Define server host and port
    host = "127.0.0.1"  # Listen on localhost
    port = 8080  # Port to listen on
    buf = 1024  # Buffer size

    # Set up the UDP socket
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind((host, port))  # Bind the server to listen on the specified port
    print(f"Server listening on {host}:{port}...")

    # Open the file to save incoming data
    with open("received_file3.txt", 'wb') as f:
        print("Ready to receive file...")

        # Receive the file name first
        data, addr = s.recvfrom(buf)
        file_name = data.decode()  # Decode the file name into a string
        print(f"Receiving file: {file_name}")

        # Receive the file data in chunks
        try:
            while True:
                data, addr = s.recvfrom(buf)
                if not data:
                    break  # No more data, end the transfer
                f.write(data)  # Write the raw binary data directly to the file
                print(f"Received {len(data)} bytes...")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            print("File download complete.")
            s.close()

if __name__ == "__main__":
    receive_file()
