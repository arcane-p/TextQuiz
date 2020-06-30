#!/usr/bin/env python3
# Pretty printing
import sys
try:
    from colorama import init, Fore, Back, Style
except: # If colorama is not working, don't use it .
    pass


class PPrint():
    def __init__(self, message, type):
        self.message = message
        self.type = type
        if "colorama" not in sys.modules:
            if self.type == "plus":
                print(f"[+] {message}")
            elif self.type == "minus":
                print(f"[-] {message}")
            elif self.type == "info":
                print(f"[*] {message}")
            elif self.type == "module":
                print(f"[?] {message}")
        else:
            init()  # colorama.init()
            if self.type == "plus":
                print(
                    f"{Style.BRIGHT}{Fore.BLUE}[+] {Style.NORMAL}{Fore.RESET}{message}")
            elif self.type == "minus":
                print(
                    f"{Style.BRIGHT}{Fore.RED}[-] {Style.NORMAL}{Fore.RESET}{message}")
            elif self.type == "info":
                print(
                    f"{Style.BRIGHT}{Fore.YELLOW}[*] {Style.NORMAL}{Fore.RESET}{message}")
            elif self.type == "module":
                print(f"{Style.BRIGHT}[?] {Style.NORMAL}{message}")
