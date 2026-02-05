from scapy.all import IP, TCP, sr1, send

# Target information
target_ip = "8.8.8.8"  # Google's DNS server (safe example)
target_port = 80

print("\n--- TCP Three Way Handshake Simulation ---\n")

# 1️⃣ SYN
ip = IP(dst=target_ip)
SYN = TCP(dport=target_port, flags='S', seq=1000)
SYNACK = sr1(ip/SYN, timeout=2)

if SYNACK:
    print("Step 1: SYN sent")
    print("Step 2: SYN-ACK received")

    # 2️⃣ ACK
    ACK = TCP(dport=target_port, flags='A', seq=SYNACK.ack, ack=SYNACK.seq + 1)
    send(ip/ACK)
    print("Step 3: ACK sent — Handshake Completed ✅")
else:
    print("No SYN-ACK received — Target may be unreachable ❌")

print("\n--- Simulation Complete ---")
