import matplotlib.pyplot as plt
import matplotlib.animation as animation
from colorama import Fore, Style

# -------------------------------------------------
# Choose scenario
# -------------------------------------------------
print(Fore.CYAN + "\n--- TCP 3-Way Handshake Failure Demonstration ---" + Style.RESET_ALL)
print("Choose a scenario:")
print("1️⃣ Normal handshake (successful)")
print("2️⃣ SYN-ACK lost (server reply fails)")
print("3️⃣ ACK lost (final step fails)")

choice = input("\nEnter option (1/2/3): ").strip()

if choice == "1":
    scenario = "normal"
elif choice == "2":
    scenario = "synack_lost"
elif choice == "3":
    scenario = "ack_lost"
else:
    print(Fore.RED + "Invalid choice. Defaulting to normal handshake." + Style.RESET_ALL)
    scenario = "normal"

# -------------------------------------------------
# Console Simulation
# -------------------------------------------------
print(Fore.YELLOW + "\n[CLIENT] Sending SYN to Server...")
if scenario != "synack_lost":
    print(Fore.CYAN + "[SERVER] Received SYN, sending SYN-ACK...")
else:
    print(Fore.RED + "[SERVER] SYN lost or timed out ❌")
if scenario == "ack_lost":
    print(Fore.CYAN + "[CLIENT] Received SYN-ACK, sending ACK...")
    print(Fore.RED + "[ACK] Lost! Connection not established ❌")
elif scenario == "normal":
    print(Fore.GREEN + "[CLIENT] Received SYN-ACK, sent ACK successfully ✅")
    print(Fore.GREEN + "Connection established successfully!" + Style.RESET_ALL)
else:
    print(Fore.RED + "Client timed out waiting for SYN-ACK ❌" + Style.RESET_ALL)

# -------------------------------------------------
# Visualization
# -------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

# Hosts
ax.text(1, 5, "Client\n192.168.1.2", fontsize=12, fontweight='bold', color="#007acc", ha='center')
ax.text(8.5, 5, "Server\n192.168.1.10", fontsize=12, fontweight='bold', color="#d9534f", ha='center')
ax.plot([1.5, 8], [4.8, 4.8], '--', color='gray', alpha=0.4)

# Arrows placeholders
arrow_syn, = ax.plot([], [], color='blue', lw=2)
arrow_synack, = ax.plot([], [], color='orange', lw=2)
arrow_ack, = ax.plot([], [], color='green', lw=2)
cross_marker, = ax.plot([], [], 'rx', markersize=14, mew=3)

# Text placeholders
status_text = ax.text(2, 1, "", fontsize=12, color="black")
packet_info = ax.text(2, 0.5, "", fontsize=10, color="gray")

# -------------------------------------------------
# Animation logic
# -------------------------------------------------
def animate(i):
    cross_marker.set_data([], [])
    if i < 20:
        arrow_syn.set_data([1.5 + i * 0.33, 1.5], [4.2, 4.2])
        status_text.set_text("SYN →")
        packet_info.set_text("SEQ=1000, ACK=0")
    elif i < 40:
        if scenario == "synack_lost":
            cross_marker.set_data(5, 3.8)
            status_text.set_text("❌ SYN-ACK Lost")
            packet_info.set_text("Timeout - No response")
        else:
            arrow_synack.set_data([8 - (i - 20) * 0.33, 8], [3.5, 3.5])
            status_text.set_text("SYN-ACK →")
            packet_info.set_text("SEQ=5000, ACK=1001")
    elif i < 60:
        if scenario == "ack_lost":
            arrow_ack.set_data([1.5 + (i - 40) * 0.33, 1.5], [2.8, 2.8])
            cross_marker.set_data(5, 2.8)
            status_text.set_text("❌ ACK Lost")
            packet_info.set_text("Connection Failed")
        elif scenario == "normal":
            arrow_ack.set_data([1.5 + (i - 40) * 0.33, 1.5], [2.8, 2.8])
            status_text.set_text("ACK →")
            packet_info.set_text("Connection Established ✅")
        else:
            packet_info.set_text("")
    return arrow_syn, arrow_synack, arrow_ack, status_text, packet_info, cross_marker

ani = animation.FuncAnimation(fig, animate, frames=80, interval=100, blit=False, repeat=False)
plt.title("TCP Handshake Simulation - " + scenario.replace("_", " ").title(), fontsize=14, fontweight='bold')
plt.show()
