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
from PIL import Image, ImageDraw, ImageFont, ImageGrab
import math
import re
import qrcode
import base64
import calendar
import requests
import speedtest
import cv2
from cryptography.fernet import Fernet
from wordcloud import WordCloud
from textblob import TextBlob
import pyfiglet
import pygame
import pyperclip
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import datasets
import datetime
from pyzbar.pyzbar import decode
import hashlib
import zipfile

def clear_screen():
    # Clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

def get_user_input(prompt, input_type=str):
    """Get user input with type checking."""
    while True:
        try:
            return input_type(input(prompt))
        except ValueError:
            print(f"Invalid input. Please enter a {input_type.__name__}.")

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
    # Replace ^ with ** for exponentiation
    expression = expression.replace("^", "**")

    # Define a function to replace sqrt
    def replace_sqrt(match):
        return f"math.sqrt({match.group(1)})"

    # Replace sqrt function calls
    expression = re.sub(r'sqrt\(([^)]+)\)', replace_sqrt, expression)

    # Define a function to replace factorial (e.g., n!)
    def replace_factorial(match):
        return f"math.factorial({match.group(1)})"

    # Replace factorial (e.g., 5!)
    expression = re.sub(r'(\d+)!', replace_factorial, expression)

    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {e}"

# Example usage:
expression = "5! + sqrt(16) + 2^3"
print(really_janky_calculator(expression))

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

def qr_code_generator():
    # Input the URL or text in the terminal
    qr_data = input("Enter the text or URL for the QR code: ").strip()

    if not qr_data:
        return "No input provided."

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill='black', back_color='white')

    # Use tkinter to select the save location
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])

    if save_path:
        img.save(save_path)
        return f"QR code saved to {save_path}"
    else:
        return "QR code not saved."
    
def qr_code_reader():
    """Read and decode a QR code from an image."""
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if not file_path:
        return "No file selected."
    image = cv2.imread(file_path)
    decoded_objects = decode(image)
    if decoded_objects:
        return f"Decoded data: {decoded_objects[0].data.decode('utf-8')}"
    else:
        return "No QR code found in the image."

def base64_encode_decode():
    # Ask the user if they want to encode or decode
    action = input("Type 'encode' to encode or 'decode' to decode: ").strip().lower()

    if action == 'encode':
        # Base64 Encode
        text_to_encode = input("Enter the text you want to encode in Base64: ").strip()
        if not text_to_encode:
            return "No text provided."
        encoded_bytes = base64.b64encode(text_to_encode.encode('utf-8'))
        encoded_str = encoded_bytes.decode('utf-8')
        return f"Encoded Base64: {encoded_str}"

    elif action == 'decode':
        # Base64 Decode
        text_to_decode = input("Enter the Base64 string you want to decode: ").strip()
        if not text_to_decode:
            return "No Base64 string provided."
        try:
            decoded_bytes = base64.b64decode(text_to_decode)
            decoded_str = decoded_bytes.decode('utf-8')
            return f"Decoded Text: {decoded_str}"
        except Exception as e:
            return f"Error decoding Base64: {e}"

    else:
        return "Invalid option. Please type 'encode' to encode or 'decode' to decode."
    
def file_reader():
    # Open a file dialog to select the file
    file_path = filedialog.askopenfilename(
        title="Select a file to read",
        filetypes=[("Text, Code, and Binary Files", "*.txt *.bat *.doc *.py *.css *.html *.xml *.js *.json *.md *.csv *.png *.jpg *.jpeg *.bmp *.gif *.pdf"),
                ("All files", "*.*")]
    )

    if not file_path:
        return "No file selected."

    try:
        # Check if the file is a binary file by reading it in binary mode
        with open(file_path, 'rb') as file:
            content = file.read()

        # Convert the binary content to a string that can be displayed
        content_as_text = content.decode('latin1')  # Use 'latin1' to handle raw binary content
        return f"Contents of {file_path} (opened as text):\n\n{content_as_text}"
    except Exception as e:
        return f"Error reading file: {e}"
    
def date_time_calculator():
    """Perform date and time calculations."""
    date1 = input("Enter first date (YYYY-MM-DD): ")
    date2 = input("Enter second date (YYYY-MM-DD): ")
    date1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
    date2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
    difference = abs((date2 - date1).days)
    return f"The difference between the two dates is {difference} days."

