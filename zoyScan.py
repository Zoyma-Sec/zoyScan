# Tool Title: zoyScan.py 
# Version: 0.0.1
# Authors 
# @Zoyma - https://zoyma-sec.github.io/
#
#Last Update: 2025/02/18
#
#
#
#!/usr/bin/python3
import subprocess
import re
import pyfiglet
from colorama import Back 
import sys


##########################
    ### Classes ###
##########################

def nmap():
    targetIp = input('Target IP: ').strip()
    print("\n")
    
    patron_ip = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'
    
    if re.match(patron_ip, targetIp):
        print('Analizando puertos y servicios...')


        resultado = subprocess.run(
            f"sudo /usr/bin/nmap {targetIp} -p- --open -vvv -sS --min-rate 500 -n",
            shell=True,
            capture_output=True,
            text=True
        )

        openPorts = re.findall(r"(\d+)/tcp\s+open", resultado.stdout)
        
        if openPorts:
            ports_str = ",".join(openPorts)
            print("\n")
            print(Back.YELLOW + f'Detected the following ports: {ports_str}' + Back.RESET)
            
            print("\n")
            print('Scanning versions and services...')
            subprocess.run(f"sudo /usr/bin/nmap -sCV -p{ports_str} {targetIp}", shell=True)
            print("\n")
            optionUdp = input('Scan finished, do you want to scan udp ports?: y/n  ')
            
            if (optionUdp == 'y' or optionUdp == 'yes'):
                print("\n")
                print('Scanning UDP ports...')
                print("\n")
                resultadoUDP = subprocess.run(
                    f"sudo /usr/bin/nmap {targetIp} -p- --open -sS --min-rate 500 -n -sU",
                    shell=True,
                    capture_output=True,
                    text=True
                )

                openUdpPorts = re.findall(r"(\d+)/udp\s+open", resultadoUDP.stdout)

                if openUdpPorts:

                    portsUDP_str = ",".join(openUdpPorts)
                    print("\n")
                    print(Back.YELLOW + f'Detected the following UDP ports: {portsUDP_str}' + Back.RESET)
                
                else:

                    print(Back.YELLOW + 'No UDP ports detected' + Back.RESET)
                
            else:
                print('Scan finished...')
                

        else:
            print(Back.YELLOW + 'No open ports detected' + Back.RESET)

        print("\n" * 2)
        

    else: 
        print(Back.RED + '\nEl formato de la IP es incorrecto...' + Back.RESET)
        nmap()

def wfuzz():
    
    def bruteForceDirectory():

        print('Add the url (example: http://example.com/): ')
        url= input('URL: ')
        print("\n")
        print('Do you want to add a new wordlist or use the default one? ')
        option = input('def/new: ')

        if (option == 'new'):

            print("\n")
            pwdWordlist = input('Introduce your wordlist: ')
            print("\n")
            status = input("Hide status code (404 by defect)? (y/n): ")
            
            if (status == 'yes' or status == 'y'):

                print("\n")
                statusCode = input('Which code do you want to hide?:')
                print("\n")
                print("Starting attack")
                subprocess.run(f"/usr/bin/wfuzz -c --hc=404,{statusCode} -t 200 -w {pwdWordlist} {url}/FUZZ", shell=True)
            
            else:

                print("\n")
                print("Starting attack")
                subprocess.run(f"/usr/bin/wfuzz -c --hc=404 -t 200 -w {pwdWordlist} {url}/FUZZ", shell=True)
        else:
            
            print("\n")
            status = input("Hide status code (404 by defect)? (y/n): ")
            
            if (status == 'yes' or status == 'y'):

                print("\n")
                statusCode = input('Which code do you want to hide?:')
                print("\n")
                print("Starting attack")
                subprocess.run(f"/usr/bin/wfuzz -c --hc=404,{statusCode} -t 200 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt {url}/FUZZ", shell=True)
            
            else:

                print("\n")
                print("Starting attack")
                subprocess.run(f"/usr/bin/wfuzz -c --hc=404 -t 200 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt {url}/FUZZ", shell=True)

            #print("\n")
            #print('Running the following command: /usr/bin/wfuzz -c --hc=404 -t 200 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt http://URLTARGET/FUZZ...')
            #print("\n")
            #lsubprocess.run(f"/usr/bin/wfuzz -c --hc=404 -t 200 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt {url}/FUZZ", shell=True)

        
    def bruteForceExtension():
        
        print('Add the url (example: http://example.com/): ')
        url= input('URL: ')
        
        


    def bruteForceSubdomains():

        print('bs')
    
    
    print("\n" * 2)
    print("[*] Choose an attack: [*]")
    print("\n")
    print("[1] Directory brute force")
    print("[2] Extension brute force")
    print("[3] Subdomain brute force")
    print("[4] Back")
    print("\n")
    option = int(input("Option: "))
    print("\n")

    if (option == 1):
        
        bruteForceDirectory()

    if (option == 2):
        
        bruteForceExtension()

    if (option == 3):

        bruteForceSubdomains()

    if (option == 4):
        fuzzing()
    

def fuzzing():

    print("\n" * 2)
    print("[*] Choose a tool: [*]")
    print("\n")
    print("[1] wfuzz")
    print("[2] gobuster")
    print("[3] feroxbuster")
    print("[4] dirsearch")
    print("[5] Back")
    print("\n")
    option = int(input("Option: "))
    print("\n")

    if (option == 1):
        wfuzz()

    if (option == 2):
        gobuster()

    if (option == 3):
        wfuzz()

    if (option == 4):
        dirsearch()

    if (option == 5):
        start()



def start():

    print("\n" * 2)
    print("[*] Que quieres realizar: [*]")
    print("\n")
    print("[1] Nmap")
    print("[2] Fuzzing")
    print("[3] Fuerza bruta a un servicio")
    print("[4] To do")
    print("[5] Salir")
    print("\n")
    option = int(input("Option: "))
    print("\n")

    if (option == 1):
        nmap()

    if (option == 2):
        fuzzing()

##########################
    ### Intro ###
##########################

def imprimir_cabecera():
  
  print('*******************************************')
  ascii_art = pyfiglet.figlet_format("zoyScan")
  print(ascii_art)
  print(f"# Tool Title: DogaScan") 
  print(f"# Version: 0.0.1")
  print(f"# Authors ")
  print(f"# @Zoyma - https://zoyma-sec.github.io/")
  print('*******************************************')
  print("\n" * 3)
imprimir_cabecera()
start()








