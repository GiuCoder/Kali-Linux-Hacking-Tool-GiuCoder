#!/usr/bin/env python3
import argparse
import subprocess
import platform
import time
import art
import sys
import os

from termcolor import colored

from tkinter import messagebox


def check_module(module):
    try:
        __import__(module)
    except ImportError:
        messagebox.showwarning(
            "Warning", f"{module} module is not installed, installing it now...")
        subprocess.check_call(["python", "-m", "pip", "install", module])
        messagebox.showinfo("Info", f"{module} module has been installed!")


check_module("argparse")
check_module("subprocess")
check_module("platform")
check_module("time")

check_module("art")
check_module("termcolor")


def clear_term():
    platform1 = platform.system()

    if platform1 in ["Darwin", "Linux"]:
        subprocess.run("clear", shell=True)
    elif platform1 == "Windows":
        subprocess.run("cls", shell=True)


clear_term()


def text_art(text):
    print(colored(art.text2art(text), "green"))


def secure():

    clear_term()
    text_art("Secure Linux\nBy GiuCoder")

    subprocess.run(
        "git clone https://github.com/GiuCoder/SecureTheLinux.git", shell=True)
    clear_term()
    subprocess.run(
        "cd SecureTheLinux && chmod +x securethelinux.sh && ./securethelinux.sh", shell=True)

    text_art("Secure Linux\nBy GiuCoder")

    os.chdir("SecureTheLinux")


def hide():
    clear_term()
    text_art("HideYourSelf\nBy GiuCoder")
    commands = [
        "if [ -d 'HideYourSelf' ]; then rm -rf HideYourSelf; fi",
        "git clone https://github.com/GiuCoder/HideYourSelf.git",
        "clear",
        "chmod +x HideYourSelf/hidemyip.sh",
        "sudo mv HideYourSelf/hidemyip.sh /usr/bin/",
        "hidemyip.sh"
    ]
    for command in commands:
        try:
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running command: {command}")
            print(e)
            break
    os.chdir("HideYourSelf")


def ip_info():
    clear_term()
    text_art("INFORMATION IP GATHERING\nBy GiuCoder")
    commands_ip = [
        "if [ -d 'INFORMATION-IP-GATHERING' ]; then rm -rf INFORMATION-IP-GATHERING; fi",
        "sudo apt-get install git python3 python3-pip",
        "clear",
        "git clone https://github.com/GiuCoder/INFORMATION-IP-GATHERING.git",
        "pip install pyfiglet",
        "pip install urllib3 colorama pyfiglet",
        "cd INFORMATION-IP-GATHERING",
        "clear",
        "python3 main.py"
    ]
    for command_ip in commands_ip:
        try:
            subprocess.run(command_ip, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running command: {command_ip}")
            print(e)
            break
    os.chdir("INFORMATION-IP-GATHERING")
    subprocess.run("python3 main.py", shell=True)


def virus():
    clear_term()
    text_art("Replicating Virus Python3\nBy GiuCoder")
    commands_virus = [
        "if [ -d 'Replicating-Virus-Python3' ]; then rm -rf Replicating-Virus-Python3; fi",
        "apt-get install python3 git",
        "git clone https://github.com/GiuCoder/Replicating-Virus-Python3.git",
        "cd Replicating-Virus-Python3",
        f"sudo python3 {os.path.join(os.getcwd(), 'Replicating-Virus-Python3', 'main.py')}"
    ]
    clear_term()
    text_art("Replicating Virus Python3\nBy GiuCoder")
    for command_virus in commands_virus:
        try:
            subprocess.run(command_virus, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running command: {command_virus}")
            print(e)
            break
    virus_dir = os.path.join(os.getcwd(), 'Replicating-Virus-Python3')
    if os.path.isdir(virus_dir):
        os.chdir(virus_dir)
    else:
        print("Error: Virus directory not found.")


def main(args):
    import os
    clear_term()
    if args.secure:
        secure()
    elif args.hide:
        hide()
    elif args.ip_info:
        ip_info()
    elif args.virus:
        virus()
    else:
        print(colored("\nInvalid Choice\n", "red"))
        os.system("python3 linuxtoolgiucoder.py --help")
        exit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=colored(
        "Kali Linux Tools By GiuCoder", "cyan"), usage="%(prog)s [options]")

    parser.add_argument("--secure", action="store_true",
                        help=colored("Secure Linux", "green"))
    parser.add_argument("--hide", action="store_true",
                        help=colored("HideYourSelf", "green"))
    parser.add_argument("--ip-info", action="store_true",
                        help=colored("INFORMATION IP GATHERING", "green"))
    parser.add_argument("--virus", action="store_true",
                        help=colored("Replicating Virus Python3", "green"))
    args = parser.parse_args()

    main(args)
