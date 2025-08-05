import socket
import time
from colorama import Fore, Style, init
from assets.file import interface
init(autoreset=True)





def ip_host():
    a = print(Fore.CYAN + """
Website to IP Lookup Tool

This tool converts a website name (like google.com) into its IP address.
It also tries to find the host name related to that IP (Reverse DNS lookup).
If the website has no known IP, it will show a clear message.\n""")
    time.sleep(1.5)
    ip = input(Fore.YELLOW +"Website name turns into IP to connect : ")
    try:
        p = socket.gethostbyname(ip)
        print(Fore.GREEN +"Searching for IP...")
        time.sleep(2.5)
        print("theis is IP : " + p)
        time.sleep(1.5)
        print(Fore.GREEN +"Searching for host..." )
        time.sleep(2.5)
        host = socket.gethostbyaddr(str(p))
        print(host)
        interface.show_social_links()
    except OSError :
        print(Fore.GREEN +"Searching for IP...")
        time.sleep(2.5)
        print(Fore.RED +"This Website does not have a known IP.")
        time.sleep(1.5)
        interface.show_social_links()

if __name__ == "__main__":
    ip_host()