def wikipedia_search():
    """Search Wikipedia and display a summary."""
    query = input("Enter search query: ")
    try:
        response = requests.get(f"https://en.wikipedia.org/api/rest_v1/page/summary/{query}")
        data = response.json()
        return data['extract']
    except:
        return "Error fetching Wikipedia content."

def file_finder():
    """Find files in a directory based on a search term."""
    directory = filedialog.askdirectory(title="Select directory to search")
    if not directory:
        return "No directory selected."
    search_term = input("Enter search term: ")
    found_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if search_term.lower() in file.lower():
                found_files.append(os.path.join(root, file))
    return "\n".join(found_files) if found_files else "No files found."

def password_strength_checker():
    """Check the strength of a password."""
    password = input("Enter password to check: ")
    strength = 0
    if len(password) >= 8:
        strength += 1
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"\d", password):
        strength += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    strength_levels = ['Very Weak', 'Weak', 'Moderate', 'Strong', 'Very Strong']
    return f"Password strength: {strength_levels[strength]}"

def memory_usage_monitor():
    """Monitor and display system memory usage."""
    memory = psutil.virtual_memory()
    return f"""
    Total: {memory.total / (1024 ** 3):.2f} GB
    Available: {memory.available / (1024 ** 3):.2f} GB
    Used: {memory.used / (1024 ** 3):.2f} GB
    Percentage: {memory.percent}%
    """

def ip_address_lookup():
    """Look up information about an IP address."""
    ip = input("Enter IP address: ")
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        return f"""
        IP: {data['query']}
        Country: {data['country']}
        City: {data['city']}
        ISP: {data['isp']}
        """
    except:
        return "Error fetching IP information."

def internet_speed_test():
    """Perform an internet speed test using Cloudflare's 50MB file."""
    print("Testing internet speed...")
    try:
        # Cloudflare speed test file (50MB)
        url = "https://speed.cloudflare.com/__down?bytes=50000000"
        
        start_time = time.time()
        response = requests.get(url, stream=True)
        size = 0
        for chunk in response.iter_content(1024):
            size += len(chunk)
        end_time = time.time()
        
        duration = end_time - start_time
        size_mb = size / 1_000_000  # Size in MB
        speed_mbps = (size_mb * 8) / duration  # Convert to Mbps
        
        return f"Estimated download speed: {speed_mbps:.2f} Mbps"
    except Exception as e:
        return f"Error performing speed test: {str(e)}"
    
def morse_code_converter():
    """Convert text to Morse code and vice versa."""
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.'
    }
    reverse_dict = {v: k for k, v in morse_code_dict.items()}
    
    choice = input("Enter 't' for text to Morse, 'm' for Morse to text: ")
    if choice.lower() == 't':
        text = input("Enter text to convert to Morse code: ").upper()
        morse = ' '.join(morse_code_dict.get(char, char) for char in text)
        return f"Morse code: {morse}"
    elif choice.lower() == 'm':
        morse = input("Enter Morse code to convert to text: ")
        text = ''.join(reverse_dict.get(code, code) for code in morse.split())
        return f"Decoded text: {text}"
    else:
        return "Invalid choice."

def binary_converter():
    """Convert between decimal and binary numbers."""
    choice = input("Enter 'd' for decimal to binary, 'b' for binary to decimal: ")
    if choice.lower() == 'd':
        decimal = int(input("Enter decimal number: "))
        binary = bin(decimal)[2:]
        return f"Binary: {binary}"
    elif choice.lower() == 'b':
        binary = input("Enter binary number: ")
        decimal = int(binary, 2)
        return f"Decimal: {decimal}"
    else:
        return "Invalid choice."

def url_shortener():
    """Shorten a long URL using a URL shortening service."""
    long_url = input("Enter the long URL to shorten: ")
    try:
        response = requests.post("https://tinyurl.com/api-create.php", data={"url": long_url})
        if response.status_code == 200:
            return f"Shortened URL: {response.text}"
        else:
            return "Error shortening URL."
    except:
        return "Error connecting to URL shortening service."

def ascii_art_generator():
    """Generate ASCII art from text."""
    text = input("Enter text for ASCII art: ")
    font = pyfiglet.figlet_format(text)
    return font

