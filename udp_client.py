from socket import *

def send_file():
    # Define server IP address and file to send
    host = "127.0.0.1"  # Change this to the server's IP address
    port = 8080  # Server port to send data
    buf = 1024  # Buffer size
    file_name = r"C:\Users\omshi\Documents\CN\CN\UDP file transfer\test_file.txt"  # File to send

    # Set up the UDP socket
    s = socket(AF_INET, SOCK_DGRAM)
    addr = (host, port)

    try:
        # Open the file in binary read mode
        with open(file_name, "rb") as f:
            # Send the file name first
            s.sendto(file_name.encode(), addr)
            print(f"Sending file: {file_name}")

            # Read the file data in chunks of size `buf`
            data = f.read(buf)

            # Send the file data in chunks
            while data:
                s.sendto(data, addr)  # Send the data as bytes
                print(f"Sending... {len(data)} bytes")
                data = f.read(buf)

            # Send EOF marker to indicate end of file transfer
            s.sendto("EOF".encode(), addr)
            print("File transfer completed, EOF sent.")

    except FileNotFoundError:
        print(f"Error: The file {file_name} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        s.close()

if __name__ == "__main__":
    send_file()
