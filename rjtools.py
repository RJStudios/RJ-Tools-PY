import os
import random
import string
import pyttsx3
import tkinter as tk
from tkinter import filedialog
import shutil
import os
import sys
from threading import Thread
import time
import socket
import cpuinfo
import psutil
import platform
import subprocess
from PIL import ImageGrab
import math
import re

def clear_screen():
    # Clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

def password_generator():
    try:
        length = int(input("Enter the desired password length: "))
        if length < 1:
            print("Invalid length! Please enter a positive number.")
            return
    except ValueError:
        print("Please enter a valid number for length.")
        return
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return f"Generated Password: {password}"

def text_to_speech(text):
    if not text.strip():
        return "You entered an empty string. Please provide text."
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    return "Text-to-speech complete."

def digital_clock():
    def update_time():
        current_time = time.strftime('%H:%M:%S')
        current_date = time.strftime('%A, %B %d, %Y')
        time_label.config(text=current_time)
        date_label.config(text=current_date)
        root.after(1000, update_time)

    def close_clock():
        root.destroy()

    root = tk.Tk()
    root.title("Digital Clock")
    root.geometry("400x200")
    time_label = tk.Label(root, font=('calibri', 50, 'bold'), background='black', foreground='white')
    time_label.pack(anchor='center')
    date_label = tk.Label(root, font=('calibri', 20), background='black', foreground='white')
    date_label.pack(anchor='center')
    close_button = tk.Button(root, text="Close Clock", command=close_clock, bg='black', fg='white')
    close_button.pack()
    root.attributes("-topmost", True)
    root.configure(bg='black')
    update_time()
    root.mainloop()

def file_mover():
    print("\n--- File Mover ---")
    print("1. Move a file")
    print("2. Move all files from a folder")
    choice = input("Choose an option (1 or 2): ").strip()
    if choice == '1':
        src_file = filedialog.askopenfilename(title="Select a File to Move")
        if not src_file:
            return "No file selected."
        dest_dir = filedialog.askdirectory(title="Select Destination Folder")
        if not dest_dir:
            return "No destination folder selected."
        try:
            shutil.move(src_file, dest_dir)
            return f"File '{os.path.basename(src_file)}' moved to {dest_dir}"
        except Exception as e:
            return f"Error: {e}"
    elif choice == '2':
        src_folder = filedialog.askdirectory(title="Select Source Folder")
        if not src_folder:
            return "No source folder selected."
        dest_dir = filedialog.askdirectory(title="Select Destination Folder")
        if not dest_dir:
            return "No destination folder selected."
        file_type = input("Enter the file extension to move (e.g., .txt, .jpg), or leave blank to move all files: ").strip()
        moved_files = 0
        for file_name in os.listdir(src_folder):
            if file_name.endswith(file_type) or not file_type:
                full_file_name = os.path.join(src_folder, file_name)
                if os.path.isfile(full_file_name):
                    try:
                        shutil.move(full_file_name, dest_dir)
                        moved_files += 1
                    except Exception as e:
                        return f"Error moving {file_name}: {e}"
        return f"Moved {moved_files} file(s) to {dest_dir}"
    else:
        return "Invalid choice. Please choose 1 or 2."

def folder_size_checker():
    folder_path = filedialog.askdirectory(title="Select Folder to Calculate Size")
    if not folder_path:
        return "No folder selected."
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    size_in_mb = total_size / (1024 * 1024)
    return f"Total size of '{folder_path}': {size_in_mb:.2f} MB"

def countdown_timer():
    try:
        seconds = int(input("Enter countdown time in seconds: "))
        if seconds < 0:
            return "Invalid time! Please enter a positive number."
    except ValueError:
        return "Please enter a valid number for time."
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f'{mins:02}:{secs:02}'
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    return "Countdown complete!"

def really_janky_calculator(expression):
    expression = expression.replace("^", "**")
    
    def replace_sqrt(match):
        return f"math.sqrt({match.group(1)})"
    
    expression = re.sub(r'sqrt\(([^)]+)\)', replace_sqrt, expression)
    
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {e}"

def screenshot_capture():
    screenshot = ImageGrab.grab()
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if save_path:
        screenshot.save(save_path)
        return f"Screenshot saved to {save_path}"
    else:
        return "Screenshot not saved."

