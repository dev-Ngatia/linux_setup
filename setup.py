"""Available Apps Include:"""

import os

#curl
#xdotool
#pyautogui
#edge
#xdm
#git
#vs code pending


#Install Edge
"""
os.system('curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg')
os.system('echo "=============================================== "')
os.system('sudo install -o root -g root -m 644 microsoft.gpg /etc/apt/trusted.gpg.d/')
os.system('echo "=============================================== "')
os.system('sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/edge stable main" > /etc/apt sources.list.d/microsoft-edge-dev.list'')
os.system('echo "=============================================== "')
os.system('sudo apt update && sudo apt install microsoft-edge-stable')
os.system('echo " "')
os.system('echo "=============================================== "')
os.system('echo " "')
"""

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



#Install xdotool
os.system('sudo apt-get install xdotool')
#os.system('ctrl + shift + n')

os.system('echo " "')
os.system('echo "=============================================== "')
os.system('echo " "')






#Install XDM
os.system('sudo ./install.sh')
os.system('echo " "')
os.system('echo "=============================================== "')
os.system('echo " "')
