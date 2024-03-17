import socket
import time

def Activate():
    HOST = "169.254.37.182" # The UR IP address
    PORT = 30002 # UR secondary client
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    f_activate = open ("C:/Users/Prajwal/Python Projects/ADVA LED/UR5 RTDE/ur_rtde/Gripperactivate.script", "rb")
    l_activate = f_activate.read(1024)
    while (l_activate):
        s.send(l_activate)
        l_activate = f_activate.read(1024)
    s.close()
    
def Open():
    HOST = "169.254.37.182" # The UR IP address
    PORT = 30002 # UR secondary client
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    f_open = open ("C:/Users/Prajwal/Python Projects/ADVA LED/UR5 RTDE/ur_rtde/Gripperopen.script", "rb")
    l_open = f_open.read(1024)
    while (l_open):
        s.send(l_open)
        l_open = f_open.read(1024)
    s.close()

def Close():
    HOST = "169.254.37.182" # The UR IP address
    PORT = 30002 # UR secondary client
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    f_close = open ("C:/Users/Prajwal/Python Projects/ADVA LED/UR5 RTDE/ur_rtde/Gripperclose.script", "rb")
    l_close = f_close.read(1024)
    while (l_close):
        s.send(l_close)
        l_close = f_close.read(1024)
    s.close()
def reset():
    HOST = "169.254.37.182" # The UR IP address
    PORT = 30002 # UR secondary client
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    f_reset = open ("C:/Users/Prajwal/Python Projects/ADVA LED/UR5 RTDE/ur_rtde/Gripperreset.script", "rb")
    l_reset = f_reset.read(1024)
    while (l_reset):
        s.send(l_reset)
        l_reset = f_reset.read(1024)
    s.close()
def cw():
    HOST = "169.254.37.182" # The UR IP address
    PORT = 30002 # UR secondary client
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    f_cw = open ("C:/Users/Prajwal/Python Projects/ADVA LED/UR5 RTDE/ur_rtde/Gripper.script", "rb")
    print(f_cw)
    l_cw = f_cw.read(1024)
    print(l_cw)
    while (l_cw):
        s.send(l_cw)
        l_cw = f_cw.read(1024)
    s.close()
    