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

    