def system_info_viewer():
    os_name = platform.system()
    os_version = platform.version()
    cpu = cpuinfo.get_cpu_info()['brand_raw']
    cpu_cores = psutil.cpu_count(logical=True)
    total_memory = psutil.virtual_memory().total / (1024 ** 3)
    used_memory = psutil.virtual_memory().used / (1024 ** 3)
    free_memory = psutil.virtual_memory().free / (1024 ** 3)

    disk_usage = psutil.disk_usage('/')
    total_disk = disk_usage.total / (1024 ** 3)
    used_disk = disk_usage.used / (1024 ** 3)
    free_disk = disk_usage.free / (1024 ** 3)

    try:
        gpu_info = subprocess.check_output(["wmic", "path", "win32_videocontroller", "get", "name"]).decode().split("\n")[1:-1]
    except Exception as e:
        gpu_info = [f"Error retrieving GPU info: {e}"]

    ascii_art = r"""
⠀⠀⠀⣤⣴⣾⣿⣿⣿⣿⣿⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡄
⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⢰⣦⣄⣀⣀⣠⣴⣾⣿⠃
⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⠀⣼⣿⡿⠿⠛⠻⠿⣿⣿⡇⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀
⠀⠀⠉⠀⠀⠀⢀⠀⠀⠀⠈⠁⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀
⠀⠀⣠⣴⣶⣿⣿⣿⣷⣶⣤⠀⠀⠀⠈⠉⠛⠛⠛⠉⠉⠀⠀⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⣶⣦⣄⣀⣀⣤⣤⣶⠀⠀
⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀
⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
⢠⣿⡿⠿⠛⠉⠉⠉⠛⠿⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀
⠘⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⢿⣿⣿⣿⣿⣿⠿⠛⠀⠀
    """

    print(ascii_art)
    print(f"OS: {os_name} {os_version}")
    print(f"CPU: {cpu} ({cpu_cores} cores)")
    print(f"Total Memory: {total_memory:.2f} GB")
    print(f"Used Memory: {used_memory:.2f} GB")
    print(f"Free Memory: {free_memory:.2f} GB")
    print(f"Total Disk Space: {total_disk:.2f} GB")
    print(f"Used Disk Space: {used_disk:.2f} GB")
    print(f"Free Disk Space: {free_disk:.2f} GB")

    print("\nGPU Information:")
    for gpu in gpu_info:
        if gpu.strip():
            print(f"  {gpu.strip()}")

def help_center():
    help_text = """
    Commands:
    1 - Password Generator: Generates a customizable password with letters, numbers, and symbols.
    2 - Text to Speech: Type words and have the computer speak them out loud.
    3 - Digital Clock: A clock that displays time and date, always stays on top.
    4 - File Mover: Select source and destination folders to move files, or select individual files.
    5 - Folder Size Checker: Calculate the total size of a folder.
    6 - Countdown Timer: Set a timer that counts down and alerts you when it's done.
    7 - Complex Calculator: Perform complex arithmetic operations and functions ( e.g. 1+2^(3+1)-sqrt(9) ).
    8 - Screenshot Capture: Take a screenshot and save it as an image file.
    9 - System Info Viewer: View system information like OS, CPU, memory, etc.
    10 - Help Center: Display this help text.
    kill, /kill: Exits PY-Tools with confirmation.
    """
    return help_text

def main_menu():
    while True:
        clear_screen()
        print("\n--- PY-Tools Main Menu ---")
        print("1. Password Generator")
        print("2. Text to Speech")
        print("3. Digital Clock")
        print("4. File Mover")
        print("5. Folder Size Checker")
        print("6. Countdown Timer")
        print("7. Complex Calculator")
        print("8. Screenshot Capture")
        print("9. System Info Viewer")
        print("10. Help Center")
        print("Type 'kill' or '/kill' to exit.")
        print("-----------------------------")
        choice = input("Select an option (1-10 or 'kill'): ").strip().lower()
        clear_screen()
        
        if choice == '1':
            result = password_generator()
        elif choice == '2':
            text = input("Enter text for Text to Speech: ")
            result = text_to_speech(text)
        elif choice == '3':
            Thread(target=digital_clock).start()
            result = "Digital clock is running. Close it from its window."
        elif choice == '4':
            result = file_mover()
        elif choice == '5':
            result = folder_size_checker()
        elif choice == '6':
            result = countdown_timer()
        elif choice == '7':
            expression = input("Enter a complex calculation ( e.g. 1+2^(3+1)-sqrt(9) ): ")
            result = really_janky_calculator(expression)
        elif choice == '8':
            result = screenshot_capture()
        elif choice == '9':
            result = system_info_viewer()
        elif choice == '10':
            result = help_center()
        elif choice in ['kill', '/kill']:
            print("Exiting PY-Tools...")
            break
        else:
            result = "Invalid option. Please try again."

        if result:
            print(result)
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main_menu()