def hash_generator():
    """Generate hash values for a given text."""
    text = input("Enter text to hash: ")
    algorithms = ['md5', 'sha1', 'sha256', 'sha512']
    results = {}
    for algo in algorithms:
        hash_object = hashlib.new(algo)
        hash_object.update(text.encode())
        results[algo] = hash_object.hexdigest()
    return "\n".join(f"{algo.upper()}: {hash_value}" for algo, hash_value in results.items())

def zip_extractor():
    """Extract contents of a ZIP file."""
    zip_path = filedialog.askopenfilename(title="Select ZIP file", filetypes=[("ZIP files", "*.zip")])
    if not zip_path:
        return "No ZIP file selected."
    extract_path = filedialog.askdirectory(title="Select extraction directory")
    if not extract_path:
        return "No extraction directory selected."
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    return f"Extracted contents to {extract_path}"

def music_player():
    """Play an audio file."""
    pygame.mixer.init()
    music_file = filedialog.askopenfilename(title="Select music file", filetypes=[("Audio files", "*.mp3;*.wav")])
    if not music_file:
        return "No music file selected."
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()
    input("Press Enter to stop playback...")
    pygame.mixer.music.stop()
    return "Music playback ended."

def random_name_generator():
    """Generate a random name."""
    first_names = ['John', 'Jane', 'Mike', 'Emily', 'David', 'Sarah', 'Chris', 'Laura', 'Pablo', 'Mihcael', 'Jenny']
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Bold', 'Green', 'Herring']
    return f"Random Name: {random.choice(first_names)} {random.choice(last_names)}"

def dice_roller():
    """Simulate rolling dice."""
    sides = get_user_input("Enter the number of sides for the dice: ", int)
    rolls = get_user_input("Enter the number of rolls: ", int)
    results = [random.randint(1, sides) for _ in range(rolls)]
    return f"Dice rolls: {results}\nSum: {sum(results)}\nAverage: {sum(results)/rolls:.2f}"

def calendar_viewer():
    """Display a calendar for a given year and month."""
    year = get_user_input("Enter year: ", int)
    month = get_user_input("Enter month (1-12): ", int)
    cal = calendar.month(year, month)
    return cal

def math_quiz():
    """Generate and run a simple math quiz."""
    score = 0
    questions = 5
    for _ in range(questions):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(['+', '-', '*'])
        question = f"{num1} {operator} {num2}"
        correct_answer = eval(question)
        user_answer = get_user_input(f"What is {question}? ", float)
        if user_answer == correct_answer:
            score += 1
            print("Correct!")
        else:
            print(f"Wrong. The correct answer is {correct_answer}")
    return f"You scored {score} out of {questions}"

def roman_numeral_converter():
    """Convert decimal numbers to Roman numerals."""
    def to_roman(num):
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        result = ""
        for i, value in enumerate(values):
            while num >= value:
                result += symbols[i]
                num -= value
        return result

    number = get_user_input("Enter a number to convert to Roman numeral: ", int)
    return f"Roman numeral: {to_roman(number)}"

def text_reverser():
    """Reverse the characters in a given text."""
    text = input("Enter text to reverse: ")
    reversed_text = text[::-1]
    return f"Reversed text: {reversed_text}"

def bmi_calculator():
    """Calculate Body Mass Index (BMI)."""
    weight = get_user_input("Enter your weight in kg: ", float)
    height = get_user_input("Enter your height in meters: ", float)
    bmi = weight / (height ** 2)
    category = "Underweight" if bmi < 18.5 else "Normal weight" if bmi < 25 else "Overweight" if bmi < 30 else "Obese"
    return f"Your BMI is {bmi:.2f} ({category})"

def text_case_converter():
    """Convert text to different cases."""
    text = input("Enter text to convert: ")
    print("1. UPPERCASE")
    print("2. lowercase")
    print("3. Title Case")
    print("4. aLtErNaTiNg CaSe")
    choice = input("Choose conversion type (1-4): ")
    if choice == '1':
        return text.upper()
    elif choice == '2':
        return text.lower()
    elif choice == '3':
        return text.title()
    elif choice == '4':
        return ''.join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(text))
    else:
        return "Invalid choice."

