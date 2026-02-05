import matplotlib.pyplot as plt
import matplotlib.animation as animation
from colorama import Fore, Style

# Handshake steps
steps = [
    ("Client sends SYN", "Client → Server: SYN"),
    ("Server sends SYN-ACK", "Server → Client: SYN-ACK"),
    ("Client sends ACK", "Client → Server: ACK"),
]

# Console log
print(Fore.CYAN + "\n--- TCP THREE-WAY HANDSHAKE SIMULATION ---\n" + Style.RESET_ALL)

for i, (title, action) in enumerate(steps, 1):
    print(Fore.YELLOW + f"Step {i}: " + Style.RESET_ALL + title)
print("\n" + Fore.GREEN + "Handshake Complete! Connection Established ✅" + Style.RESET_ALL)

# --- Visualization Setup ---
fig, ax = plt.subplots(figsize=(7, 4))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis("off")

client_y = 4
server_y = 2

client_text = ax.text(1, client_y + 0.3, "CLIENT", fontsize=12, fontweight="bold", color="deepskyblue")
server_text = ax.text(8, server_y + 0.3, "SERVER", fontsize=12, fontweight="bold", color="orange")

arrow = None
label = ax.text(4, 5, "", fontsize=12, ha="center", color="white", bbox=dict(facecolor="gray", alpha=0.6, boxstyle="round,pad=0.3"))

# --- Animation Function ---
def animate(i):
    global arrow
    if arrow:
        arrow.remove()

    if i == 0:  # SYN
        arrow = ax.arrow(2, client_y, 5, -2, head_width=0.2, color="deepskyblue", linewidth=2)
        label.set_text("SYN")
        label.set_color("deepskyblue")

    elif i == 1:  # SYN-ACK
        arrow = ax.arrow(7, server_y, -5, 2, head_width=0.2, color="orange", linewidth=2)
        label.set_text("SYN-ACK")
        label.set_color("orange")

    elif i == 2:  # ACK
        arrow = ax.arrow(2, client_y, 5, -2, head_width=0.2, color="limegreen", linewidth=2)
        label.set_text("ACK")
        label.set_color("limegreen")

    elif i == 3:
        label.set_text("Connection Established ✅")
        label.set_color("green")

ani = animation.FuncAnimation(fig, animate, frames=4, interval=1500, repeat=False)

fig.patch.set_facecolor("#0f172a")  # Dark background
plt.show()
