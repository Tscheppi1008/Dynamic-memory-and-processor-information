import sys
import time as t
import psutil as p
import colorama
from colorama import Fore, Back, Style
import GPUtil
colorama.init(autoreset=True)


h = 100.0

def display_usage(cpu_usage, mem_usage, bars = 50):
    cpu_percent = (cpu_usage / h)
    cpu_bar = f'{Fore.BLUE}█' * int(cpu_percent * bars) + f'{Fore.MAGENTA}-' * (bars - int(cpu_percent * bars))
    
    mem_percent = (mem_usage / h)
    mem_bar = f'{Fore.GREEN}█' * int(mem_percent * bars) + f'{Fore.MAGENTA}-' * (bars - int(mem_percent * bars))

    print(f"\r {Fore.GREEN} MEM Usage: {Fore.WHITE}|{mem_bar}{Fore.WHITE}| {Fore.RED}{mem_usage:.2f}%  ", end="")
    print(f" {Fore.BLUE}CPU Usage: {Fore.WHITE}|{cpu_bar}{Fore.WHITE}| {Fore.RED}{cpu_usage:.2f}%  ", end="\r")
    
    


while True:
    
    display_usage(p.cpu_percent(), p.virtual_memory().percent, 30)
    t.sleep(0.5)




