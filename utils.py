# Externe Datei für nützliche Funktionen
import torch

# Begrüßung und bissel Werbung
def print_welcome():
    print("\033[91mWelcome to the Python Image-Captioning Program for Mac / Windows / Linux  with MPS, CUDA OR CPU\033[0m")

def print_stats():
    print("\033[94mSalesforce/blip2-opt-2.7b ≈ 3.744.679.936 billion parameters\033[0m")

def print_credits():
    print("\033[91mProgramming: Markus Rößler\n\033[0m")
    print("\033[93mMR-XOTOX-NASSE-WÄNDE-SDXL\033[0m")
    print("\033[93mnow in version 1.0 FP32 at CivitAI\033[0m")
    print("\033[93mhttps://civitai.com/models/448483/mr-xotox-nasse-waende-sdxl\n\033[0m")

def print_footer():
    print("June / 2024 Version 1.3")
    print("\033[91mwww.der-zerfleischer.de\033[0m")

def get_device():
    device = torch.device("mps" if torch.backends.mps.is_available() else "cuda" if torch.cuda.is_available() else "cpu")
    return device

###########
def filter_and_sort_allowed_list(allowed_file, ignore_file):
    # Lies die Einträge aus der Ignore-Liste
    with open(ignore_file, 'r') as file:
        ignore_list = set(line.strip().lower() for line in file)

    # Lies die Einträge aus der Allowed-Liste
    with open(allowed_file, 'r') as file:
        allowed_list = [line.strip().lower() for line in file]

    # Filtere die Allowed-Liste, um Einträge zu entfernen, die in der Ignore-Liste vorkommen
    filtered_allowed_list = [entry for entry in allowed_list if entry not in ignore_list]

    # Sortiere die gefilterte Liste alphabetisch
    sorted_filtered_allowed_list = sorted(filtered_allowed_list)

    # Schreibe die sortierte und gefilterte Liste zurück in die Allowed-Liste Datei
    with open(allowed_file, 'w') as file:
        for entry in sorted_filtered_allowed_list:
            file.write(entry + '\n')

# Beispielaufruf der Funktion
filter_and_sort_allowed_list('allowed_words.txt', 'ignore_liste.txt')
###########
