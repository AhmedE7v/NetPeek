import socket
import time
from assets.file import interface
from colorama import Fore, Style, init

def service_name():
    print(Fore.CYAN + """This tool allows you to enter a port number and find out which service is commonly associated with it (e.g., port 80 → HTTP).
If the port is known, it displays the corresponding service name.
Otherwise, it will inform you that no known service is associated with the port.\n""")
    time.sleep(2)
    p = input(Fore.YELLOW +"Enter the port to know the service nema  : ")

    try:
        service_name = socket.getservbyport(int(p))
        time.sleep(1.5)
        print(Fore.GREEN +"Searching for service port...")
        time.sleep(1.5)
        print(service_name)
        interface.show_social_links()

        
       
    except OSError:
        time.sleep(1.6)
        print(Fore.GREEN +"Searching for service port...")
        time.sleep(2.5)
        print(Fore.RED + "This port does not have a known service.")
        interface.show_social_links()

        


if __name__ == "__main__":
    service_name()