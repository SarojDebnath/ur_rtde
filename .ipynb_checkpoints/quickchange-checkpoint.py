import socket
import time

file="C:/Users/sarojd/Vision_Arsenal/ur_rtde/TF_bier.script" #Destination to the .script file

def Activate():
    HOST = "192.168.1.111" # The UR IP address
    PORT = 30002 # UR secondary client
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    f_activate = open ('C:/Users/sarojd/Vision_Arsenal/ur_rtde/TF_bier.script', "rb")
    l_activate = f_activate.read(1024)
    while (l_activate):
        s.send(l_activate)
        l_activate = f_activate.read(1024)
    s.close()
Activate()