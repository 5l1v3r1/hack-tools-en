# -*- coding: utf-8 -*-
import os
import time
import getpass
from time import sleep
from colorama import Fore, Back, Style

#Author-x11repo#
#When copying, please specify me as the Author and do not delete these lines
#!# Update 0.4.3.1 Alpha #!#

os.system("cls")
os.system("clear")
def menu(selected = ""):
	os.system("cls")
	os.system("clear")

	if(selected == ""):
		print(Fore.GREEN+f"╔╗ ╔╗        ╔╗  ╔════╗        ╔╗")
		print(Fore.GREEN+f"║║ ║║        ║║  ║╔╗╔╗║        ║║")
		print(Fore.GREEN+f"║╚═╝║╔══╗╔══╗║║╔╗╚╝║║╚╝╔══╗╔══╗║║ ╔══╗")
		print(Fore.GREEN+f"║╔═╗║║╔╗║║╔═╝║╚╝╝  ║║  ║╔╗║║╔╗║║║ ║══╣")
		print(Fore.GREEN+f"║║ ║║║╔╗║║╚═╗║╔╗╗  ║║  ║╚╝║║╚╝║║╚╗╠══║")
		print(Fore.GREEN+f"╚╝ ╚╝╚╝╚╝╚══╝╚╝╚╝  ╚╝  ╚══╝╚══╝╚═╝╚══╝{Style.RESET_ALL}")
		print(Fore.BLUE+f"                      a.k.a Kali Linux")
		print(Fore.BLUE+f"{Fore.BLUE}======================================")
		print(Fore.GREEN+f"{Style.RESET_ALL}Created By x11repo a.k.a Aqua")
		print(Fore.GREEN+f"{Style.RESET_ALL}Telegram: https://teleg.run/hacktools666")
		print(Fore.GREEN+f"{Style.RESET_ALL}Ver: 0.4.3.1 Alpha")
		print(Fore.BLUE+f"{Fore.BLUE}======================================")
		print(Fore.GREEN+f"{Style.RESET_ALL}{Fore.RED}[!]{Style.RESET_ALL} Install all repositories before using!\n to do this, enter {Fore.GREEN}999")
		print(Fore.BLUE+f"======================================")
		time.sleep(1)
		print(Fore.GREEN+f"{Style.RESET_ALL}1. Information collection {Fore.GREEN}")
		time.sleep(0.2)
		print(Fore.GREEN+f"{Style.RESET_ALL}2. Vulnerability analysis")
		time.sleep(0.2)
		print(Fore.GREEN+f"{Style.RESET_ALL}3. Database evaluation")
		time.sleep(0.2)
		print(Fore.GREEN+f"{Style.RESET_ALL}4. Attack the password")
		time.sleep(0.2)
		print(Fore.GREEN+f"{Style.RESET_ALL}5. Wireless attacks")
		time.sleep(0.2)
		print(Fore.GREEN+f"{Style.RESET_ALL}6. Engineering analysis")
		time.sleep(0.2)
		print(Fore.GREEN+f"{Style.RESET_ALL}7. Operating tools")
		time.sleep(0.2)
		print(Fore.GREEN+f"{Style.RESET_ALL}8. Sniffing and spoofing")
		time.sleep(0.2)
		print(Fore.GREEN+f"{Style.RESET_ALL}9. Operation post")
		time.sleep(0.2)
		print(Fore.GREEN+f"{Style.RESET_ALL}10. Criminalystic")
		time.sleep(0.2)
		print(Fore.GREEN+f"{Style.RESET_ALL}11. Reporting tool")
		time.sleep(0.2)
		print(Fore.GREEN+f"{Style.RESET_ALL}12. Stress-testing")
		time.sleep(0.2)
		print(Fore.GREEN+f"{Style.RESET_ALL}13. System services")
		time.sleep(0.2)
		print(Fore.BLUE+f"====================================")
		time.sleep(0.2)
		print(Fore.GREEN+f"To update, enter '7777'")
		time.sleep(0.2)
		print(Fore.BLUE+f"====================================")

	if(selected == ""):
		menu1 = input("$ > ")
		selected = menu1
	else:
		menu1 = selected

	print("SELECTED: " + selected)

	if selected == "7777":
		os.system("cd && rm -rf hack-tools-en && git clone https://github.com/x11-repo/hack-tools-en.git")
		print(Fore.BLUE+f"=====================================\n{Fore.GREEN}[INFO]{Style.RESET_ALL}Hack Tools \nбыл успешно обновлён.\n{Fore.GREEN}[INFO]{Style.RESET_ALL}Через 5 секунд он будет\n автоматически запущен\n{Fore.BLUE}====================================="+Style.RESET_ALL)
		time.sleep(5)
		os.system("cd && cd hack-tools-en && python3 HackTools.py")

	if selected == "999":
		print(Fore.BLUE+f"\n======================================"+Style.RESET_ALL)
		print("[INFO] you can collapse the terminal\n And go watch cartoons...")
		print ("Because it will take a long time.")
		print(Fore.BLUE+f"========================================"+Style.RESET_ALL)
		print(Fore.WHITE+f"{Back.RED}\nBut it is better to monitor the installation, since \nwill ask for confirmation when cloning"+Style.RESET_ALL)
		time.sleep(8)
		os.system("apt update")
		os.system("apt install -y git")
		os.system("apt install -y python")
		os.system("apt install -y python2")
		os.system("apt install -y wget")
		os.system("apt install -y nmap")
		os.system("plg install -y hydra ")
		os.system("apt update -y")
		os.system("apt install -y git")
		os.system("apt install python2")
		os.system("cd && git clone https://github.com/sqlmapproject/sqlmap.git")
		os.system("cd")
		os.system("apt install wget")
		os.system("cd && wget https://Auxilus.github.io/metasploit.sh")
		os.system("cd && bash metasploit.sh")
		os.system("cd && cd metasploit-framework")
		os.system("cd && gem install bundle --pre")
		os.system("cd && bundle config build.nokogiri --use-system-libraries")
		os.system("cd && bundle install")
		os.system("cd")
		os.system("apt update -y")
		os.system("apt install -y git")
		os.system("cd")
		os.system("apt update -y")
		os.system("apt install -y git")
		os.system("apt install -y python2")
		os.system("cd && git clone https://github.com/ihebski/angryFuzzer.git")
		os.system("cd && cd angryFuzzer")
		os.system("cd && pip2 install -r requirements.txt")
		os.system("cd && pip2 install requests")
		os.system("cd")
		os.system("apt update -y")
		os.system("apt install -y git")
		os.system("apt install -y php")
		os.system("cd && git clone https://github.com/Tuhinshubhra/RED_HAWK")
		os.system("cd")
		os.system("apt update -y")
		os.system("apt install -y python2")
		os.system("apt install -y git")
		os.system("cd && git clone https://github.com/evait-security/weeman.git")
		os.system("cd && cd weeman")
		os.system("cd && chmod +x weeman.py")
		os.system("cd")
		os.system("apt update -y")
		os.system("apt install -y git")
		os.system("apt install -y python")
		os.system("cd && git clone https://github.com/maldevel/IPGeoLocation.git")
		os.system("cd && cd IPGeoLocation")
		os.system("cd && pip install -r requirements.txt")
		os.system("cd")
		os.system("apt update -y")
		os.system("apt install -y git")
		os.system("apt install -y python")
		os.system("cd && git clone https://github.com/Mebus/cupp.git")
		os.system("apt update -y")
		os.system("apt install -y git")
		os.system("apt install -y python")
		os.system("apt install -y nano")
		os.system("pip install requests")
		os.system("cd && git clone https://github.com/reverse-shell/routersploit.git")
		os.system("cd && cd routersploit")
		os.system("pip2 install -r requirements.txt")
		os.system("pip2 install -r requirements-dev.txt")
		os.system("pip2 install -r requests")
		os.system("cd && apt install p0f") ### 1 пункт
		os.system("cd && apt install arp-scan") ###  arp-scan
		os.system("cd && apt install cutycapt") ##  cutycapt
		os.system("cd && apt install python-elixir python-qt4 xsltproc")
		os.system("cd && git clone https://github.com/secforce/sparta.git") ## python sparta.py
		os.system("cd && git clone https://github.com/golismero/golismero.git") ## python golismero.py
		os.system("cd && apt install masscan") ## masscan
		os.system("cd && wget https://github.com/`curl -s https://github.com/ron190/jsql-injection/releases | grep -E -o '/ron190/jsql-injection/releases/download/v[0-9]{1,2}.[0-9]{1,2}/jsql-injection-v[0-9]{1,2}.[0-9]{1,2}.jar' | head -n 1`") ## java -jar ./jsql-injection-v*.jar
		os.system("cd && apt install openvas") #### 2 punkt ## openvas-start
		os.system("cd && git clone https://github.com/SpiderLabs/jboss-autopwn.git") ## ./e2.sh ## 3 punkt
		os.system("cd && apt install dirb") ## dirb
		os.system("cd && git clone https://github.com/iniqua/plecost.git && cd plecost && chmod +x * && python3 setup.py install") ##plecost
		os.system("cd && gem install wpscan && wpscan --update --disable-tls-checks") ## wpscan
		os.system("cd && git clone https://github.com/epsylon/xsser.git && cd && cd xsser &&  python3 setup.py install &&  apt install python3-pycurl python3-bs4 python3-geoip python3-geoip2 python3-gi python3-cairocffi python3-selenium firefoxdriver &&  pip3 install pycurl bs4 geoip2 gobject cairocffi selenium") ## xsser
		os.system("cd &&  apt install crunch") ## 4 punkt ## crunch
		## hashcat -- cd hack-tools-en/assets/hashcat/ && ./hashcat64.bin --help
		os.system("cd && wget http://www.openwall.com/john/g/john-1.7.9.tar.bz2 && wget http://www.openwall.com/john/g/john-1.7.9.tar.bz2.sign && wget http://www.openwall.com/signatures/openwall-signatures.asc && pgp -ka openwall-signatures.asc && pgp john-1.7.9.tar.bz2.sign john-1.7.9.tar.bz2 &&  apt install john") ## john
		os.system("cd &&  apt install ncrack") ## ncrack
		os.system("cd &&  apt install aircrack-ng")## 5 punkt ## aircrack-ng
		os.system("cd &&  apt install git build-essential libssl-dev libpcap-dev && git clone https://github.com/joswr1ght/asleap && cd && cd asleap-2.2 && make")## cd asleap-2.2 && ./asleap
		os.system("cd &&  apt install libpcap-dev && wget http://www.willhackforsushi.com/code/cowpatty/4.6/cowpatty-4.6.tgz && tar xvzf cowpatty-*.tgz && cd cowpatty-4.6 && make &&  make install")### cd cowpatty-4.6 && ./cowpatty
		os.system("cd &&  apt install mdk3") ##  mdk3
		os.system("cd &&  apt install reaver") ##  reaver
		os.system("cd &&  apt install wifite") ##  wifite
		os.system("cd &&  apt install yara") ## 6 punkt ##  yara
		os.system("cd && curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall") ## 7 punkt
		###!!!! НАДО ДОБАВИТЬ МЕТАСПЛОИТ И АРМИТАЖ !!!!###
		os.system("cd && git clone https://github.com/trustedsec/social-engineer-toolkit/ set/ && cd && cd set && chmod +x * &&  python setup.py") ## setoolkit
		os.system("cd && apt install python3-pip && git clone https://www.github.com/threat9/routersploit && cd routersploit && python3 -m pip install -r requirements.txt") ## cd routersploit && python3 rsf.py
		os.system("cd &&  apt install yersinia") ## yersinia -h
		os.system("cd &&  apt install ettercap-graphical")## 8 punkt ##  ettercap -h
		os.system("cd &&  apt install sslstrip") ##  sslstrip -h
		os.system("cd &&  apt install dsniff") ##  dsniff -h
		os.system("cd &&  apt install wireshark") ##  wireshark
		os.system("cd &&  apt install dns2tcp") ## 9 punkt ##  dns2tcpd
		os.system("cd &&  apt install sbd") ##  sbd
		os.system("cd &&  apt install nghttp2") ##  nghttpd
		os.system("cd &&  apt install kdiff3")## 10 punkt ##  kdiff3 
		############## p0f
		os.system("cd &&  apt install xpdf") ##  xpdf
		os.system("cd &&  apt install libimage-exiftool-perl") ##  exiftool
		os.system("cd &&  apt install cherrytree")## 11 punkt ##  cherrytree
		os.system("cd &&  apt install xrdp &&  systemctl enable xrdp") ##  xrdp -h
		############## aircrack-ng --help
		os.system("cd &&  apt install ardour") ##  ardour5
		os.system("cd &&  apt install dhcpig") ##12 punkt ##  dhcpig
		os.system("cd &&  apt install t50") ##  t50 -h
		os.system("cd &&  apt install terminator") ##  terminator
		os.system("cd &&  apt install thc-ipv6") ## больше не поддерживается
		os.system("cd &&  apt install python3-crcelk python3-pluginbase python3-pyasn1 python3-serial python3-smoke-zephyr python3-tabulate python3-termcolor &&  pip3 install termineter")
		##############  termineter
		print("========================================")
		print("[+] Всё было успешно установленно :)")
		print("[+] Счастливого хакинга <3")
		kkk = input("[+] Вернутся в меню? (y/n): ")
		print("========================================")
		if kkk == "y":
			menu()
			return

	if selected == "1":
		os.system("clear")
		print(Fore.GREEN+f"╔╗ ╔╗        ╔╗  ╔════╗        ╔╗")
		print(Fore.GREEN+f"║║ ║║        ║║  ║╔╗╔╗║        ║║")
		print(Fore.GREEN+f"║╚═╝║╔══╗╔══╗║║╔╗╚╝║║╚╝╔══╗╔══╗║║ ╔══╗")
		print(Fore.GREEN+f"║╔═╗║║╔╗║║╔═╝║╚╝╝  ║║  ║╔╗║║╔╗║║║ ║══╣")
		print(Fore.GREEN+f"║║ ║║║╔╗║║╚═╗║╔╗╗  ║║  ║╚╝║║╚╝║║╚╗╠══║")
		print(Fore.GREEN+f"╚╝ ╚╝╚╝╚╝╚══╝╚╝╚╝  ╚╝  ╚══╝╚══╝╚═╝╚══╝{Style.RESET_ALL}")
		print(Fore.BLUE+f"                      a.k.a Kali Linux")
		print(Fore.BLUE+f"{Fore.BLUE}======================================")
		print(Fore.GREEN+f"{Style.RESET_ALL}Created By x11repo a.k.a Aqua")
		print(Fore.GREEN+f"{Style.RESET_ALL}Telegram: https://teleg.run/hacktools666")
		print(Fore.GREEN+f"{Style.RESET_ALL}Ver: 0.4.3.1 Alpha")
		print(Fore.BLUE+f"{Fore.BLUE}======================================")
		print(Fore.GREEN+f"{Style.RESET_ALL}{Fore.RED}[!]{Style.RESET_ALL} Перед использованием\n установите все репозитории!\n Для этого введите {Fore.GREEN}999")
		print(Fore.BLUE+f"======================================")
		print(Fore.GREEN+f"{Style.RESET_ALL}1. Information collection {Fore.GREEN}")
		print(Fore.BLUE+f"          {Fore.YELLOW}011) Arp-scan"+Style.RESET_ALL)
		print(Fore.YELLOW+f"          021) Cutycapt"+Style.RESET_ALL)
		print(Fore.YELLOW+f"          031) p0f"+Style.RESET_ALL)
		print(Fore.YELLOW+f"          041) SPARTA"+Style.RESET_ALL)
		print(Fore.YELLOW+f"          051) Golismero"+Style.RESET_ALL)
		print(Fore.YELLOW+f"          061) Masscan"+Style.RESET_ALL)
		print(Fore.YELLOW+f"          071) jSQL-injection"+Style.RESET_ALL)
		print(Fore.GREEN+f"{Style.RESET_ALL}2. Vulnerability analysis")
		print(Fore.GREEN+f"{Style.RESET_ALL}3. Database evaluation")
		print(Fore.GREEN+f"{Style.RESET_ALL}4. Attack the password")
		print(Fore.GREEN+f"{Style.RESET_ALL}5. Wireless attacks")
		print(Fore.GREEN+f"{Style.RESET_ALL}6. Engineering analysis")
		print(Fore.GREEN+f"{Style.RESET_ALL}7. Operating tools")
		print(Fore.GREEN+f"{Style.RESET_ALL}8. Sniffing and spoofing")
		print(Fore.GREEN+f"{Style.RESET_ALL}9. Operation post")
		print(Fore.GREEN+f"{Style.RESET_ALL}10. Criminalystic")
		print(Fore.GREEN+f"{Style.RESET_ALL}11. Reporting tool")
		print(Fore.GREEN+f"{Style.RESET_ALL}12. Stress-testing")
		print(Fore.GREEN+f"{Style.RESET_ALL}13. System services")
		print(Fore.BLUE+f"====================================")
		print(Fore.GREEN+f"To update, enter '7777'")
		print(Fore.BLUE+f"====================================")

		menu1 = input("$ > ")

	if menu1 == "011":
		os.system(" arp-scan")
		exit(0)
	if menu1 == "021":
		os.system(" cutycapt")
		exit(0)
	if menu1 == "031":
		os.system(" p0f")
		exit(0)
	if menu1 == "041":
		os.system("cd && cd sparta && chmod +x * &&  python sparta.py")
		exit(0)
	if menu1 == "051":
		os.system("cd && cd golismero && chmod +x * &&  python golismero.py")
		exit(0)
	if menu1 == "061":
		os.system(" masscan")
		exit(0)
	if menu1 == "071":
		os.system("java -jar ./jsql-injection-v*.jar")
		exit(0)

	if selected == "2":
		os.system("clear")
		print(Fore.GREEN+f"╔╗ ╔╗        ╔╗  ╔════╗        ╔╗")
		print(Fore.GREEN+f"║║ ║║        ║║  ║╔╗╔╗║        ║║")
		print(Fore.GREEN+f"║╚═╝║╔══╗╔══╗║║╔╗╚╝║║╚╝╔══╗╔══╗║║ ╔══╗")
		print(Fore.GREEN+f"║╔═╗║║╔╗║║╔═╝║╚╝╝  ║║  ║╔╗║║╔╗║║║ ║══╣")
		print(Fore.GREEN+f"║║ ║║║╔╗║║╚═╗║╔╗╗  ║║  ║╚╝║║╚╝║║╚╗╠══║")
		print(Fore.GREEN+f"╚╝ ╚╝╚╝╚╝╚══╝╚╝╚╝  ╚╝  ╚══╝╚══╝╚═╝╚══╝{Style.RESET_ALL}")
		print(Fore.BLUE+f"                      a.k.a Kali Linux")
		print(Fore.BLUE+f"{Fore.BLUE}======================================")
		print(Fore.GREEN+f"{Style.RESET_ALL}Created By x11repo a.k.a Aqua")
		print(Fore.GREEN+f"{Style.RESET_ALL}Telegram: https://teleg.run/hacktools666")
		print(Fore.GREEN+f"{Style.RESET_ALL}Ver: 0.4.3.1 Alpha")
		print(Fore.BLUE+f"{Fore.BLUE}======================================")
		print(Fore.GREEN+f"{Style.RESET_ALL}{Fore.RED}[!]{Style.RESET_ALL} Перед использованием\n установите все репозитории!\n Для этого введите {Fore.GREEN}999")
		print(Fore.BLUE+f"======================================")
		print(Fore.GREEN+f"{Style.RESET_ALL}1. Information collection {Fore.GREEN}")
		print(Fore.GREEN+f"{Style.RESET_ALL}2. Vulnerability analysis")
		print(Fore.BLUE+f"          {Fore.YELLOW}012) openvas"+Style.RESET_ALL)
		print(Fore.GREEN+f"{Style.RESET_ALL}3. Database evaluation")
		print(Fore.GREEN+f"{Style.RESET_ALL}4. Attack the password")
		print(Fore.GREEN+f"{Style.RESET_ALL}5. Wireless attacks")
		print(Fore.GREEN+f"{Style.RESET_ALL}6. Engineering analysis")
		print(Fore.GREEN+f"{Style.RESET_ALL}7. Operating tools")
		print(Fore.GREEN+f"{Style.RESET_ALL}8. Sniffing and spoofing")
		print(Fore.GREEN+f"{Style.RESET_ALL}9. Operation post")
		print(Fore.GREEN+f"{Style.RESET_ALL}10. Criminalystic")
		print(Fore.GREEN+f"{Style.RESET_ALL}11. Reporting tool")
		print(Fore.GREEN+f"{Style.RESET_ALL}12. Stress-testing")
		print(Fore.GREEN+f"{Style.RESET_ALL}13. System services")
		print(Fore.BLUE+f"====================================")
		print(Fore.GREEN+f"To update, enter '7777'")
		print(Fore.BLUE+f"====================================")

		menu1 = input("$ > ")

	if menu1 == "012":
		os.system(" openvas-start")
		exit(0)

	if selected == "3":
		os.system("clear")
		print(Fore.GREEN+f"╔╗ ╔╗        ╔╗  ╔════╗        ╔╗")
		print(Fore.GREEN+f"║║ ║║        ║║  ║╔╗╔╗║        ║║")
		print(Fore.GREEN+f"║╚═╝║╔══╗╔══╗║║╔╗╚╝║║╚╝╔══╗╔══╗║║ ╔══╗")
		print(Fore.GREEN+f"║╔═╗║║╔╗║║╔═╝║╚╝╝  ║║  ║╔╗║║╔╗║║║ ║══╣")
		print(Fore.GREEN+f"║║ ║║║╔╗║║╚═╗║╔╗╗  ║║  ║╚╝║║╚╝║║╚╗╠══║")
		print(Fore.GREEN+f"╚╝ ╚╝╚╝╚╝╚══╝╚╝╚╝  ╚╝  ╚══╝╚══╝╚═╝╚══╝{Style.RESET_ALL}")
		print(Fore.BLUE+f"                      a.k.a Kali Linux")
		print(Fore.BLUE+f"{Fore.BLUE}======================================")
		print(Fore.GREEN+f"{Style.RESET_ALL}Created By x11repo a.k.a Aqua")
		print(Fore.GREEN+f"{Style.RESET_ALL}Telegram: https://teleg.run/hacktools666")
		print(Fore.GREEN+f"{Style.RESET_ALL}Ver: 0.4.3.1 Alpha")
		print(Fore.BLUE+f"{Fore.BLUE}======================================")
		print(Fore.GREEN+f"{Style.RESET_ALL}{Fore.RED}[!]{Style.RESET_ALL} Перед использованием\n установите все репозитории!\n Для этого введите {Fore.GREEN}999")
		print(Fore.BLUE+f"======================================")
		print(Fore.GREEN+f"{Style.RESET_ALL}1. Information collection {Fore.GREEN}")
		print(Fore.GREEN+f"{Style.RESET_ALL}2. Vulnerability analysis")
		print(Fore.GREEN+f"{Style.RESET_ALL}3. Database evaluation")
		print(Fore.BLUE+f"          {Fore.YELLOW}013) Jboss-autopwn"+Style.RESET_ALL)
		print(Fore.YELLOW+f"          023) DirB"+Style.RESET_ALL)
		print(Fore.YELLOW+f"          033) Plecost"+Style.RESET_ALL)
		print(Fore.YELLOW+f"          043) WPScan"+Style.RESET_ALL)
		print(Fore.YELLOW+f"          053) xSSer"+Style.RESET_ALL)
		print(Fore.GREEN+f"{Style.RESET_ALL}4. Attack the password")
		print(Fore.GREEN+f"{Style.RESET_ALL}5. Wireless attacks")
		print(Fore.GREEN+f"{Style.RESET_ALL}6. Engineering analysis")
		print(Fore.GREEN+f"{Style.RESET_ALL}7. Operating tools")
		print(Fore.GREEN+f"{Style.RESET_ALL}8. Sniffing and spoofing")
		print(Fore.GREEN+f"{Style.RESET_ALL}9. Operation post")
		print(Fore.GREEN+f"{Style.RESET_ALL}10. Criminalystic")
		print(Fore.GREEN+f"{Style.RESET_ALL}11. Reporting tool")
		print(Fore.GREEN+f"{Style.RESET_ALL}12. Stress-testing")
		print(Fore.GREEN+f"{Style.RESET_ALL}13. System services")
		print(Fore.BLUE+f"====================================")
		print(Fore.GREEN+f"To update, enter '7777'")
		print(Fore.BLUE+f"====================================")

		menu1 = input("$ > ")

	if menu1 == "013":
		os.system("cd && cd jboss-autopwn &&  ./e2.sh")
		exit(0)
	if menu1 == "023":
		os.system(" dirb")
		exit(0)
	if menu1 == "033":
		os.system(" plecost")
		exit(0)
	if menu1 == "043":
		os.system(" wpscan")
		exit(0)
	if menu1 == "053":
		os.system(" xsser")
		exit(0)

	if selected == "4":
		os.system("clear")
		print(Fore.GREEN+f"╔╗ ╔╗        ╔╗  ╔════╗        ╔╗")
		print(Fore.GREEN+f"║║ ║║        ║║  ║╔╗╔╗║        ║║")
		print(Fore.GREEN+f"║╚═╝║╔══╗╔══╗║║╔╗╚╝║║╚╝╔══╗╔══╗║║ ╔══╗")
		print(Fore.GREEN+f"║╔═╗║║╔╗║║╔═╝║╚╝╝  ║║  ║╔╗║║╔╗║║║ ║══╣")
		print(Fore.GREEN+f"║║ ║║║╔╗║║╚═╗║╔╗╗  ║║  ║╚╝║║╚╝║║╚╗╠══║")
		print(Fore.GREEN+f"╚╝ ╚╝╚╝╚╝╚══╝╚╝╚╝  ╚╝  ╚══╝╚══╝╚═╝╚══╝{Style.RESET_ALL}")
		print(Fore.BLUE+f"                      a.k.a Kali Linux")
		print(Fore.BLUE+f"{Fore.BLUE}======================================")
		print(Fore.GREEN+f"{Style.RESET_ALL}Created By x11repo a.k.a Aqua")
		print(Fore.GREEN+f"{Style.RESET_ALL}Telegram: https://teleg.run/hacktools666")
		print(Fore.GREEN+f"{Style.RESET_ALL}Ver: 0.4.3.1 Alpha")
		print(Fore.BLUE+f"{Fore.BLUE}======================================")
		print(Fore.GREEN+f"{Style.RESET_ALL}{Fore.RED}[!]{Style.RESET_ALL} Перед использованием\n установите все репозитории!\n Для этого введите {Fore.GREEN}999")
		print(Fore.BLUE+f"======================================")
		print(Fore.GREEN+f"{Style.RESET_ALL}1. Information collection {Fore.GREEN}")
		print(Fore.GREEN+f"{Style.RESET_ALL}2. Vulnerability analysis")
		print(Fore.GREEN+f"{Style.RESET_ALL}3. Database evaluation")
		print(Fore.GREEN+f"{Style.RESET_ALL}4. Attack the password")
		print(Fore.BLUE+f"          {Fore.YELLOW}014) crunch"+Style.RESET_ALL)
		print(Fore.YELLOW+f"          024) hashCat"+Style.RESET_ALL) ## cd hack-tools-en/assets/hashcat/ && ./hashcat64.bin --help
		print(Fore.YELLOW+f"          034) john"+Style.RESET_ALL) # john
		print(Fore.YELLOW+f"          044) ncrack"+Style.RESET_ALL) # ncrack
		print(Fore.GREEN+f"{Style.RESET_ALL}5. Wireless attacks")
		print(Fore.GREEN+f"{Style.RESET_ALL}6. Engineering analysis")
		print(Fore.GREEN+f"{Style.RESET_ALL}7. Operating tools")
		print(Fore.GREEN+f"{Style.RESET_ALL}8. Sniffing and spoofing")
		print(Fore.GREEN+f"{Style.RESET_ALL}9. Operation post")
		print(Fore.GREEN+f"{Style.RESET_ALL}10. Criminalystic")
		print(Fore.GREEN+f"{Style.RESET_ALL}11. Reporting tool")
		print(Fore.GREEN+f"{Style.RESET_ALL}12. Stress-testing")
		print(Fore.GREEN+f"{Style.RESET_ALL}13. System services")
		print(Fore.BLUE+f"====================================")
		print(Fore.GREEN+f"To update, enter '7777'")
		print(Fore.BLUE+f"====================================")
		
		menu1 = input("$ > ")

	if menu1 == "014":
		os.system(" crunch")
		exit(0)
	if menu1 == "024":
		os.system("cd && cd hack-tools-en/assets/hashcat/ && ./hashcat64.bin --help")
		exit(0)
	if menu1 == "034":
		os.system(" john")
		exit(0)
	if menu1 == "044":
		os.system(" ncrack")
		exit(0)

	if selected == "5":
		os.system("clear")
		print(Fore.GREEN+f"╔╗ ╔╗        ╔╗  ╔════╗        ╔╗")
		print(Fore.GREEN+f"║║ ║║        ║║  ║╔╗╔╗║        ║║")
		print(Fore.GREEN+f"║╚═╝║╔══╗╔══╗║║╔╗╚╝║║╚╝╔══╗╔══╗║║ ╔══╗")
		print(Fore.GREEN+f"║╔═╗║║╔╗║║╔═╝║╚╝╝  ║║  ║╔╗║║╔╗║║║ ║══╣")
		print(Fore.GREEN+f"║║ ║║║╔╗║║╚═╗║╔╗╗  ║║  ║╚╝║║╚╝║║╚╗╠══║")
		print(Fore.GREEN+f"╚╝ ╚╝╚╝╚╝╚══╝╚╝╚╝  ╚╝  ╚══╝╚══╝╚═╝╚══╝{Style.RESET_ALL}")
		print(Fore.BLUE+f"                      a.k.a Kali Linux")
		print(Fore.BLUE+f"{Fore.BLUE}======================================")
		print(Fore.GREEN+f"{Style.RESET_ALL}Created By x11repo a.k.a Aqua")
		print(Fore.GREEN+f"{Style.RESET_ALL}Telegram: https://teleg.run/hacktools666")
		print(Fore.GREEN+f"{Style.RESET_ALL}Ver: 0.4.3.1 Alpha")
		print(Fore.BLUE+f"{Fore.BLUE}======================================")
		print(Fore.GREEN+f"{Style.RESET_ALL}{Fore.RED}[!]{Style.RESET_ALL} Перед использованием\n установите все репозитории!\n Для этого введите {Fore.GREEN}999")
		print(Fore.BLUE+f"======================================")
		print(Fore.GREEN+f"{Style.RESET_ALL}1. Information collection {Fore.GREEN}")
		print(Fore.GREEN+f"{Style.RESET_ALL}2. Vulnerability analysis")
		print(Fore.GREEN+f"{Style.RESET_ALL}3. Database evaluation")
		print(Fore.GREEN+f"{Style.RESET_ALL}4. Attack the password")
		print(Fore.GREEN+f"{Style.RESET_ALL}5. Wireless attacks")
		print(Fore.BLUE+f"          {Fore.YELLOW}015) aircrack-ng"+Style.RESET_ALL) # aircrack-ng
		print(Fore.YELLOW+f"          025) asleap-2"+Style.RESET_ALL) ##  cd asleap-2.2 && ./asleap
		print(Fore.YELLOW+f"          035) coWPAtty"+Style.RESET_ALL) # cd cowpatty-4.6 && ./cowpatty
		print(Fore.YELLOW+f"          045) mdk3"+Style.RESET_ALL) #  mdk3
		print(Fore.YELLOW+f"          055) reaver"+Style.RESET_ALL) #  reaver
		print(Fore.YELLOW+f"          065) wifite"+Style.RESET_ALL) #  wifite
		print(Fore.YELLOW+f"          075) RouterSploit"+Style.RESET_ALL) ##  cd routersploit && python3 rsf.py
		print(Fore.GREEN+f"{Style.RESET_ALL}6. Engineering analysis")
		print(Fore.GREEN+f"{Style.RESET_ALL}7. Operating tools")
		print(Fore.GREEN+f"{Style.RESET_ALL}8. Sniffing and spoofing")
		print(Fore.GREEN+f"{Style.RESET_ALL}9. Operation post")
		print(Fore.GREEN+f"{Style.RESET_ALL}10. Criminalystic")
		print(Fore.GREEN+f"{Style.RESET_ALL}11. Reporting tool")
		print(Fore.GREEN+f"{Style.RESET_ALL}12. Stress-testing")
		print(Fore.GREEN+f"{Style.RESET_ALL}13. System services")
		print(Fore.BLUE+f"====================================")
		print(Fore.GREEN+f"To update, enter '7777'")
		print(Fore.BLUE+f"====================================")
		
		menu1 = input("$ > ")

	if menu1 == "015":
		os.system(" aircrack-ng")
		exit(0)
	if menu1 == "025":
		os.system("cd && cd asleap-2.2 &&  ./asleap")
		exit(0)
	if menu1 == "035":
		os.system("cd && cd cowpatty-4.6 && ./cowpatty")
		exit(0)
	if menu1 == "045":
		os.system(" mdk3")
		exit(0)
	if menu1 == "055":
		os.system(" reaver")
		exit(0)
	if menu1 == "065":
		os.system(" wifite")
		exit(0)
	if menu1 == "075":
		os.system("cd && cd routersploit && python3 rsf.py")
		exit(0)

	if selected == "6":
		os.system("clear")
		print(Fore.GREEN+f"╔╗ ╔╗        ╔╗  ╔════╗        ╔╗")
		print(Fore.GREEN+f"║║ ║║        ║║  ║╔╗╔╗║        ║║")
		print(Fore.GREEN+f"║╚═╝║╔══╗╔══╗║║╔╗╚╝║║╚╝╔══╗╔══╗║║ ╔══╗")
		print(Fore.GREEN+f"║╔═╗║║╔╗║║╔═╝║╚╝╝  ║║  ║╔╗║║╔╗║║║ ║══╣")
		print(Fore.GREEN+f"║║ ║║║╔╗║║╚═╗║╔╗╗  ║║  ║╚╝║║╚╝║║╚╗╠══║")
		print(Fore.GREEN+f"╚╝ ╚╝╚╝╚╝╚══╝╚╝╚╝  ╚╝  ╚══╝╚══╝╚═╝╚══╝{Style.RESET_ALL}")
		print(Fore.BLUE+f"                      a.k.a Kali Linux")
		print(Fore.BLUE+f"{Fore.BLUE}======================================")
		print(Fore.GREEN+f"{Style.RESET_ALL}Created By x11repo a.k.a Aqua")
		print(Fore.GREEN+f"{Style.RESET_ALL}Telegram: https://teleg.run/hacktools666")
		print(Fore.GREEN+f"{Style.RESET_ALL}Ver: 0.4.3.1 Alpha")
		print(Fore.BLUE+f"{Fore.BLUE}======================================")
		print(Fore.GREEN+f"{Style.RESET_ALL}{Fore.RED}[!]{Style.RESET_ALL} Перед использованием\n установите все репозитории!\n Для этого введите {Fore.GREEN}999")
		print(Fore.BLUE+f"======================================")
		print(Fore.GREEN+f"{Style.RESET_ALL}1. Information collection {Fore.GREEN}")
		print(Fore.GREEN+f"{Style.RESET_ALL}2. Vulnerability analysis")
		print(Fore.GREEN+f"{Style.RESET_ALL}3. Database evaluation")
		print(Fore.GREEN+f"{Style.RESET_ALL}4. Attack the password")
		print(Fore.GREEN+f"{Style.RESET_ALL}5. Wireless attacks")
		print(Fore.GREEN+f"{Style.RESET_ALL}6. Engineering analysis")
		print(Fore.BLUE+f"          {Fore.YELLOW}016) yara"+Style.RESET_ALL) #  yara
		print(Fore.GREEN+f"{Style.RESET_ALL}7. Operating tools")
		print(Fore.GREEN+f"{Style.RESET_ALL}8. Sniffing and spoofing")
		print(Fore.GREEN+f"{Style.RESET_ALL}9. Operation post")
		print(Fore.GREEN+f"{Style.RESET_ALL}10. Criminalystic")
		print(Fore.GREEN+f"{Style.RESET_ALL}11. Reporting tool")
		print(Fore.GREEN+f"{Style.RESET_ALL}12. Stress-testing")
		print(Fore.GREEN+f"{Style.RESET_ALL}13. System services")
		print(Fore.BLUE+f"====================================")
		print(Fore.GREEN+f"To update, enter '7777'")
		print(Fore.BLUE+f"====================================")
		
		menu1 = input("$ > ")

	if menu1 == "016":
		os.system(" yara")
		exit(0)

	if selected == "7":
		os.system("clear")
		print(Fore.GREEN+f"╔╗ ╔╗        ╔╗  ╔════╗        ╔╗")
		print(Fore.GREEN+f"║║ ║║        ║║  ║╔╗╔╗║        ║║")
		print(Fore.GREEN+f"║╚═╝║╔══╗╔══╗║║╔╗╚╝║║╚╝╔══╗╔══╗║║ ╔══╗")
		print(Fore.GREEN+f"║╔═╗║║╔╗║║╔═╝║╚╝╝  ║║  ║╔╗║║╔╗║║║ ║══╣")
		print(Fore.GREEN+f"║║ ║║║╔╗║║╚═╗║╔╗╗  ║║  ║╚╝║║╚╝║║╚╗╠══║")
		print(Fore.GREEN+f"╚╝ ╚╝╚╝╚╝╚══╝╚╝╚╝  ╚╝  ╚══╝╚══╝╚═╝╚══╝{Style.RESET_ALL}")
		print(Fore.BLUE+f"                      a.k.a Kali Linux")
		print(Fore.BLUE+f"{Fore.BLUE}======================================")
		print(Fore.GREEN+f"{Style.RESET_ALL}Created By x11repo a.k.a Aqua")
		print(Fore.GREEN+f"{Style.RESET_ALL}Telegram: https://teleg.run/hacktools666")
		print(Fore.GREEN+f"{Style.RESET_ALL}Ver: 0.4.3.1 Alpha")
		print(Fore.BLUE+f"{Fore.BLUE}======================================")
		print(Fore.GREEN+f"{Style.RESET_ALL}{Fore.RED}[!]{Style.RESET_ALL} Перед использованием\n установите все репозитории!\n Для этого введите {Fore.GREEN}999")
		print(Fore.BLUE+f"======================================")
		print(Fore.GREEN+f"{Style.RESET_ALL}1. Information collection {Fore.GREEN}")
		print(Fore.GREEN+f"{Style.RESET_ALL}2. Vulnerability analysis")
		print(Fore.GREEN+f"{Style.RESET_ALL}3. Database evaluation")
		print(Fore.GREEN+f"{Style.RESET_ALL}4. Attack the password")
		print(Fore.GREEN+f"{Style.RESET_ALL}5. Wireless attacks")
		print(Fore.GREEN+f"{Style.RESET_ALL}6. Engineering analysis")
		print(Fore.GREEN+f"{Style.RESET_ALL}7. Operating tools")
		print(Fore.BLUE+f"          {Fore.YELLOW}017) Metasploit"+Style.RESET_ALL) # 
		print(Fore.YELLOW+f"          027) Social Ingeenering Tollkit"+Style.RESET_ALL) ##  setoolkit
		print(Fore.YELLOW+f"          037) RouterSploit"+Style.RESET_ALL) ##  cd routersploit && python3 rsf.py
		print(Fore.YELLOW+f"          047) yersinia"+Style.RESET_ALL) ##   yersinia -h
		print(Fore.GREEN+f"{Style.RESET_ALL}8. Sniffing and spoofing")
		print(Fore.GREEN+f"{Style.RESET_ALL}9. Operation post")
		print(Fore.GREEN+f"{Style.RESET_ALL}10. Criminalystic")
		print(Fore.GREEN+f"{Style.RESET_ALL}11. Reporting tool")
		print(Fore.GREEN+f"{Style.RESET_ALL}12. Stress-testing")
		print(Fore.GREEN+f"{Style.RESET_ALL}13. System services")
		print(Fore.BLUE+f"====================================")
		print(Fore.GREEN+f"To update, enter '7777'")
		print(Fore.BLUE+f"====================================")
		
		menu1 = input("$ > ")

	if menu1 == "017":
		print(" none, sorry.")
		exit(0)
	if menu1 == "027":
		os.system(" setoolkit")
		exit(0)
	if menu1 == "037":
		os.system("cd && cd routersploit && python3 rsf.py")
		exit(0)
	if menu1 == "047":
		os.system(" yersinia -h")
		exit(0)

	if selected == "8":
		os.system("clear")
		print(Fore.GREEN+f"╔╗ ╔╗        ╔╗  ╔════╗        ╔╗")
		print(Fore.GREEN+f"║║ ║║        ║║  ║╔╗╔╗║        ║║")
		print(Fore.GREEN+f"║╚═╝║╔══╗╔══╗║║╔╗╚╝║║╚╝╔══╗╔══╗║║ ╔══╗")
		print(Fore.GREEN+f"║╔═╗║║╔╗║║╔═╝║╚╝╝  ║║  ║╔╗║║╔╗║║║ ║══╣")
		print(Fore.GREEN+f"║║ ║║║╔╗║║╚═╗║╔╗╗  ║║  ║╚╝║║╚╝║║╚╗╠══║")
		print(Fore.GREEN+f"╚╝ ╚╝╚╝╚╝╚══╝╚╝╚╝  ╚╝  ╚══╝╚══╝╚═╝╚══╝{Style.RESET_ALL}")
		print(Fore.BLUE+f"                      a.k.a Kali Linux")
		print(Fore.BLUE+f"{Fore.BLUE}======================================")
		print(Fore.GREEN+f"{Style.RESET_ALL}Created By x11repo a.k.a Aqua")
		print(Fore.GREEN+f"{Style.RESET_ALL}Telegram: https://teleg.run/hacktools666")
		print(Fore.GREEN+f"{Style.RESET_ALL}Ver: 0.4.3.1 Alpha")
		print(Fore.BLUE+f"{Fore.BLUE}======================================")
		print(Fore.GREEN+f"{Style.RESET_ALL}{Fore.RED}[!]{Style.RESET_ALL} Перед использованием\n установите все репозитории!\n Для этого введите {Fore.GREEN}999")
		print(Fore.BLUE+f"======================================")
		print(Fore.GREEN+f"{Style.RESET_ALL}1. Information collection {Fore.GREEN}")
		print(Fore.GREEN+f"{Style.RESET_ALL}2. Vulnerability analysis")
		print(Fore.GREEN+f"{Style.RESET_ALL}3. Database evaluation")
		print(Fore.GREEN+f"{Style.RESET_ALL}4. Attack the password")
		print(Fore.GREEN+f"{Style.RESET_ALL}5. Wireless attacks")
		print(Fore.GREEN+f"{Style.RESET_ALL}6. Engineering analysis")
		print(Fore.GREEN+f"{Style.RESET_ALL}7. Operating tools")
		print(Fore.GREEN+f"{Style.RESET_ALL}8. Sniffing and spoofing")
		print(Fore.BLUE+f"          {Fore.YELLOW}018) Ettercap"+Style.RESET_ALL) #  ettercap -h
		print(Fore.YELLOW+f"          028) SSLstrip"+Style.RESET_ALL) ##   sslstrip -h
		print(Fore.YELLOW+f"          038) dsniff"+Style.RESET_ALL) ##   dsniff -h
		print(Fore.YELLOW+f"          048) Wireshark"+Style.RESET_ALL) ##   wireshark
		print(Fore.GREEN+f"{Style.RESET_ALL}9. Operation post")
		print(Fore.GREEN+f"{Style.RESET_ALL}10. Criminalystic")
		print(Fore.GREEN+f"{Style.RESET_ALL}11. Reporting tool")
		print(Fore.GREEN+f"{Style.RESET_ALL}12. Stress-testing")
		print(Fore.GREEN+f"{Style.RESET_ALL}13. System services")
		print(Fore.BLUE+f"====================================")
		print(Fore.GREEN+f"To update, enter '7777'")
		print(Fore.BLUE+f"====================================")
		
		menu1 = input("$ > ")

	if menu1 == "018":
		os.system(" ettercap -h")
		exit(0)
	if menu1 == "028":
		os.system(" sslstrip -h")
		exit(0)
	if menu1 == "038":
		os.system(" dsniff -h")
		exit(0)
	if menu1 == "048":
		os.system(" wireshark")
		exit(0)

	if selected == "9":
		os.system("clear")
		print(Fore.GREEN+f"╔╗ ╔╗        ╔╗  ╔════╗        ╔╗")
		print(Fore.GREEN+f"║║ ║║        ║║  ║╔╗╔╗║        ║║")
		print(Fore.GREEN+f"║╚═╝║╔══╗╔══╗║║╔╗╚╝║║╚╝╔══╗╔══╗║║ ╔══╗")
		print(Fore.GREEN+f"║╔═╗║║╔╗║║╔═╝║╚╝╝  ║║  ║╔╗║║╔╗║║║ ║══╣")
		print(Fore.GREEN+f"║║ ║║║╔╗║║╚═╗║╔╗╗  ║║  ║╚╝║║╚╝║║╚╗╠══║")
		print(Fore.GREEN+f"╚╝ ╚╝╚╝╚╝╚══╝╚╝╚╝  ╚╝  ╚══╝╚══╝╚═╝╚══╝{Style.RESET_ALL}")
		print(Fore.BLUE+f"                      a.k.a Kali Linux")
		print(Fore.BLUE+f"{Fore.BLUE}======================================")
		print(Fore.GREEN+f"{Style.RESET_ALL}Created By x11repo a.k.a Aqua")
		print(Fore.GREEN+f"{Style.RESET_ALL}Telegram: https://teleg.run/hacktools666")
		print(Fore.GREEN+f"{Style.RESET_ALL}Ver: 0.4.3.1 Alpha")
		print(Fore.BLUE+f"{Fore.BLUE}======================================")
		print(Fore.GREEN+f"{Style.RESET_ALL}{Fore.RED}[!]{Style.RESET_ALL} Перед использованием\n установите все репозитории!\n Для этого введите {Fore.GREEN}999")
		print(Fore.BLUE+f"======================================")
		print(Fore.GREEN+f"{Style.RESET_ALL}1. Information collection {Fore.GREEN}")
		print(Fore.GREEN+f"{Style.RESET_ALL}2. Vulnerability analysis")
		print(Fore.GREEN+f"{Style.RESET_ALL}3. Database evaluation")
		print(Fore.GREEN+f"{Style.RESET_ALL}4. Attack the password")
		print(Fore.GREEN+f"{Style.RESET_ALL}5. Wireless attacks")
		print(Fore.GREEN+f"{Style.RESET_ALL}6. Engineering analysis")
		print(Fore.GREEN+f"{Style.RESET_ALL}7. Operating tools")
		print(Fore.GREEN+f"{Style.RESET_ALL}8. Sniffing and spoofing")
		print(Fore.GREEN+f"{Style.RESET_ALL}9. Operation post")
		print(Fore.BLUE+f"          {Fore.YELLOW}019) dns2tcpd"+Style.RESET_ALL) #  dns2tcpd
		print(Fore.YELLOW+f"          029) sbd"+Style.RESET_ALL) ##   sbd
		print(Fore.YELLOW+f"          039) nghttpd"+Style.RESET_ALL) ##   nghttpd
		print(Fore.GREEN+f"{Style.RESET_ALL}10. Criminalystic")
		print(Fore.GREEN+f"{Style.RESET_ALL}11. Reporting tool")
		print(Fore.GREEN+f"{Style.RESET_ALL}12. Stress-testing")
		print(Fore.GREEN+f"{Style.RESET_ALL}13. System services")
		print(Fore.BLUE+f"====================================")
		print(Fore.GREEN+f"To update, enter '7777'")
		print(Fore.BLUE+f"====================================")
		
		menu1 = input("$ > ")

	if menu1 == "019":
		os.system(" dns2tcpd")
		exit(0)
	if menu1 == "029":
		os.system(" sbd")
		exit(0)
	if menu1 == "039":
		os.system(" nghttpd")
		exit(0)

	if selected == "10":	
		os.system("clear")
		print(Fore.GREEN+f"╔╗ ╔╗        ╔╗  ╔════╗        ╔╗")
		print(Fore.GREEN+f"║║ ║║        ║║  ║╔╗╔╗║        ║║")
		print(Fore.GREEN+f"║╚═╝║╔══╗╔══╗║║╔╗╚╝║║╚╝╔══╗╔══╗║║ ╔══╗")
		print(Fore.GREEN+f"║╔═╗║║╔╗║║╔═╝║╚╝╝  ║║  ║╔╗║║╔╗║║║ ║══╣")
		print(Fore.GREEN+f"║║ ║║║╔╗║║╚═╗║╔╗╗  ║║  ║╚╝║║╚╝║║╚╗╠══║")
		print(Fore.GREEN+f"╚╝ ╚╝╚╝╚╝╚══╝╚╝╚╝  ╚╝  ╚══╝╚══╝╚═╝╚══╝{Style.RESET_ALL}")
		print(Fore.BLUE+f"                      a.k.a Kali Linux")
		print(Fore.BLUE+f"{Fore.BLUE}======================================")
		print(Fore.GREEN+f"{Style.RESET_ALL}Created By x11repo a.k.a Aqua")
		print(Fore.GREEN+f"{Style.RESET_ALL}Telegram: https://teleg.run/hacktools666")
		print(Fore.GREEN+f"{Style.RESET_ALL}Ver: 0.4.3.1 Alpha")
		print(Fore.BLUE+f"{Fore.BLUE}======================================")
		print(Fore.GREEN+f"{Style.RESET_ALL}{Fore.RED}[!]{Style.RESET_ALL} Перед использованием\n установите все репозитории!\n Для этого введите {Fore.GREEN}999")
		print(Fore.BLUE+f"======================================")
		print(Fore.GREEN+f"{Style.RESET_ALL}1. Information collection {Fore.GREEN}")
		print(Fore.GREEN+f"{Style.RESET_ALL}2. Vulnerability analysis")
		print(Fore.GREEN+f"{Style.RESET_ALL}3. Database evaluation")
		print(Fore.GREEN+f"{Style.RESET_ALL}4. Attack the password")
		print(Fore.GREEN+f"{Style.RESET_ALL}5. Wireless attacks")
		print(Fore.GREEN+f"{Style.RESET_ALL}6. Engineering analysis")
		print(Fore.GREEN+f"{Style.RESET_ALL}7. Operating tools")
		print(Fore.GREEN+f"{Style.RESET_ALL}8. Sniffing and spoofing")
		print(Fore.GREEN+f"{Style.RESET_ALL}9. Operation post")
		print(Fore.GREEN+f"{Style.RESET_ALL}10. Criminalystic")
		print(Fore.BLUE+f"          {Fore.YELLOW}0110) kDiff3"+Style.RESET_ALL) #  kdiff3
		print(Fore.YELLOW+f"          0210) p0f"+Style.RESET_ALL) ##   p0f
		print(Fore.YELLOW+f"          0310) xPdf"+Style.RESET_ALL) ##   xpdf
		print(Fore.YELLOW+f"          0410) exiftool"+Style.RESET_ALL) ##   exiftool
		print(Fore.GREEN+f"{Style.RESET_ALL}11. Reporting tool")
		print(Fore.GREEN+f"{Style.RESET_ALL}12. Stress-testing")
		print(Fore.GREEN+f"{Style.RESET_ALL}13. System services")
		print(Fore.BLUE+f"====================================")
		print(Fore.GREEN+f"To update, enter '7777'")
		print(Fore.BLUE+f"====================================")

		menu1 = input("$ > ")

	if menu1 == "0110":
		os.system(" kdiff3")
		exit(0)
	if menu1 == "0210":
		os.system(" p0f")
		exit(0)
	if menu1 == "0310":
		os.system(" xpdf")
		exit(0)
	if menu1 == "0410":
		os.system(" exiftool")
		exit(0)

	if selected == "11":
		os.system("clear")
		print(Fore.GREEN+f"╔╗ ╔╗        ╔╗  ╔════╗        ╔╗")
		print(Fore.GREEN+f"║║ ║║        ║║  ║╔╗╔╗║        ║║")
		print(Fore.GREEN+f"║╚═╝║╔══╗╔══╗║║╔╗╚╝║║╚╝╔══╗╔══╗║║ ╔══╗")
		print(Fore.GREEN+f"║╔═╗║║╔╗║║╔═╝║╚╝╝  ║║  ║╔╗║║╔╗║║║ ║══╣")
		print(Fore.GREEN+f"║║ ║║║╔╗║║╚═╗║╔╗╗  ║║  ║╚╝║║╚╝║║╚╗╠══║")
		print(Fore.GREEN+f"╚╝ ╚╝╚╝╚╝╚══╝╚╝╚╝  ╚╝  ╚══╝╚══╝╚═╝╚══╝{Style.RESET_ALL}")
		print(Fore.BLUE+f"                      a.k.a Kali Linux")
		print(Fore.BLUE+f"{Fore.BLUE}======================================")
		print(Fore.GREEN+f"{Style.RESET_ALL}Created By x11repo a.k.a Aqua")
		print(Fore.GREEN+f"{Style.RESET_ALL}Telegram: https://teleg.run/hacktools666")
		print(Fore.GREEN+f"{Style.RESET_ALL}Ver: 0.4.3.1 Alpha")
		print(Fore.BLUE+f"{Fore.BLUE}======================================")
		print(Fore.GREEN+f"{Style.RESET_ALL}{Fore.RED}[!]{Style.RESET_ALL} Перед использованием\n установите все репозитории!\n Для этого введите {Fore.GREEN}999")
		print(Fore.BLUE+f"======================================")
		print(Fore.GREEN+f"{Style.RESET_ALL}1. Information collection {Fore.GREEN}")
		print(Fore.GREEN+f"{Style.RESET_ALL}2. Vulnerability analysis")
		print(Fore.GREEN+f"{Style.RESET_ALL}3. Database evaluation")
		print(Fore.GREEN+f"{Style.RESET_ALL}4. Attack the password")
		print(Fore.GREEN+f"{Style.RESET_ALL}5. Wireless attacks")
		print(Fore.GREEN+f"{Style.RESET_ALL}6. Engineering analysis")
		print(Fore.GREEN+f"{Style.RESET_ALL}7. Operating tools")
		print(Fore.GREEN+f"{Style.RESET_ALL}8. Sniffing and spoofing")
		print(Fore.GREEN+f"{Style.RESET_ALL}9. Operation post")
		print(Fore.GREEN+f"{Style.RESET_ALL}10. Criminalystic")
		print(Fore.GREEN+f"{Style.RESET_ALL}11. Reporting tool")
		print(Fore.BLUE+f"          {Fore.YELLOW}0111) cherrytree"+Style.RESET_ALL) #  cherrytree
		print(Fore.YELLOW+f"          0211) xrdp"+Style.RESET_ALL) ##   xrdp -h
		print(Fore.YELLOW+f"          0311) aircrack-ng"+Style.RESET_ALL) ##  aircrack-ng --help
		print(Fore.YELLOW+f"          0411) ardour5"+Style.RESET_ALL) ##   ardour5
		print(Fore.GREEN+f"{Style.RESET_ALL}12. Stress-testing")
		print(Fore.GREEN+f"{Style.RESET_ALL}13. System services")
		print(Fore.BLUE+f"====================================")
		print(Fore.GREEN+f"To update, enter '7777'")
		print(Fore.BLUE+f"====================================")

		menu1 = input("$ > ")
	
	if menu1 == "0111":
		os.system(" cherrytree")
		exit(0)
	if menu1 == "0211":
		os.system(" xrdp -h")
		exit(0)
	if menu1 == "0311":
		os.system(" aircrack-ng --help")
		exit(0)
	if menu1 == "0411":
		os.system(" ardour5")
		exit(0)

	if selected == "12":
		os.system("clear")
		print(Fore.GREEN+f"╔╗ ╔╗        ╔╗  ╔════╗        ╔╗")
		print(Fore.GREEN+f"║║ ║║        ║║  ║╔╗╔╗║        ║║")
		print(Fore.GREEN+f"║╚═╝║╔══╗╔══╗║║╔╗╚╝║║╚╝╔══╗╔══╗║║ ╔══╗")
		print(Fore.GREEN+f"║╔═╗║║╔╗║║╔═╝║╚╝╝  ║║  ║╔╗║║╔╗║║║ ║══╣")
		print(Fore.GREEN+f"║║ ║║║╔╗║║╚═╗║╔╗╗  ║║  ║╚╝║║╚╝║║╚╗╠══║")
		print(Fore.GREEN+f"╚╝ ╚╝╚╝╚╝╚══╝╚╝╚╝  ╚╝  ╚══╝╚══╝╚═╝╚══╝{Style.RESET_ALL}")
		print(Fore.BLUE+f"                      a.k.a Kali Linux")
		print(Fore.BLUE+f"{Fore.BLUE}======================================")
		print(Fore.GREEN+f"{Style.RESET_ALL}Created By x11repo a.k.a Aqua")
		print(Fore.GREEN+f"{Style.RESET_ALL}Telegram: https://teleg.run/hacktools666")
		print(Fore.GREEN+f"{Style.RESET_ALL}Ver: 0.4.3.1 Alpha")
		print(Fore.BLUE+f"{Fore.BLUE}======================================")
		print(Fore.GREEN+f"{Style.RESET_ALL}{Fore.RED}[!]{Style.RESET_ALL} Перед использованием\n установите все репозитории!\n Для этого введите {Fore.GREEN}999")
		print(Fore.BLUE+f"======================================")
		print(Fore.GREEN+f"{Style.RESET_ALL}1. Information collection {Fore.GREEN}")
		print(Fore.GREEN+f"{Style.RESET_ALL}2. Vulnerability analysis")
		print(Fore.GREEN+f"{Style.RESET_ALL}3. Database evaluation")
		print(Fore.GREEN+f"{Style.RESET_ALL}4. Attack the password")
		print(Fore.GREEN+f"{Style.RESET_ALL}5. Wireless attacks")
		print(Fore.GREEN+f"{Style.RESET_ALL}6. Engineering analysis")
		print(Fore.GREEN+f"{Style.RESET_ALL}7. Operating tools")
		print(Fore.GREEN+f"{Style.RESET_ALL}8. Sniffing and spoofing")
		print(Fore.GREEN+f"{Style.RESET_ALL}9. Operation post")
		print(Fore.GREEN+f"{Style.RESET_ALL}10. Criminalystic")
		print(Fore.GREEN+f"{Style.RESET_ALL}11. Reporting tool")
		print(Fore.GREEN+f"{Style.RESET_ALL}12. Stress-testing")
		print(Fore.BLUE+f"          {Fore.YELLOW}0112) dhcpig"+Style.RESET_ALL) #  dhcpig
		print(Fore.YELLOW+f"          0212) t50"+Style.RESET_ALL) ##   t50 -h
		print(Fore.YELLOW+f"          0312) terminAtOr"+Style.RESET_ALL) ##   terminator
		print(Fore.YELLOW+f"          0412) terminEtEr"+Style.RESET_ALL) ##   termineter
		print(Fore.GREEN+f"{Style.RESET_ALL}13. System services")
		print(Fore.BLUE+f"====================================")
		print(Fore.GREEN+f"To update, enter '7777'")
		print(Fore.BLUE+f"====================================")
	
		menu1 = input("$ > ")

	if menu1 == "0112":
		os.system(" dhcpig")
		exit(0)
	if menu1 == "0212":
		os.system(" t50 -h")
		exit(0)
	if menu1 == "0312":
		os.system(" terminator")
		exit(0)
	if menu1 == "0412":
		os.system(" termineter")
		exit(0)

	if selected == "13":
		print("none, sorry.")
		time.sleep(3)
		exit(0)

	if(not menu1.startswith("0")):
		# главные меню
		menu(menu1)
	else:
		# подменю
		time.sleep(1)
		menu(selected)

	return

menu()
