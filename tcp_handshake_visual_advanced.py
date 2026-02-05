import matplotlib.pyplot as plt
import matplotlib.animation as animation
from colorama import Fore, Style

# -----------------------------
# Console Output (Simulation)
# -----------------------------
print(Fore.CYAN + "\n--- TCP 3-Way Handshake Simulation ---" + Style.RESET_ALL)
print(Fore.YELLOW + "1️⃣ Client (192.168.1.2) sends SYN to Server (192.168.1.10)")
print("   [SEQ=1000, ACK=0, FLAG=SYN]")
print(Fore.YELLOW + "2️⃣ Server (192.168.1.10) replies with SYN-ACK")
print("   [SEQ=5000, ACK=1001, FLAG=SYN,ACK]")
print(Fore.YELLOW + "3️⃣ Client (192.168.1.2) responds with ACK")
print("   [SEQ=1001, ACK=5001, FLAG=ACK]")
print(Fore.GREEN + "\n✅ TCP Connection Established Successfully!\n" + Style.RESET_ALL)

# -----------------------------
# Visualization Setup
# -----------------------------
fig, ax = plt.subplots(figsize=(8, 5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

# Host labels
ax.text(1, 5, "Client\n192.168.1.2", fontsize=12, fontweight='bold', color="#007acc", ha='center')
ax.text(8.5, 5, "Server\n192.168.1.10", fontsize=12, fontweight='bold', color="#d9534f", ha='center')

# Static connection line
ax.plot([1.5, 8], [4.8, 4.8], '--', color='gray', alpha=0.4)

# Arrow placeholders
arrow_syn, = ax.plot([], [], color='blue', lw=2, label="SYN")
arrow_synack, = ax.plot([], [], color='orange', lw=2, label="SYN-ACK")
arrow_ack, = ax.plot([], [], color='green', lw=2, label="ACK")

# Step text
step_text = ax.text(2, 1, "", fontsize=12, color="black")

# Packet info
packet_info = ax.text(2, 0.5, "", fontsize=10, color="gray")

# -----------------------------
# Animation Function
# -----------------------------
def animate(i):
    if i < 20:
        arrow_syn.set_data([1.5 + i * 0.33, 1.5], [4.2, 4.2])
        step_text.set_text("Step 1: SYN →")
        packet_info.set_text("SEQ=1000, ACK=0, FLAG=SYN")
    elif i < 40:
        arrow_synack.set_data([8 - (i - 20) * 0.33, 8], [3.5, 3.5])
        step_text.set_text("Step 2: SYN-ACK →")
        packet_info.set_text("SEQ=5000, ACK=1001, FLAG=SYN,ACK")
    elif i < 60:
        arrow_ack.set_data([1.5 + (i - 40) * 0.33, 1.5], [2.8, 2.8])
        step_text.set_text("Step 3: ACK →")
        packet_info.set_text("SEQ=1001, ACK=5001, FLAG=ACK")
    else:
        step_text.set_text("Connection Established ✅")
        packet_info.set_text("")

    return arrow_syn, arrow_synack, arrow_ack, step_text, packet_info

# -----------------------------
# Animate and Display
# -----------------------------
ani = animation.FuncAnimation(fig, animate, frames=80, interval=100, blit=False, repeat=False)
plt.title("TCP Three-Way Handshake Visualization", fontsize=14, fontweight='bold')
plt.legend(loc='lower right')
plt.show()
