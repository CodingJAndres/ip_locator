import sys
import requests
import argparse
from colorama import Fore, Style, init

# Inicializar colorama
init()

# Colores
def color_text(text, color, attrs=None):
    color_map = {
        'green': Fore.GREEN,
        'gray': Fore.LIGHTBLACK_EX,
        'red': Fore.RED,
        'purple': Fore.MAGENTA,
        'cyan': Fore.CYAN,
        'off': Style.RESET_ALL
    }
    color_code = color_map.get(color, Style.RESET_ALL)
    return f"{color_code}{text}{Style.RESET_ALL}"

def banner():
    print(color_text("\n      / \\  `.  __..-,O ", 'green'))
    print(color_text("      :   \\ --''_..-'.'", 'green'))
    print(color_text("       |    . .-' `. '.'", 'green'))
    print(color_text("       :     .     .`.'", 'green'))
    print(color_text("        \\     `.  /  ..", 'green'))
    print(color_text("         \\      `.   ' .", 'green'))
    print(color_text("          `,       `.   \"", 'green'))
    print(color_text("         ,|,`.        `-\\. ", 'green'))
    print(color_text("        '.||  ``-...__..-`", 'green'))
    print(color_text("         |  |", 'green'))
    print(color_text("         |__|", 'green'))
    print(color_text("         /||\\", 'green'))
    print(color_text("        //||\\\\", 'green'))
    print(color_text("       // || \\", 'green'))
    print(color_text("    __//__||__\\__", 'green'))
    print(color_text("   '--------------' SSt", 'green'))

    print(color_text("\n    ---[ https://github.com/CodingJAndres/ ]---  ", 'green'))
    print(color_text("    +--==[ 01101000 01101111 01101100 01100001 ]==-- + ", 'green'))
    print()

# Help Panel
def help_panel():
    banner()
    print(color_text("Herramienta para rastrear una IP pública, puede ser su IP o alguna otra IP.", 'gray'))
    print("\nUSO:")
    print(f"\t{color_text('Rastrear su propia IP:', 'purple')} \t{color_text('./ipTracker.py', 'green')}")
    print(f"\t{color_text('Rastrear otra IP:', 'purple')} \t{color_text('./ipTracker.py -i <ip-address>', 'green')}")
    print("\nOPCIONES:")
    print(f"\t{color_text('-i <ip-address>', 'cyan')} {color_text('Rastrear otra dirección IP.', 'purple')}")
    print(f"\t{color_text('-h', 'cyan')} {color_text('Mostrar este panel de ayuda.', 'purple')}")
    sys.exit(0)

# Tracker
def tracker(ip_address):
    banner()
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}", headers={"User-Agent": "Mozilla/5.0"})
        data = response.json()
        
        if data['status'] == 'fail':
            print(color_text("\nError - No hay información de la IP", 'red'))
            sys.exit(1)

        print(color_text(f"\tIP: {color_text(data['query'], 'green')}", 'gray'))
        print(color_text(f"\tPais: {color_text(data['country'], 'green')}", 'gray'))
        print(color_text(f"\tCiudad: {color_text(data['city'], 'green')}", 'gray'))
        print(color_text(f"\tRegion: {color_text(data['regionName'], 'green')}", 'gray'))
        print(color_text(f"\tLatitud: {color_text(data['lat'], 'green')}", 'gray'))
        print(color_text(f"\tLongitud: {color_text(data['lon'], 'green')}", 'gray'))
        print(color_text(f"\tISP: {color_text(data['isp'], 'green')}", 'gray'))
    except requests.RequestException as e:
        print(color_text(f"\nError al realizar la solicitud: {str(e)}", 'red'))
    sys.exit(0)

# Main
def main():
    parser = argparse.ArgumentParser(description='Rastrear información de IP')
    parser.add_argument('-i', '--ip', type=str, help='Dirección IP a rastrear')
    args = parser.parse_args()
    
    if args.ip:
        tracker(args.ip)
    else:
        banner()
        try:
            response = requests.get("http://ip-api.com/json/", headers={"User-Agent": "Mozilla/5.0"})
            data = response.json()

            if data['status'] == 'fail':
                print(color_text("\nError - No hay información de la IP", 'red'))
                sys.exit(1)

            print(color_text(f"\tIP: {color_text(data['query'], 'green')}", 'gray'))
            print(color_text(f"\tPais: {color_text(data['country'], 'green')}", 'gray'))
            print(color_text(f"\tCiudad: {color_text(data['city'], 'green')}", 'gray'))
            print(color_text(f"\tRegion: {color_text(data['regionName'], 'green')}", 'gray'))
            print(color_text(f"\tLatitud: {color_text(data['lat'], 'green')}", 'gray'))
            print(color_text(f"\tLongitud: {color_text(data['lon'], 'green')}", 'gray'))
            print(color_text(f"\tISP: {color_text(data['isp'], 'green')}", 'gray'))
        except requests.RequestException as e:
            print(color_text(f"\nError al realizar la solicitud: {str(e)}", 'red'))

if __name__ == "__main__":
    main()
