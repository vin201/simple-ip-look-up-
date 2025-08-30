import os
import requests
import time
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

# Rainbow colors
rainbow = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

logo = [
"==================================================",
"| $$$$$$\\  $$$$$$$\\  $$$$$$$\\  $$$$$$\\ $$$$$$$$\\  |",
"|$$  __$$\\ $$  __$$\\ $$  __$$\\ \\_$$  _|\\__$$  __| |",
"|$$ /  $$ |$$ |  $$ |$$ |  $$ |  $$ |     $$ |    |",
"|$$ |  $$ |$$$$$$$  |$$$$$$$\\ |  $$ |     $$ |    |",
"|$$ |  $$ |$$  __$$< $$  __$$\\   $$ |     $$ |    |",
"|$$ |  $$ |$$ |  $$ |$$ |  $$ |  $$ |     $$ |    |",
"| $$$$$$  |$$ |  $$ |$$$$$$$  |$$$$$$\\    $$ |    |",
"| \\______/ \\__|  \\__|\\_______/ \\______|   \\__|    |",
"==================================================",
"               Orbit IP v2 by Purify"
]

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def rainbow_print(text):
    for i, line in enumerate(text):
        color = rainbow[i % len(rainbow)]
        print(f"{color}{line}")

def animate_logo(times=3, delay=0.1):
    """Animate logo with changing rainbow colors"""
    for _ in range(times):
        clear_console()
        global rainbow
        rainbow = rainbow[1:] + rainbow[:1]
        rainbow_print(logo)
        time.sleep(delay)

def loading_screen(duration=3):
    """Show a rainbow loading screen at startup"""
    clear_console()
    print(f"{Fore.CYAN}Welcome to Orbit v2...")
    for i in range(duration * 10):
        dots = "." * (i % 4)
        color = rainbow[i % len(rainbow)]
        print(f"{color}Loading{dots}", end="\r")
        time.sleep(0.1)
    print("\n")  # move to next line after loading

def get_ip_info(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return None

def display_info(info):
    if not info or info.get("status") != "success":
        print(f"{Fore.RED}Error: Could not retrieve IP information.")
        return
    fields = ["query", "isp", "regionName", "city", "zip", "country"]
    labels = ["IP", "ISP", "Region", "City", "Zip", "Country"]
    print("\n")
    for i, (label, field) in enumerate(zip(labels, fields)):
        color = rainbow[i % len(rainbow)]
        print(f"{color}{label}: {Fore.WHITE}{info.get(field, 'N/A')}")
    
    # Add Discord message
    print(f"\n{Fore.MAGENTA}Add purify_.1 on Discord!")

def main():
    # Startup loading screen
    loading_screen(duration=4)
    
    while True:
        clear_console()
        os.system("title Orbit IP v2 by Purify") if os.name == "nt" else None
        rainbow_print(logo)
        x = input(f"{Fore.CYAN}Press {Fore.GREEN}Enter{Fore.CYAN} to start or {Fore.RED}X{Fore.CYAN} to exit: ").strip().lower()
        if x == "x":
            print(f"{Fore.RED}Exiting program... Goodbye!")
            break

        clear_console()
        ip = input(f"{Fore.CYAN}Enter target IP: {Fore.WHITE}")
        animate_logo(times=4, delay=0.08)
        loading_screen(duration=3)  # loading after IP entry
        info = get_ip_info(ip)
        display_info(info)

        cont = input(f"\n{Fore.CYAN}Press {Fore.GREEN}Enter{Fore.CYAN} to continue or {Fore.RED}X{Fore.CYAN} to exit: ").strip().lower()
        if cont == "x":
            print(f"{Fore.RED}Exiting program... Goodbye!")
            break

if __name__ == "__main__":
    main()
