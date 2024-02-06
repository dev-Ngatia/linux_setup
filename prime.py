import os

#Connect Wifi
os.system('nmcli d wifi connect strathmore password 5trathm0re')
os.system('nmcli d wifi connect Thind-5 password *321@ignawMS*')
os.system('nmcli d wifi connect "Eliezer Faiba" password Africa@2023')
os.system('nmcli d wifi connect Julie password JMariera@123')
os.system('echo " "')
os.system('echo "=============================================== "')
os.system('echo " "')
os.system('echo "Wifi Connected"')
os.system('echo " "')
os.system('echo "=============================================== "')
os.system('echo " "')
os.system('ip addr')

os.system('echo " "')
os.system('echo "=============================================== "')
os.system('echo " "')


#Update apt
os.system('sudo apt update')
os.system('echo "=============================================== "')
os.system('sudo apt upgrade')
os.system('echo " "')
os.system('echo "=============================================== "')
os.system('echo " "')


#Install Curl
os.system('sudo apt install curl')
os.system('echo "=============================================== "')
os.system('curl --version')
os.system('echo " "')
os.system('echo "=============================================== "')
os.system('echo " "')





#Install pywhatkit
os.system('pip install pywhatkit') 
os.system('echo " "')
os.system('echo "=============================================== "')
os.system('echo " "')


#Install VS Code
os.system('ctrl + shift + n')
os.system('sudo apt install software-properties-common apt-transport-https wget -y')
os.system('echo "=============================================== "')
os.system('wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -')
os.system('echo "=============================================== "')
os.system('sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"')
os.system('echo "=============================================== "')
os.system('sudo apt install code')
os.system('echo "=============================================== "')
os.system('code --version')
os.system('echo " "')
os.system('echo "=============================================== "')
os.system('echo " "')




#Install GIT
os.system('ctrl + shift + n')
os.system('sudo apt install git')

os.system('echo "=============================================== "')
os.system('git --version')

os.system('echo "=============================================== "')
os.system('git config --global user.name "Dev-Ngatia"')

os.system('echo "=============================================== "')
os.system('git config --global user.email "ngatia3223@gmail.com"')
os.system('echo " "')
os.system('echo "=============================================== "')
os.system('echo " "')



"""#os.system('/usr/bin/msfpc elf bind eth0 4444')
#os.system('python2 -m SimpleHTTPServer 8080')
os.system('echo " "')
os.system('echo "=============================================== "')
os.system('echo " "')"""
