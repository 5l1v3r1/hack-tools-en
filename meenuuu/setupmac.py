 # -*- coding: utf-8 -*-
import os
import time
from time import sleep
from colorama import Fore, Back, Style
print(Fore.BLUE+f"\n========================================================="+Style.RESET_ALL)
print("[INFO] You can minimize the terminal and go watch cartoons ...")
print("Because it will take a long time.")
print(Fore.BLUE+f"========================================================= "+ Style.RESET_ALL)
print(Fore.WHITE+f"{Back.RED}\nBut it’s better to monitor the installation, as it will ask for confirmation when cloning."+Style.RESET_ALL)
time.sleep(8)
os.system("brew update")
os.system("brew install git")
os.system("brew install python")
os.system("brew install python2")
os.system("brew install wget")
os.system("brew install nmap")
os.system("brew install hydra ")
os.system("cd && git clone https://github.com/sqlmapproject/sqlmap.git")
os.system("cd")
os.system("brew install wget")
os.system("cd && wget https://Auxilus.github.io/metasploit.sh")
os.system("cd && bash metasploit.sh")
os.system("cd && cd metasploit-framework")
os.system("cd && gem install bundle --pre")
os.system("cd && bundle config build.nokogiri --use-system-libraries")
os.system("cd && bundle install")
os.system("cd")
os.system("cd && git clone https://github.com/ihebski/angryFuzzer.git")
os.system("cd && cd angryFuzzer")
os.system("cd && pip2 install -r requirements.txt")
os.system("cd && pip2 install requests")
os.system("cd")
os.system("brew install php")
os.system("cd && git clone https://github.com/Tuhinshubhra/RED_HAWK")
os.system("cd")
os.system("cd && git clone https://github.com/evait-security/weeman.git")
os.system("cd && cd weeman")
os.system("cd && chmod +x weeman.py")
os.system("cd")
os.system("cd && git clone https://github.com/maldevel/IPGeoLocation.git")
os.system("cd && cd IPGeoLocation")
os.system("cd && pip install -r requirements.txt")
os.system("cd")
os.system("cd && git clone https://github.com/Mebus/cupp.git")
os.system("brew install -y python")
os.system("brew install -y nano")
os.system("pip install requests")
os.system("cd && git clone https://github.com/reverse-shell/routersploit.git")
os.system("cd && cd routersploit")
os.system("pip2 install -r requirements.txt")
os.system("pip2 install -r requirements-dev.txt")
os.system("pip2 install -r requests")
os.system("cd && brew install p0f") ### 1 пункт
os.system("cd && brew install arp-scan") ### sudo arp-scan
os.system("cd && brew install cutycapt") ## sudo cutycapt
os.system("cd && brew install python-elixir python-qt4 xsltproc")
os.system("cd && git clone https://github.com/secforce/sparta.git") ## python sparta.py
os.system("cd && git clone https://github.com/golismero/golismero.git") ## python golismero.py
os.system("cd && brew install masscan") ## masscan
os.system("cd && wget https://github.com/`curl -s https://github.com/ron190/jsql-injection/releases | grep -E -o '/ron190/jsql-injection/releases/download/v[0-9]{1,2}.[0-9]{1,2}/jsql-injection-v[0-9]{1,2}.[0-9]{1,2}.jar' | head -n 1`") ## java -jar ./jsql-injection-v*.jar
os.system("cd && brew install openvas") #### 2 punkt ## openvas-start
os.system("cd && git clone https://github.com/SpiderLabs/jboss-autopwn.git") ## ./e2.sh ## 3 punkt
os.system("cd && brew install dirb") ## dirb
os.system("cd && git clone https://github.com/iniqua/plecost.git && cd plecost && chmod +x * && python3 setup.py install") ##plecost
os.system("cd && gem install wpscan && wpscan --update --disable-tls-checks") ## wpscan
os.system("cd && git clone https://github.com/epsylon/xsser.git && cd && cd xsser && sudo python3 setup.py install && sudo apt install python3-pycurl python3-bs4 python3-geoip python3-geoip2 python3-gi python3-cairocffi python3-selenium firefoxdriver && sudo pip3 install pycurl bs4 geoip2 gobject cairocffi selenium") ## xsser
os.system("cd &&  apt install crunch") ## 4 punkt ## crunch
## hashcat -- cd hack-tools-en/assets/hashcat/ && ./hashcat64.bin --help
os.system("cd && wget http://www.openwall.com/john/g/john-1.7.9.tar.bz2 && wget http://www.openwall.com/john/g/john-1.7.9.tar.bz2.sign && wget http://www.openwall.com/signatures/openwall-signatures.asc && pgp -ka openwall-signatures.asc && pgp john-1.7.9.tar.bz2.sign john-1.7.9.tar.bz2 && sudo apt install john") ## john
os.system("cd && brew install ncrack") ## ncrack
os.system("cd && brew install aircrack-ng")## 5 punkt ## aircrack-ng
os.system("cd && brew install git build-essential libssl-dev libpcap-dev && git clone https://github.com/joswr1ght/asleap && cd && cd asleap-2.2 && make")## cd asleap-2.2 && ./asleap
os.system("cd && brew install libpcap-dev && wget http://www.willhackforsushi.com/code/cowpatty/4.6/cowpatty-4.6.tgz && tar xvzf cowpatty-*.tgz && cd cowpatty-4.6 && make && sudo make install")### cd cowpatty-4.6 && ./cowpatty
os.system("cd && brew install mdk3") ## sudo mdk3
os.system("cd && brew install reaver") ## sudo reaver
os.system("cd && brew install wifite") ## sudo wifite
os.system("cd && brew install yara") ## 6 punkt ## sudo yara
os.system("cd && curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall") ## 7 punkt
###!!!! НАДО ДОБАВИТЬ МЕТАСПЛОИТ И АРМИТАЖ !!!!###
os.system("cd && git clone https://github.com/trustedsec/social-engineer-toolkit/ set/ && cd && cd set && chmod +x * && sudo python setup.py") ## setoolkit
os.system("cd && apt install python3-pip && git clone https://www.github.com/threat9/routersploit && cd routersploit && python3 -m pip install -r requirements.txt") ## cd routersploit && python3 rsf.py
os.system("cd && brew install yersinia") ##sudo yersinia -h
os.system("cd && brew install ettercap-graphical")## 8 punkt ## sudo ettercap -h
os.system("cd && brew install sslstrip") ## sudo sslstrip -h
os.system("cd && brew install dsniff") ## sudo dsniff -h
os.system("cd && brew install wireshark") ## sudo wireshark
os.system("cd && brew install dns2tcp") ## 9 punkt ## sudo dns2tcpd
os.system("cd && brew install sbd") ## sudo sbd
os.system("cd && brew install nghttp2") ## sudo nghttpd
os.system("cd && brew install kdiff3")## 10 punkt ## sudo kdiff3 
############## p
os.system("cd && brew install xpdf") ## sudo xpdf
os.system("cd && brew install libimage-exiftool-perl") ## sudo exiftool
os.system("cd && brew install cherrytree")## 11 punkt ## sudo cherrytree
os.system("cd && brew install xrdp && sudo systemctl enable xrdp") ## sudo xrdp -h
############## ack-ng --help
os.system("cd && brew install ardour") ## sudo ardour5
os.system("cd && brew install dhcpig") ##12 punkt ## sudo dhcpig
os.system("cd && brew install t50") ## sudo t50 -h
os.system("cd && brew install terminator") ## sudo terminator
os.system("cd && brew install thc-ipv6") ## больше не поддерживается
os.system("cd && brew install python3-crcelk python3-pluginbase python3-pyasn1 python3-serial python3-smoke-zephyr python3-tabulate python3-termcolor && sudo pip3 install termineter")
############## sudo termineter
os.system("cd && brew install hashcat")