def clipboard_manager():
    """Manage clipboard content."""
    text = pyperclip.paste()
    print("Current clipboard content:")
    print(text)
    choice = input("Enter '1' to copy new text to clipboard, '2' to clear clipboard: ")
    if choice == '1':
        new_text = input("Enter text to copy to clipboard: ")
        pyperclip.copy(new_text)
        return "Text copied to clipboard."
    elif choice == '2':
        pyperclip.copy('')
        return "Clipboard cleared."
    else:
        return "Invalid choice."

def todo_list():
    """Simple TODO list manager."""
    todos = []
    while True:
        print("\n1. Add task\n2. View tasks\n3. Mark task as done\n4. Exit")
        choice = get_user_input("Enter your choice: ", int)
        if choice == 1:
            task = input("Enter task: ")
            todos.append({"task": task, "done": False})
        elif choice == 2:
            for i, todo in enumerate(todos, 1):
                status = "✓" if todo["done"] else " "
                print(f"{i}. [{status}] {todo['task']}")
        elif choice == 3:
            index = get_user_input("Enter task number to mark as done: ", int) - 1
            if 0 <= index < len(todos):
                todos[index]["done"] = True
            else:
                print("Invalid task number.")
        elif choice == 4:
            break
        else:
            print("Invalid choice.")
    return "TODO list manager closed."

def fibonacci_generator():
    """Generate Fibonacci sequence."""
    n = get_user_input("Enter the number of Fibonacci terms to generate: ", int)
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return f"Fibonacci sequence: {sequence}"

def rock_paper_scissors():
    """Play Rock Paper Scissors against the computer."""
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    if user_choice not in choices:
        return "Invalid choice. Please try again."
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "paper" and computer_choice == "rock") or \
        (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def hangman_game():
    """Play a game of Hangman."""
    words = ["python", "programming", "computer", "algorithm", "database"]
    word = random.choice(words)
    word_letters = set(word)
    alphabet = set(string.ascii_lowercase)
    used_letters = set()
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print("You have", lives, "lives left and you have used these letters: ", " ".join(used_letters))
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").lower()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print("Letter is not in the word.")
        elif user_letter in used_letters:
            print("You have already used that letter. Please try again.")
        else:
            print("Invalid character. Please try again.")

    if lives == 0:
        return f"Sorry, you died. The word was {word}"
    else:
        return f"Congratulations! You guessed the word {word}!"

def tic_tac_toe():
    """Play a game of Tic Tac Toe."""
    board = [" " for _ in range(9)]
    current_player = "X"

    def print_board():
        for i in range(0, 9, 3):
            print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
            if i < 6:
                print("---------")

    def is_winner(player):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]
        return any(all(board[i] == player for i in condition) for condition in win_conditions)

    def is_board_full():
        return " " not in board

    while True:
        print_board()
        move = get_user_input(f"Player {current_player}, enter your move (1-9): ", int) - 1

        if move < 0 or move > 8 or board[move] != " ":
            print("Invalid move. Try again.")
            continue

        board[move] = current_player

        if is_winner(current_player):
            print_board()
            return f"Player {current_player} wins!"

        if is_board_full():
            print_board()
            return "It's a tie!"

        current_player = "O" if current_player == "X" else "X"

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
    10 - QR Code Generator: Generates a nice QR Code for you
    11 - QR Code Reader: give qr code image and it tells you what it contains
    12 - Base 64 Encoder / Decoder: Encodes and Decodes text to base64
    13 - File Reader: Reads anything from .txt and .py to even binary such as .png and .pdf
    help - Help Center: This shows help description for every program
    kill, /kill: Exits PY-Tools with confirmation.
    """
    return help_text

def print_rj_tools_ascii():
    ascii_art = """
 $$$$$$\     $$$$$\       $$$$$$$$\                  $$\           
