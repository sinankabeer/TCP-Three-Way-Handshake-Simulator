import matplotlib.pyplot as plt
import matplotlib.animation as animation
from colorama import Fore, Style
import time

# -------------------------------------------------
# Choose scenario
# -------------------------------------------------
print(Fore.CYAN + "\n--- TCP 3-Way Handshake with Retry Demonstration ---" + Style.RESET_ALL)
print("Choose a scenario:")
print("1️⃣ Normal handshake (successful)")
print("2️⃣ SYN-ACK lost (server reply fails, retry after timeout)")
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
print(Fore.YELLOW + "\n[CLIENT] Sending SYN to Server..." + Style.RESET_ALL)
time.sleep(1)

if scenario == "synack_lost":
    print(Fore.RED + "[SERVER] ❌ SYN-ACK lost! No response to client..." + Style.RESET_ALL)
    print(Fore.YELLOW + "[CLIENT] Timeout reached. Retrying in..." + Style.RESET_ALL)
    for sec in range(3, 0, -1):
        print(Fore.LIGHTBLACK_EX + f"   {sec}..." + Style.RESET_ALL)
        time.sleep(1)
    print(Fore.YELLOW + "[CLIENT] Retrying SYN..." + Style.RESET_ALL)
    time.sleep(1)
    print(Fore.CYAN + "[SERVER] Received SYN (retry), sending SYN-ACK..." + Style.RESET_ALL)
    time.sleep(1)
    print(Fore.GREEN + "[CLIENT] Received SYN-ACK, sending ACK ✅" + Style.RESET_ALL)
    print(Fore.GREEN + "Connection established successfully after retry!\n" + Style.RESET_ALL)

elif scenario == "ack_lost":
    print(Fore.CYAN + "[SERVER] Received SYN, sending SYN-ACK..." + Style.RESET_ALL)
    time.sleep(1)
    print(Fore.CYAN + "[CLIENT] Received SYN-ACK, sending ACK..." + Style.RESET_ALL)
    time.sleep(1)
    print(Fore.RED + "[ACK] ❌ Lost! Connection not fully established" + Style.RESET_ALL)

else:
    print(Fore.CYAN + "[SERVER] Received SYN, sending SYN-ACK..." + Style.RESET_ALL)
    time.sleep(1)
    print(Fore.GREEN + "[CLIENT] Received SYN-ACK, sending ACK ✅" + Style.RESET_ALL)
    print(Fore.GREEN + "Connection established successfully!" + Style.RESET_ALL)

# -------------------------------------------------
# Visualization
# -------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

# Hosts
ax.text(1, 5, "Client\n192.168.1.2", fontsize=12, fontweight='bold', color="#007acc", ha='center')
ax.text(8.5, 5, "Server\n192.168.1.10", fontsize=12, fontweight='bold', color="#d9534f", ha='center')
ax.plot([1.5, 8], [4.8, 4.8], '--', color='gray', alpha=0.4)

# Animation elements
arrow_syn, = ax.plot([], [], color='blue', lw=2)
arrow_syn_retry, = ax.plot([], [], color='purple', lw=2)
arrow_synack, = ax.plot([], [], color='orange', lw=2)
arrow_ack, = ax.plot([], [], color='green', lw=2)
cross_marker, = ax.plot([], [], 'rx', markersize=14, mew=3)

status_text = ax.text(2, 1, "", fontsize=12, color="black")
packet_info = ax.text(2, 0.5, "", fontsize=10, color="gray")

# -------------------------------------------------
# Animation logic
# -------------------------------------------------
def animate(i):
    cross_marker.set_data([], [])
    status_text.set_text("")
    packet_info.set_text("")

    # Step 1: SYN
    if i < 20:
        x_vals = [1.5, 1.5 + i * 0.33]
        y_vals = [4.2, 4.2]
        arrow_syn.set_data(x_vals, y_vals)
        status_text.set_text("SYN →")
        packet_info.set_text("SEQ=1000, ACK=0")

    # Step 2: SYN-ACK (may be lost)
    elif i < 40:
        if scenario == "synack_lost":
            # Make it blink red
            if i % 6 < 3:
                cross_marker.set_data([5], [3.8])
                status_text.set_text("❌ SYN-ACK Lost")
                packet_info.set_text("Client waiting... Timeout triggered")
        else:
            x_vals = [8, 8 - (i - 20) * 0.33]
            y_vals = [3.5, 3.5]
            arrow_synack.set_data(x_vals, y_vals)
            status_text.set_text("SYN-ACK →")
            packet_info.set_text("SEQ=5000, ACK=1001")

    # Step 3: Retry SYN (if lost)
    elif scenario == "synack_lost" and 40 <= i < 60:
        x_vals = [1.5, 1.5 + (i - 40) * 0.33]
        y_vals = [3.0, 3.0]
        arrow_syn_retry.set_data(x_vals, y_vals)
        status_text.set_text("🔁 RETRY: SYN →")
        packet_info.set_text("Client retries SYN after timeout")

    # Step 4: Retry success
    elif scenario == "synack_lost" and 60 <= i < 80:
        x_vals = [8, 8 - (i - 60) * 0.33]
        y_vals = [2.5, 2.5]
        arrow_synack.set_data(x_vals, y_vals)
        status_text.set_text("SYN-ACK → (Retry)")
        packet_info.set_text("Server responds to retry")

    # Step 5: ACK (success or lost)
    elif i >= 80:
        x_vals = [1.5, 1.5 + (i - 80) * 0.33]
        y_vals = [2.0, 2.0]
        arrow_ack.set_data(x_vals, y_vals)
        if scenario == "ack_lost":
            # Blink red cross when ACK is lost
            if i % 6 < 3:
                cross_marker.set_data([5], [2.0])
                status_text.set_text("❌ ACK Lost")
                packet_info.set_text("Connection failed (ACK not received)")
        else:
            status_text.set_text("ACK →")
            packet_info.set_text("Connection Established ✅")

    return arrow_syn, arrow_syn_retry, arrow_synack, arrow_ack, status_text, packet_info, cross_marker

# -------------------------------------------------
# Run Animation
# -------------------------------------------------
ani = animation.FuncAnimation(fig, animate, frames=120, interval=100, blit=False, repeat=False)
plt.title("TCP Handshake Simulation - " + scenario.replace("_", " ").title(), fontsize=14, fontweight='bold')
plt.show()
