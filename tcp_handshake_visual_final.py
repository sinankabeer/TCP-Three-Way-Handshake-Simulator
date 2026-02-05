import matplotlib.pyplot as plt
import matplotlib.animation as animation
from colorama import Fore, Style

# Console output simulation
print(Fore.CYAN + "\n--- TCP 3-Way Handshake Simulation ---" + Style.RESET_ALL)
print(Fore.YELLOW + "1️⃣ Client sends SYN to Server")
print("2️⃣ Server replies with SYN-ACK")
print("3️⃣ Client responds with ACK")
print(Fore.GREEN + "\nConnection Established Successfully!\n" + Style.RESET_ALL)

# Set up the figure
fig, ax = plt.subplots(figsize=(8, 5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

# Add host labels
ax.text(1, 5, "Client", fontsize=14, fontweight='bold', color="#007acc")
ax.text(8, 5, "Server", fontsize=14, fontweight='bold', color="#d9534f")

# Draw static dashed line (connection)
ax.plot([1.5, 8], [4.8, 4.8], '--', color='gray', alpha=0.5)

# Arrows for animation
arrow_syn, = ax.plot([], [], color='blue', lw=2)
arrow_synack, = ax.plot([], [], color='orange', lw=2)
arrow_ack, = ax.plot([], [], color='green', lw=2)

# Step text
step_text = ax.text(2, 1, "", fontsize=12, color="black")

# Signature text
ax.text(3, 0.5, "Project by Sinan Muhammed Kabeer", fontsize=10, color="gray", style='italic')

# Animation function
def animate(i):
    if i < 20:
        arrow_syn.set_data([1.5 + i * 0.33, 1.5], [4.2, 4.2])
        step_text.set_text("Step 1: SYN →")
    elif i < 40:
        arrow_synack.set_data([8 - (i - 20) * 0.33, 8], [3.5, 3.5])
        step_text.set_text("Step 2: SYN-ACK →")
    elif i < 60:
        arrow_ack.set_data([1.5 + (i - 40) * 0.33, 1.5], [2.8, 2.8])
        step_text.set_text("Step 3: ACK →")
    else:
        step_text.set_text("Connection Established ✅")

    return arrow_syn, arrow_synack, arrow_ack, step_text

ani = animation.FuncAnimation(fig, animate, frames=80, interval=100, blit=False, repeat=False)
plt.title("TCP Three-Way Handshake Visualization", fontsize=14, fontweight='bold')
plt.show()
