import socket
import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

HOST = '127.0.0.1'
PORT = 65432

def display_typing(message, color=Fore.CYAN, delay=0.05):
    """Typewriter effect for smooth animation"""
    for char in message:
        print(color + char, end='', flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL)

def perform_handshake():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        display_typing("[Client] Connecting to server...", Fore.YELLOW)
        time.sleep(1)
        s.connect((HOST, PORT))

        display_typing("[Client] Sending SYN...", Fore.GREEN)
        s.sendall(b"SYN")
        time.sleep(1)

        data = s.recv(1024)
        if data.decode() == "SYN-ACK":
            display_typing("[Client] Received SYN-ACK ✅", Fore.MAGENTA)
            time.sleep(1)
            display_typing("[Client] Sending ACK...", Fore.GREEN)
            s.sendall(b"ACK")
            time.sleep(0.5)
            display_typing(Fore.CYAN + "\n[Client] TCP 3-Way Handshake Complete 🎉\n")
        else:
            display_typing("[Client] Handshake failed ❌", Fore.RED)

if __name__ == "__main__":
    perform_handshake()
