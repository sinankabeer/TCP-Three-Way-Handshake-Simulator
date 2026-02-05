import socket
import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

HOST = '127.0.0.1'
PORT = 65432

def display_typing(message, color=Fore.CYAN, delay=0.05):
    """Typewriter effect for nice animation"""
    for char in message:
        print(color + char, end='', flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL)

def simulate_handshake(conn, addr):
    display_typing(f"\n[Server] Connection request from {addr}", Fore.YELLOW)
    time.sleep(1)

    display_typing("[Server] SYN received...", Fore.GREEN)
    time.sleep(1)

    display_typing("[Server] Sending SYN-ACK...", Fore.MAGENTA)
    conn.sendall(b"SYN-ACK")
    time.sleep(1)

    data = conn.recv(1024)
    if data.decode() == "ACK":
        display_typing("[Server] ACK received ✅", Fore.GREEN)
        time.sleep(0.5)
        display_typing(Fore.CYAN + "\n[Server] TCP 3-Way Handshake Complete 🎉\n")
    else:
        display_typing("[Server] Handshake failed ❌", Fore.RED)

def start_server():
    display_typing("[Server] Starting TCP Handshake Simulation...", Fore.CYAN)
    time.sleep(1)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        display_typing(f"[Server] Listening on {HOST}:{PORT}...", Fore.YELLOW)
        conn, addr = s.accept()

        with conn:
            simulate_handshake(conn, addr)
            display_typing("[Server] Connection closed.\n", Fore.RED)

if __name__ == "__main__":
    start_server()
