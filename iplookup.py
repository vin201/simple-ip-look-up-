import os
import requests
import colorama

# initialize colorama
colorama.init()

logo = """

 ▒█████   ██▀███   ▄▄▄▄    ██▓▄▄▄█████▓ ██▒   █▓
▒██▒  ██▒▓██ ▒ ██▒▓█████▄ ▓██▒▓  ██▒ ▓▒▓██░   █▒
▒██░  ██▒▓██ ░▄█ ▒▒██▒ ▄██▒██▒▒ ▓██░ ▒░ ▓██  █▒░
▒██   ██░▒██▀▀█▄  ▒██░█▀  ░██░░ ▓██▓ ░   ▒██ █░░
░ ████▓▒░░██▓ ▒██▒░▓█  ▀█▓░██░  ▒██▒ ░    ▒▀█░  
░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░▒▓███▀▒░▓    ▒ ░░      ░ ▐░  
  ░ ▒ ▒░   ░▒ ░ ▒░▒░▒   ░  ▒ ░    ░       ░ ░░  
░ ░ ░ ▒    ░░   ░  ░    ░  ▒ ░  ░           ░░  
    ░ ░     ░      ░       ░                 ░  
                        ░                   ░   

"""

while True:
    os.system("cls")  # clear console
    os.system("title orbit ipv2-bypurify")  # set console title
    print(logo)  # show the logo
    x = input("Press Enter to start...")

    if x == "":
        os.system("cls")
        IP = input("Enter target IP: ")

        # request IP data
        r = requests.get(f"http://ip-api.com/json/{IP}")
        info = r.json()

        print("\nRESULTS\n")
        print(f"Region: {info.get('regionName', 'N/A')}")
        print(f"City: {info.get('city', 'N/A')}")
        print(f"Zip: {info.get('zip', 'N/A')}")
        print(f"ISP: {info.get('isp', 'N/A')}")
        print(f"IP: {info.get('query', 'N/A')}")

        pause = input("\nPress Enter to continue...")
