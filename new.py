import os,time,random,sys

os.system('clear')
def text(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.25)
text('\u001b[32;1m[+] LOADING [==============================================] \n[+] COMPLETED')
print("_"*60)
print("                                                 ")

print("""\u001b[32;1m888    888     d8888   .d8888b.  888    d8P  
888    888    d8P888  d88P  Y88b 888   d8P   
888    888   d8P 888  888    888 888  d8P    
8888888888  d8P  888  888        888d88K     
888    888 d88   888  888        8888888b    
888    888 8888888888 888    888 888  Y88b   
888    888       888  Y88b  d88P 888   Y88b  
888    888       888   "Y8888P"  888    Y88b\n\n888    888          888888b.   
888    888          888  "88b  
888    888          888  .88P  
8888888888 888  888 8888888K.  
888    888 888  888 888  "Y88b 
888    888 888  888 888    888 
888    888 Y88b 888 888   d88P 
888    888  "Y88888 8888888P    V1.0
""")

print("_"*60)

print("\033[1;36;40m\nDeveloped By EL3©7®0|\|5 54G4®\nProgramming Language --- Python3\nFollow Me on GitHub ---  @Electrons-Force \nTested Only On Termux!")

print("\u001b[32;1m_"*60)

def tools():
	print(""" _____           _
|_   _|__   ___ | |___
  | |/ _ \ / _ \| / __|
  | | (_) | (_) | \__ \
  
  |_|\___/ \___/|_|___/""")
	print("_"*60)
	print("\033[1;31;40m1.Nmap (network scanner)\n2.Shellphish (accounts phisher)\n3.Parat (RAT for Windows)\n4.saycheese (cam hacker)\n5.TBomb (bomber)\n6.Hydra\n7.Metasploit-Framework)\n8.D-TECT\n9.commix\n10.smb-scanner\n11.PhoneSploit\n12.TheFatRat (payload generator)\n13.ipcs\n14.GhostDroid\n15.routersploit\n16.ReconSpider\n17.SQL-Map \n18.DDOS Attack\n19.IPGeolocation\n20.TM Venom\n\u001b[32;1m\n0.Exit")
	print("_"*60)
	
tools()

loop = True

while loop:
	a=input("H4H> ")
	if a == "1":
		os.system("python nmap.py")
		tools()
		
			
	elif a == "2":
		os.system("python shellphish.py")
		tools()
	
	elif a == '3':
		os.system("python parat.py")
		tools()
		
	elif a =="4":
		os.system("python saycheese.py")
		tools()
	
	elif a =="5":
		os.system("python TBomb.py")
		tools()
		
	elif a =="6":
		os.system("python hydra.py")
		tools()
		
	elif a =="7":
		os.system("python metasploit.py")
		tools()
	
	
	elif a == "8":
		os.system("python D-TECT.py")
		tools()

	elif a == "9":
		os.system("python commix.py")
		tools()	

	elif a == "10":
		os.system("python smb-scanner.py")
		tools()

	elif a == "11":
		os.system("python phonesploit.py")
		tools()

	elif a == "12":
		os.system("python fatrat.py")
		tools()

	elif a == "13":
		os.system("python ipcs.py")
		tools()
	
	elif a == "14":
		os.system("python ghostdroid.py")
		tools()

	elif a == "15":
		os.system("python routersploit.py")
		tools()

	elif a == "16":
		os.system("python reconspider.py")
		tools()

	elif a == "17":
		os.system("python sql-map.py")
		tools()

	elif a == "18":
		os.system("python ddos.py")
		tools()

	elif a == "20":
		os.system("python TM-Venom.py")
		tools()

	elif a == "19":
		os.system("python ip.py")
		tools()









	elif a == "0":
		print("\033[1;36;40m[+] EXITING.......")
		break
   
        	
			
      
		
		
	
	

	