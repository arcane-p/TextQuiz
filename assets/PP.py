#!/usr/bin/env python3
#Pretty printing
from colorama import init, Fore, Back, Style

class PPrint():
    def __init__(self, message, type="info"):
        self.message = message
        self.type = type
        init() #colorama.init()
        if self.type == "plus":
            print(f"{Style.BRIGHT}{Fore.BLUE}[+] {Style.NORMAL}{Fore.RESET}{message}")
        elif self.type == "minus":
            print(f"{Style.BRIGHT}{Fore.RED}[-] {Style.NORMAL}{Fore.RESET}{message}")
        elif self.type == "info":
            print(f"{Style.BRIGHT}{Fore.YELLOW}[*] {Style.NORMAL}{Fore.RESET}{message}")
        elif self.type == "module":
            print(f"{Style.BRIGHT}[?] {Style.NORMAL}{message}")
