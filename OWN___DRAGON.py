import getpass
import os
import time
from random import choice
from colorama import Fore, Style, init
from datetime import datetime, timedelta
import warnings
import sys
import requests
import re

init(autoreset=True)

correct_email = "dx"
correct_password = "dx"

pairs = ['AUDCAD-OTC',
 'AUDCHF-OTC',
 'AUDJPY-OTC',
 'AUDNZD-OTC',
 'AUDUSD-OTC',
 'AXJAUD',
 'AXP-OTC',
 'BA-OTC',
 'BRLUSD-OTC',
 'BTCUSD-OTC',
 'CADCHF-OTC',
 'CADJPY-OTC',
 'CHFJPY-OTC',
 'CHIA50',
 'DJIUSD',
 'EURAUD-OTC',
 'EURCAD-OTC',
 'EURCHF-OTC',
 'EURGBP-OTC',
 'EURJPY-OTC',
 'EURNZD-OTC',
 'EURSGD-OTC',
 'EURUSD-OTC',
 'F40EUR',
 'FB-OTC',
 'FTSGBP',
 'GBPAUD-OTC',
 'GBPCAD-OTC',
 'GBPCHF-OTC',
 'GBPJPY-OTC',
 'GBPNZD-OTC',
 'GBPUSD-OTC',
 'HSIHKD',
 'IBXEUR',
 'INTC-OTC',
 'IT4EUR',
 'JNJ-OTC',
 'JPXJPY',
 'MCD-OTC',
 'MSFT-OTC',
 'NDXUSD',
 'NZDCAD-OTC',
 'NZDCHF-OTC',
 'NZDJPY-OTC',
 'PFE-OTC',
 'STXEUR',
 'UKBrent-OTC',
 'USCrude-OTC',
 'USDARS-OTC',
 'USDBDT-OTC',
 'USDCAD-OTC',
 'USDCHF-OTC',
 'USDCOP-OTC',
 'USDDZD-OTC',
 'USDEGP-OTC',
 'USDIDR-OTC',
 'USDINR-OTC',
 'USDJPY-OTC',
 'USDMXN-OTC',
 'USDNGN-OTC',
 'USDPHP-OTC',
 'USDPKR-OTC',
 'USDTRY-OTC',
 'XAGUSD-OTC',
 'XAUUSD-OTC',
 'USDZAR-OTC']

