import os
import socket
import threading

# Set the wireless interface to ad-hoc mode
os.system("sudo iwconfig wlan0 mode ad-hoc")

# Set the ESSID (network name) of the ad-hoc network
os.system("sudo iwconfig wlan0 essid my_adhoc_network")

# Set the channel number for the ad-hoc network
os.system("sudo iwconfig wlan0 channel 1")

# Set the IP address for the wireless interface
os.system("sudo ifconfig wlan0 192.168.1.1 netmask 255.255.255.0")

# Set the IP address and port number of the remote node to chat with
REMOTE_HOST = "192.168.1.2"
REMOTE_PORT = 12345

# Create a UDP socket for sending and receiving messages
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def receive_messages():
    # Continuously receive messages from the remote node
    while True:
        message, address = sock.recvfrom(1024)
        if address[0] == REMOTE_HOST:
            print(f"Received message: {message.decode('utf-8')}")
        else:
            print(f"Broadcasting message: {message.decode('utf-8')}")
            sock.sendto(message, ("255.255.255.255", REMOTE_PORT))

def send_messages():
    # Continuously send messages to the remote node
    while True:
        message = input("Enter a message: ")
        sock.sendto(message.encode("utf-8"), (REMOTE_HOST, REMOTE_PORT))

# Start a thread to receive messages
threading.Thread(target=receive_messages, daemon=True).start()

# Start a thread to send messages
threading.Thread(target=send_messages, daemon=False).start()
