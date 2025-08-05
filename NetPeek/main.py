from assets.file import ip_host
from assets.file import service_name
from assets.file import port_service_name
from colorama import Fore, Style, init
import pyfiglet



init(autoreset=True)


banner = pyfiglet.figlet_format(" "*40 + "NetPeek")
print(Fore.CYAN + banner)
# Banner for developer
dev_banner = pyfiglet.figlet_format("By AhmedE7v", font="slant")

# Print the banner in green
print(Fore.GREEN + dev_banner)

# Extra credits line
print(Fore.CYAN + "★ Developed with ♥ by AhmedE7v | github.com/AhmedE7v")
print(Fore.YELLOW + "★ Telegram: @EG_SILENT_MAN | TikTok: @a7med_e7v")



def show_menu():
    
    print(Fore.CYAN + "\n Select a tool to run:\n")

    # جدول الأدوات
    print(Fore.YELLOW + "╔═══════════════════════╗═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print(Fore.GREEN  + "║ 1. IP & Host    -It converts any website name (such as google.com) to IP addresses and displays the host name without a beacon.         ║")
    print(Fore.MAGENTA+ "║ 2. Service Name -Type the port number (e.g. 80), which identifies the name of the service that usually uses this port (e.g. HTTP).      ║")
    print(Fore.BLUE   + "║ 3. Port Service -Type the name of the service (e.g. ftp), which is its port number (e.g. 21).                                           ║")
    print(Fore.YELLOW + "╚═══════════════════════╝═════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝")
    
    # الاختيار
    choice = input(Fore.CYAN + "\n➤ Your choice: ")
    if choice == "1":
        ip_host.ip_host()
    elif choice == "2":
        service_name.service_name()
    elif choice == "3":
        port_service_name.port_service()
    else:
        print(Fore.RED + "Invalid selection ")

if __name__ == "__main__":
    show_menu()