$$  __$$\    \__$$ |      \__$$  __|                 $$ |          
$$ |  $$ |      $$ |         $$ | $$$$$$\   $$$$$$\  $$ | $$$$$$$\ 
$$$$$$$  |      $$ |         $$ |$$  __$$\ $$  __$$\ $$ |$$  _____|
$$  __$$< $$\   $$ |         $$ |$$ /  $$ |$$ /  $$ |$$ |\$$$$$$\  
$$ |  $$ |$$ |  $$ |         $$ |$$ |  $$ |$$ |  $$ |$$ | \____$$\ 
$$ |  $$ |\$$$$$$  |         $$ |\$$$$$$  |\$$$$$$  |$$ |$$$$$$$  |
\__|  \__| \______/          \__| \______/  \______/ \__|\_______/
    """
    print(ascii_art)

def main_menu():
    result = print_rj_tools_ascii()
    menu_items = [
        ("1. Password Generator", "2. Text To Speech", "3. Digital Clock"),
        ("4. File Mover", "5. Folder Size Checker", "6. Countdown Timer"),
        ("7. Really Janky Calculator", "8. Screenshot Capture", "9. System Info Viewer"),
        ("10. QR Code Generator", "11. QR Code Reader", "12. Base64 Encode Decode"),
        ("13. File Reader", "14. Date Time Calculator", "15. Wikipedia Search"),
        ("16. File Finder", "17. Password Strength Checker", "18. Memory Usage Monitor"),
        ("19. IP Address Lookup", "20. Internet Speed Test", "21. Morse Code Converter"),
        ("22. Binary Converter", "23. URL Shortener", "24. ASCII Art Generator"),
        ("25. Hash Generator", "26. Zip Extractor", "27. Music Player"),
        ("28. Random Name Generator", "29. Dice Roller", "30. Calendar Viewer"),
        ("31. Math Quiz", "32. Roman Numeral Converter", "33. Text Reverser"),
        ("34. BMI Calculator", "35. Text Case Converter", "36. Clipboard Manager"),
        ("37. Todo List", "38. Fibonacci Generator", "39. Rock Paper Scissors"),
        ("40. Hangman Game", "41. Tic Tac Toe",),
        (""),
        ("help - Help Center", "kill or /kill to exit"),
    ]
    col_width = max(len(item) for row in menu_items for item in row) + 2
    
    print("\n" + "=" * (col_width * 3))
    print("RJ Tools Menu".center(col_width * 3))
    print("=" * (col_width * 3))
    
    for row in menu_items:
        print("".join(f"{item:<{col_width}}" for item in row))
    
    print("=" * (col_width * 3))

    choice = input("Select an option: ").strip().lower()
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
        expression = input("Enter a complex calculation ( e.g. 1+2^(3+1)-sqrt(9), 5!): ")
        result = really_janky_calculator(expression)
    elif choice == '8':
        result = screenshot_capture()
    elif choice == '9':
        result = system_info_viewer()
    elif choice == '10':
        result = qr_code_generator()
    elif choice == '11':
        result = qr_code_reader()
    elif choice == '12':
        result = base64_encode_decode()
    elif choice == '13':
        result = file_reader()
    elif choice == '14':
        result = date_time_calculator()
    elif choice == '15':
        result = wikipedia_search()
    elif choice == '16':
        result = file_finder()
    elif choice == '17':
        result = password_strength_checker()
    elif choice == '18':
        result = memory_usage_monitor()
    elif choice == '19':
        result = ip_address_lookup()
    elif choice == '20':
        result = internet_speed_test()
    elif choice == '21':
        result = morse_code_converter()
    elif choice == '22':
        result = binary_converter()
    elif choice == '23':
        result = url_shortener()
    elif choice == '24':
        result = ascii_art_generator()
    elif choice == '25':
        result = hash_generator()
    elif choice == '26':
        result = zip_extractor()
    elif choice == '27':
        result = music_player()
    elif choice == '28':
        result = random_name_generator()
    elif choice == '29':
        result = dice_roller()
    elif choice == '30':
        result = calendar_viewer()
    elif choice == '31':
        result = math_quiz()
    elif choice == '32':
        result = roman_numeral_converter()
    elif choice == '33':
        result = text_reverser()
    elif choice == '34':
        result = bmi_calculator()
    elif choice == '35':
        result = text_case_converter()
    elif choice == '36':
        result = clipboard_manager()
    elif choice == '37':
        result = todo_list()
    elif choice == '38':
        result = fibonacci_generator()
    elif choice == '39':
        result = rock_paper_scissors()
    elif choice == '40':
        result = hangman_game()
    elif choice == '41':
        result = tic_tac_toe()
    elif choice == 'help':
        result = help_center()
    elif choice in ['kill', '/kill']:
        quit()
    else:
        result = "Invalid option. Please try again."

    if result:
        print(result)
    input("\nPress Enter to continue...")

if __name__ == "__main__":
    main_menu()
