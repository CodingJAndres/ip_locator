import sys
import requests
import argparse
from colorama import Fore, Style, init


init()


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


def tracker(ip_address, output_file=None):
    banner()
    try:
       
        response = requests.get(f"http://ip-api.com/json/{ip_address}", headers={"User-Agent": "Mozilla/5.0"})
        data = response.json()

        
        if data['status'] == 'fail':
            print(color_text("\nError - No hay información de la IP", 'red'))
            sys.exit(1)

        
        results = [
            f"\tIP: {data['query']}",
            f"\tPaís: {data['country']}",
            f"\tCiudad: {data['city']}",
            f"\tRegión: {data['regionName']}",
            f"\tLatitud: {data['lat']}",
            f"\tLongitud: {data['lon']}",
            f"\tISP: {data['isp']}",
            f"\tGoogle Maps Link: https://www.google.com/maps?q={data['lat']},{data['lon']}"
        ]

        
        for line in results:
            print(color_text(line, 'gray'))

        
        if output_file:
            with open(output_file, 'w') as file:
                file.write('\n'.join(results))
            print(color_text(f"\nResultados guardados en: {output_file}", 'green'))
    except requests.RequestException as e:
        print(color_text(f"\nError al realizar la solicitud: {str(e)}", 'red'))
    sys.exit(0)


def main():
    parser = argparse.ArgumentParser(description='Rastrear información de IP y crear enlaces de Google Maps')
    parser.add_argument('-i', '--ip', type=str, help='Dirección IP a rastrear')
    parser.add_argument('-o', '--output', type=str, help='Guardar los resultados en un archivo')
    args = parser.parse_args()

    
    if args.ip:
        tracker(args.ip, args.output)
    else:
        banner()
        try:
            
            response = requests.get("http://ip-api.com/json/", headers={"User-Agent": "Mozilla/5.0"})
            data = response.json()

            if data['status'] == 'fail':
                print(color_text("\nError - No hay información de la IP", 'red'))
                sys.exit(1)

            results = [
                f"\tIP: {data['query']}",
                f"\tPaís: {data['country']}",
                f"\tCiudad: {data['city']}",
                f"\tRegión: {data['regionName']}",
                f"\tLatitud: {data['lat']}",
                f"\tLongitud: {data['lon']}",
                f"\tISP: {data['isp']}",
                f"\tGoogle Maps Link: https://www.google.com/maps?q={data['lat']},{data['lon']}"
            ]

           
            for line in results:
                print(color_text(line, 'gray'))

            if args.output:
                with open(args.output, 'w') as file:
                    file.write('\n'.join(results))
                print(color_text(f"\nResultados guardados en: {args.output}", 'green'))

        except requests.RequestException as e:
            print(color_text(f"\nError al realizar la solicitud: {str(e)}", 'red'))

if __name__ == "__main__":
    main()
