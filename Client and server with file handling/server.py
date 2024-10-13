import socket

# Database to store student attendance
attendance_db = []

# Load attendance from file
def load_attendance():
    global attendance_db
    try:
        with open("users.txt", "r") as f:
            attendance_db = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        with open("users.txt", "w") as f:
            pass  # Create the file if it doesn't exist

# Save attendance to file
def save_attendance():
    with open("users.txt", "w") as f:
        for student in attendance_db:
            f.write(student + '\n')

def check_in(roll_number):
    if any(roll_number in student for student in attendance_db):
        return f"You are already here."
    else:
        attendance_db.append(f"{roll_number}-CI")
        save_attendance()
        return f"Welcome Student {roll_number}"

def check_out(roll_number):
    # Ensure the student is checked in
    if f"{roll_number}-CI" not in attendance_db:
        return f"You didn't check in today. Contact System Administrator."
    
    # Remove check-in record and add check-out record at the beginning
    attendance_db.remove(f"{roll_number}-CI")
    attendance_db.insert(0, f"{roll_number}-CO")
    save_attendance()
    return f"GoodBye Student {roll_number}! Have a nice day."

def print_attendance():
    print("Current Attendance List:")
    for student in attendance_db:
        print(student)

def main():
    # Load attendance from file when the server starts
    load_attendance()

    # Define server address and port
    server_ip = '127.0.0.1'
    server_port = 2000

    # Create UDP socket
    try:
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.bind((server_ip, server_port))
        print("Socket Created and Bound")
    except socket.error as err:
        print(f"Could not create or bind socket. Error: {err}")
        return

    print("Listening for Messages...\n")

    while True:
        # Receive the message from the client
        try:
            client_message, client_address = udp_socket.recvfrom(2000)
            client_message = client_message.decode().strip()
            print(f"Received Message from IP: {client_address[0]} and Port No: {client_address[1]}")
            print("Client Message: " + client_message)
        except socket.error as err:
            print(f"Receive Failed. Error: {err}")
            continue

        # Process the message (roll number and action)
        roll_number, action = client_message[:8], client_message[9:]
        if action == "CI":
            response = check_in(roll_number)
        elif action == "CO":
            response = check_out(roll_number)
        else:
            response = "Invalid action. Use CI for check-in and CO for check-out."

        # Print current attendance
        print_attendance()

        # Send the response back to the client
        try:
            udp_socket.sendto(response.encode(), client_address)
        except socket.error as err:
            print(f"Send Failed. Error: {err}")

if __name__ == "__main__":
    main()
