import requests
import argparse
import sys
from colorama import Fore

GREEN = Fore.GREEN
RED   = Fore.RED
WHITE = Fore.WHITE


def get_arguments():
    parser = argparse.ArgumentParser(description="Website hidden paths")
    parser.add_argument('-u' , '--url' , nargs='?' , dest='url' , help= "Website, example: http://www.example.com" , required=True)
    parser.add_argument('-w', '--wordlist', nargs='?', dest='wordlist', help='Wordlist file, example: /root/wordlists/wordlist.txt', required=True)
    args = parser.parse_args()
    return args


def request(url) :
    try :
        return requests.get(url)
    except :
        pass


def process(url , wordlist_location):
    try :
        
        r = requests.get(url + "/" + "wq7zx1dbnd4dqsax9nmk")
        r404 = len(r.text)
           
        with open(wordlist_location , "r") as wordlist :
            for line in wordlist :
                word = line.strip()
                subdomain = url + "/" + word
                response = request(subdomain)
                rcurrent = len(response.text)
                if rcurrent != r404 :
                    print(f'{WHITE}[+] Detected Hidden Dir/file :{GREEN} {subdomain} {RED} with {rcurrent} Bytes')

    except :
        print("Exit")
        sys.exit()

result = get_arguments()
process(result.url, result.wordlist)

