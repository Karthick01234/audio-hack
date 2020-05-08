import os
tgreen = '\033[32m'
print( tgreen + "installing dependencies")
os.system("apt install curl")
os.system("apt install wget")
os.system("apt install unzip")
os.system("apt install php")
os.system("termux-setup-storage")
os.system("mkdir /sdcard/audiohack")
os.system("mv index.html /sdcard/audiohack && mv save.php /sdcard/audiohack && mv jquery.js /sdcard/audiohack && mv k.gif /sdcard/audiohack")
os.system("mkdir /sdcard/audiohack/voice")
os.system("chmod +x start.sh")
print(" ")
print("Now start the tool by using command ./start.sh")