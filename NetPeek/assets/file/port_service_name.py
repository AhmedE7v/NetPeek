import socket
import time
from assets.file import interface
from colorama import Fore, Style, init

def port_service():
    print(Fore.CYAN + """This tool allows you to enter a service name (like http, ftp, or ssh) and it returns the default port number associated with that service.
If the service is recognized, it shows the correct port number.
Otherwise, it informs you that no known port is associated with the given service.\n""")
    time.sleep(1)
    port = input(Fore.YELLOW +"Enter the service nema to know the port : ")
    try:
        p  = socket.getservbyname(port)
        time.sleep(1.5)
        print(Fore.GREEN +"Searching for service port...")
        time.sleep(1.5)
        print(p)
        interface.show_social_links()
    except OSError:
        time.sleep(1.5)
        print(Fore.GREEN +"Searching for service port...")
        time.sleep(2.5)
        print(Fore.RED + "This service does not have a known port.")
        interface.show_social_links()

if __name__ == "__main__":
    port_service()
