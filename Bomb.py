import time
import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def dramatic_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def user_confirmation():
    clear_screen()
    print("\033[1;33m")  # Yellow text
    print("⚠️  WARNING")
    print("This file may perform dangerous actions.")
    print("Are you sure you want to run this file?")
    choice = input("(yes/no): ").strip().lower()
    print("\033[0m")  # Reset color

    if choice != "yes":
        print("Aborting execution. Stay safe! 😌")
        sys.exit()

def warning_screen():
    clear_screen()
    print("\033[1;31m")  # Red text
    dramatic_print("⚠️  WARNING: Unauthorized access detected!", 0.07)
    time.sleep(1.5)
    dramatic_print("Security protocol XYZ-42 engaged.", 0.07)
    time.sleep(1)
    dramatic_print("Initializing self-destruct sequence...", 0.07)
    time.sleep(2)
    print("\033[0m")  # Reset color

def countdown():
    for i in range(10, 0, -1):
        print(f"💣 Detonation in: {i} seconds")
        time.sleep(1)
    print("💥 Self-destruct sequence complete.")

def final_message():
    time.sleep(1)
    clear_screen()
    print("\033[1;32m")  # Green text
    dramatic_print("🎉 Just kidding!", 0.1)
    time.sleep(1)
    dramatic_print("Your system is totally fine 😄", 0.1)
    dramatic_print("Remember: Always lock your screen! 🔐", 0.1)
    print("\033[0m")  # Reset color

def self_destruct_prank():
    user_confirmation()
    warning_screen()
    countdown()
    final_message()

# Run the prank
if __name__ == "__main__":
    self_destruct_prank()
