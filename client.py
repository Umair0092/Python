import socket

def main():
    server_id='127.0.0.1'
    server_port=2000
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    message=input("Enter Message")
    udp_socket.sendto(message.encode(),(server_id,server_port))
    print("message sent")


if __name__ == "__main__":
    main()    