import socket


def main():
    server_ip='127.0.0.1'
    server_port=2000
    #Create UDP socket
    try:
        udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        udp_socket.bind((server_ip,server_port))
        print("Socket Created and bound" )
    except:
        print(f"Could not create or bind socket. Error:{err}")
        return
    print("listening for messages...\n")
    client_message, client_address=udp_socket.recvfrom(2000)
    client_message=client_message.decode().strip()
    print(f"Client has send this message{client_message} from {client_address[0]}({client_address[1]})")

if __name__ == "__main__":
    main()    