def login():
    print(Style.BRIGHT + Fore.RED + """


    ██████╗ ██████╗  █████╗  ██████╗  ██████╗ ███╗   ██╗
    ██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗  ██║
    ██║  ██║██████╔╝███████║██║  ███╗██║   ██║██╔██╗ ██║
    ██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║
    ██████╔╝██║  ██║██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║
    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝

""")
    print("                " + Style.BRIGHT + Fore.GREEN + "𝗘𝗡𝗧𝗘𝗥 𝗟𝗜𝗖𝗘𝗡𝗦𝗘 𝗞𝗘𝗬 𝗗𝗥𝗔𝗚𝗢𝗡-𝗫𝗧...!")
    print("\n")
    email = input("     " + Style.BRIGHT + Fore.RED + "𝗙𝗜𝗥𝗦𝗧 𝗞𝗘𝗬:-   ")
    print("\n\n")
    password = getpass.getpass("     " + Style.BRIGHT + Fore.RED + " 𝗦𝗘𝗖𝗢𝗡𝗗 𝗞𝗘𝗬:-   ")
    print("\n" *2)

    # Check for correct email and password
    if email == correct_email and password == correct_password:
        print("                    " + Style.BRIGHT + Fore.GREEN + " 𝗟𝗜𝗖𝗘𝗡𝗦𝗘 𝗩𝗘𝗥𝗜𝗙𝗜𝗗𝗘 [✓]")
        time.sleep(1)
    else:
        print("                  " + Style.BRIGHT + Fore.RED + "Login failed! Exiting...")
        exit()

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def show_banner():
    print(Fore.RED + """
     ██████╗░██████╗░░█████╗░░██████╗░░█████╗░███╗░░██╗
     ██╔══██╗██╔══██╗██╔══██╗██╔════╝░██╔══██╗████╗░██║
     ██║░░██║██████╔╝███████║██║░░██╗░██║░░██║██╔██╗██║
     ██║░░██║██╔══██╗██╔══██║██║░░╚██╗██║░░██║██║╚████║
     ██████╔╝██║░░██║██║░░██║╚██████╔╝╚█████╔╝██║░╚███║
     ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░░╚════╝░╚═╝░░╚══╝
    """)
    print("                  " + Style.BRIGHT + Fore.RED + "━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("                     " + Style.BRIGHT + Fore.GREEN + "VERIFIED LICENSE [✓]")
    print("                  " + Style.BRIGHT + Fore.RED + "━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(" " + Fore.CYAN + Style.BRIGHT + "﴾◀═══════>> DRAGON 𖤍 IS MOST POWERFUL 𖤍 SOFTWARE <<═══════➤﴿")
    print(" " + Fore.CYAN + Style.BRIGHT + "﴾◀═════════════════>> DRAGON - XT v4.2 <<════════════════➤﴿")
    print(" " + Fore.CYAN + Style.BRIGHT + "﴾◀══════════════>> TELEGRAM: @H4X_ADNAN_LR <<═════════════➤﴿")
    print(" " + Fore.CYAN + Style.BRIGHT + "﴾◀═══════════════>> DEVELOPER ―‣ ADNAN'〆 <<══════════════➤﴿")
    print("\n" *2)
    print("             " + Fore.YELLOW + Style.BRIGHT + "TIME_ZONE Asia/Dhaka UTC +6:00")
    print("              " + Fore.MAGENTA + Style.BRIGHT + "AVAILABLE BROKER [ QUOTEX ]")
    print(Style.BRIGHT + Fore.RED + "━" * 65)
    print("\n")

def get_user_input():
    while True:
        DEAF00_COLOR = "\033[38;2;222;175;0m"  # Hex #DEAF00 as RGB (222, 175, 0)
        selected_pairs = input(Style.BRIGHT + DEAF00_COLOR + "𓆰⚚𓆪 TYPE YOUR CURRENCY NAME :  " + Style.BRIGHT + Fore.MAGENTA).split(",")
        selected_pairs = [pair.strip() for pair in selected_pairs if pair.strip() in pairs]

        if not selected_pairs:
            print(Style.BRIGHT + Fore.RED + "Invalid pair selected. Please choose a valid pair.")
        else:
            break

    while True:
        DEAF00_COLOR = "\033[38;2;222;175;0m"  # Hex #DEAF00 as RGB (222, 175, 0)
        day_analysis = input(Style.BRIGHT + DEAF00_COLOR + "𓆰⚚𓆪 DAY ANALYSIS (1-30):  " + Style.BRIGHT + Fore.MAGENTA)

        if day_analysis.isdigit() and 1 <= int(day_analysis) <= 30:
            break
        else:
            print(Style.BRIGHT + Fore.RED + "Oops, out of range. Please enter a value between 1 and 30.")

    while True:
        DEAF00_COLOR = "\033[38;2;222;175;0m"  # Hex #DEAF00 as RGB (222, 175, 0)
        min_percentage = input(Style.BRIGHT + DEAF00_COLOR + "𓆰⚚𓆪 PERCENTAGE (0-100):  " + Style.BRIGHT + Fore.MAGENTA)

        if min_percentage.isdigit() and 0 <= int(min_percentage) <= 100:
            break
        else:
            print(Style.BRIGHT + Fore.RED + "Oops, out of range. Please enter a value between 0 and 100.")

    while True:
        DEAF00_COLOR = "\033[38;2;222;175;0m"  # Hex #DEAF00 as RGB (222, 175, 0)
        filter_value = input(Style.BRIGHT + DEAF00_COLOR + "𓆰⚚𓆪 Filters 1 [H] or 2 [T]:  " + Style.BRIGHT + Fore.MAGENTA)

        if filter_value.isdigit() and 1 <= int(filter_value) <= 2:
            break
        else:
            print(Style.BRIGHT + Fore.RED + "Oops, out of range. Please enter a value 1 or 2.")

    while True:
        DEAF00_COLOR = "\033[38;2;222;175;0m"  # Hex #DEAF00 as RGB (222, 175, 0)
        separate = input(Style.BRIGHT + DEAF00_COLOR + "𓆰⚚𓆪 RSI Filter? (1 [Y] or 0 [N]):  " + Style.BRIGHT + Fore.MAGENTA)

        if separate.isdigit() and int(separate) in [0, 1]:
            break
        else:
            print(Style.BRIGHT + Fore.RED + "Oops, out of range. Please enter a value 1 or 0.")

    DEAF00_COLOR = "\033[38;2;222;175;0m"  # Hex #DEAF00 as RGB (222, 175, 0)
    signal_type_prompt = "𓆰⚚𓆪 SELECT SIGNAL TYPE {NORMAL}:  "
    print(f"{DEAF00_COLOR}{Style.BRIGHT}{signal_type_prompt}{Style.RESET_ALL}", end="")

    while True:
        signal_type = input().strip().lower()
        if signal_type in ['normal', 'blackout']:
            break
        else:
            print(Style.BRIGHT + Fore.RED + "Invalid signal type. Please choose 'normal' or 'blackout'.")
            print(f"{DEAF00_COLOR}{Style.BRIGHT}{signal_type_prompt}{Style.RESET_ALL}", end="")


    while True:
        DEAF00_COLOR = "\033[38;2;222;175;0m"  # Hex #DEAF00 as RGB (222, 175, 0)
        start_time = input(Style.BRIGHT + DEAF00_COLOR + "𓆰⚚𓆪 START OF THE LIST (HH:MM): " + Style.BRIGHT + Fore.MAGENTA)
        if re.match(r'^\d{2}:\d{2}$', start_time):
            break
        else:
            print(Style.BRIGHT + Fore.RED + "Invalid time format. Please enter in HH:MM format.")

    while True:
        DEAF00_COLOR = "\033[38;2;222;175;0m"  # Hex #DEAF00 as RGB (222, 175, 0)
        end_time = input(Style.BRIGHT + DEAF00_COLOR + "𓆰⚚𓆪 END OF THE LIST (HH:MM): " + Style.BRIGHT + Fore.MAGENTA)
        if re.match(r'^\d{2}:\d{2}$', end_time):
            break
        else:
            print(Style.BRIGHT + Fore.RED + "Invalid time format. Please enter in HH:MM format.")

        DEAF00_COLOR = "\033[38;2;222;175;0m"  # Hex #DEAF00 as RGB (222, 175, 0)
    signal_type_prompt0 = "𓆰⚚𓆪 SELECT SIGNAL TYPE (CALL/PUT/BOTH): "
    print(f"{DEAF00_COLOR}{Style.BRIGHT}{signal_type_prompt0}{Style.RESET_ALL}{Style.BRIGHT}{Fore.MAGENTA}", end="" + Style.BRIGHT + Fore.MAGENTA)

    while True:
        DEAF00_COLOR = "\033[38;2;222;175;0m"  # Hex #DEAF00 as RGB (222, 175, 0)
        signal_type0 = input().strip().lower()
        if signal_type0 in ['call', 'put', 'both']:
            break
        else:
            print(Style.BRIGHT + Fore.RED + "Invalid signal type. Please choose CALL, PUT, or BOTH.")
            print(f"{DEAF00_COLOR}{Style.BRIGHT}{signal_type_prompt0}{Style.RESET_ALL}{Style.BRIGHT}{Fore.MAGENTA}", end="" + Style.BRIGHT + Fore.MAGENTA)

    print("\n")
    print(Style.BRIGHT + Fore.GREEN + "Loading Asset Data...")

    return selected_pairs, signal_type, day_analysis, min_percentage, start_time, end_time, filter_value, separate, signal_type0

def animate_loading(selected_pairs):
    colors = [Fore.RED, Fore.GREEN]
    bold = Style.BRIGHT
    text = "GETTING ASSET'S..."
    spinner = ['\\', '|', '/', '-']

    for idx, pair in enumerate(selected_pairs):
        color = colors[idx % len(colors)]
        end_time = time.time() + 3
        while time.time() < end_time:
            for spin in spinner:
                sys.stdout.write(f"\r{bold}{color}{text} {spin}   {pair}{Style.RESET_ALL}")
                sys.stdout.flush()
                time.sleep(0.05)

    sys.stdout.write(f"\r{bold}{color}{text} Done with all pairs...{Style.RESET_ALL}\n")
    sys.stdout.flush()
    print("\n" * 1)
    print(" " + Fore.YELLOW + Style.BRIGHT + "Generated 𓆩DRAGON𓆪 Signal's")
    print(Style.BRIGHT + Fore.RED + "•═══════• DRAGON 𓆩⚚𓆪 LIST •═══════•[✓]")
    print(Style.BRIGHT + Fore.WHITE + "1 MINUITE :-")
    print("\n")

def generate_signal(selected_pairs, signal_type, day_analysis, min_percentage, start_time, end_time, filter_value, separate, signal_type0):

    animate_loading(selected_pairs)

    formatted_pairs = [pair.replace('-OTC', '_otc') for pair in selected_pairs]

    # Join the selected_pairs list into a comma-separated string
    pairs_str = ','.join(formatted_pairs)

    params = {
        'start_time': start_time,
        'end_time': end_time,
        'days': day_analysis,
        'pairs': pairs_str,  # Changed from list to comma-separated string
        'mode': signal_type,
        'min_percentage': min_percentage,
        'filter': filter_value,
        'separate': separate
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    url = "https://alltradingapi.com/signal_list_gen/qx_signal.js"

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()

        try:
            data = response.json()
            return data['signals'] if 'signals' in data else []
        except ValueError:
            response_text = response.text
            pattern2 = re.compile(r"(?i)[A-Z]{2}～([A-Z]+)_otc～(\d{2}:\d{2})～(\w+)")
            pattern1 = re.compile(r"(?i)[A-Z]{2}～([A-Z]+)_otc～(\d{2}:\d{2})")

            lines = response_text.splitlines()

            signals_found = False
            signals = []

            for line in lines:
                match2 = pattern2.search(line)
                if match2:
                    pair, time_str, direction = match2.groups()
                    formatted_pair = f"{pair}-OTC"
                    if signal_type0.lower() == "call":
                        signal = f"{time_str},{formatted_pair},CALL"
                        print(Style.BRIGHT + Fore.GREEN + signal)
                        signals.append(signal)
                    elif signal_type0.lower() == "put":
                        signal = f"{time_str},{formatted_pair},PUT"
                        print(Style.BRIGHT + Fore.RED + signal)
                        signals.append(signal)
                    elif signal_type0.lower() == "both":
                        if direction.lower() == "call":
                            signal = f"{time_str},{formatted_pair},CALL"
                            print(Style.BRIGHT + Fore.GREEN + signal)
                            signals.append(signal)
                        elif direction.lower() == "put":
                            signal = f"{time_str},{formatted_pair},PUT"
                            print(Style.BRIGHT + Fore.RED + signal)
                            signals.append(signal)
                    signals_found = True
                    continue
                match1 = pattern1.search(line)
                if match1:
                    pair, time_str = match1.groups()
                    formatted_pair = f"{pair}-OTC"
                    signal = f"{time_str},{formatted_pair}"
                    print(Style.BRIGHT + Fore.RED + signal)
                    signals.append(signal)
                    signals_found = True

            if not signals_found:
                print("No signals found")

            return signals
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return []

def display_signals(signals):
    print("\n")
    print(Style.BRIGHT + Fore.RED + "•═══════•[✓] END THE DRAGON SIGNAL [✓] •═══════•")
    print("\n" * 1)
    finished_message = Fore.LIGHTYELLOW_EX + Style.BRIGHT + " 𓆩====== FINISHED ✧ SINAI'S ======𓆪"
    print("     " + finished_message)
    print("\n")
    print("             " + Style.BRIGHT + Fore.CYAN + " 𓆩DRAGON-XT ⚚ v4.05𓆪")

def copy_signals(signals):
    signal_text = "\n".join(signals)
    try:
        import pyperclip
        pyperclip.copy(signal_text)
        print(Style.BRIGHT + Fore.GREEN + "Signals copied to clipboard!")
    except ImportError:
        print(Style.BRIGHT + Fore.RED + "pyperclip is not installed. Please install it to use this feature.")

def main():
    clear_screen()
    login()
    clear_screen()
    show_banner()

    selected_pairs, signal_type, day_analysis, min_percentage, start_time, end_time, filter_value, separate, signal_type0 = get_user_input()

    signals = generate_signal(selected_pairs, signal_type, day_analysis, min_percentage, start_time, end_time, filter_value, separate, signal_type0)

    if not signals:
        print(Style.BRIGHT + Fore.YELLOW + "𓆩====== FINISHED ✧ SIGNAL'S ======𓆪")
        print("\n")
        print("           " + Style.BRIGHT + Fore.CYAN + " 𓆩DRAGON-XT ⚚ v4.2𓆪")
    else:
        display_signals(signals)

    print("\n")
    print("        " + Style.BRIGHT + Fore.WHITE + "Type { C } For Copy SIGNAL'S")
    print(Style.BRIGHT + Fore.RED + "=" * 50)
    print("            " + Style.BRIGHT + Fore.RED + "Press " + Style.BRIGHT + Fore.YELLOW + "( q )" + Style.BRIGHT + Fore.RED + " For Quit")
    print(Style.BRIGHT + Fore.RED + "=" * 50)

    while True:
        user_choice = input().strip().lower()
        if user_choice == 'c':
            copy_signals(signals)
        elif user_choice == 'q':
            print(Style.BRIGHT + Fore.GREEN + "Exiting the DRAGON..Good Bye...")
            break
        else:
            print(Style.BRIGHT + Fore.RED + "Invalid choice. Please press 'c' to copy or 'q' to quit.")

if __name__ == "__main__":
    main()