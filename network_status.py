#!/usr/bin/python3
#pip3 install termcolor ipinfo

from ipinfo import getHandler
from requests import get
from os import system
from termcolor import colored, cprint
from subprocess import check_output

def ipinfo_layout():
    print(colored("------------------------------------", color1))
    print(colored(" - ", color1) +
          colored("pub ip\t", color2) +
          colored("| ", color1) +
          colored(f"{pub_ip}", color3))

    print(colored(" - ", color1) +
          colored("loc\t\t", color2) +
          colored("| ", color1) +
          colored(f"{ipinfo.city}, {ipinfo.region}, {ipinfo.country_name}", color3))

    print(colored(" - ", color1) +
          colored("pin\t\t", color2) +
          colored("| ", color1) +
          colored(f"{ipinfo.postal}", color3))

    print(colored(" - ", color1) +
          colored("isp\t\t", color2) +
          colored("| ", color1) +
          colored(f"{ipinfo.org}", color3))

    print(colored(" - ", color1) +
          colored("timezone\t", color2) +
          colored("| ", color1) +
          colored(f"{ipinfo.timezone}", color3))
    print(colored("------------------------------------", color1))

#set colors
color1 = 'white' #border
color2 = 'cyan'  #ipinfo label
color3 = 'green' #ipinfo data

clear = lambda: system('clear')
cursor_hide = lambda: system('tput civis')
pub_ip_provider = "http://icanhazip.com"
handler = getHandler()
details = handler.getDetails()
pub_ip_old = ""
links_old = ""


if __name__ == "__main__":
    cursor_hide()
    while True:

        try:
            links = check_output(['ip', '-br', '-c', 'addr']).decode("utf8")
            pub_ip = get(pub_ip_provider,timeout=1).content[:-1:].decode("utf8")

            if (links != links_old) or (pub_ip != pub_ip_old):
                ipinfo = handler.getDetails(pub_ip)

                clear()
                print(links)
                ipinfo_layout()

            pub_ip_old = pub_ip
            links_old = links

        except KeyboardInterrupt:
            break
        except:
            pass
