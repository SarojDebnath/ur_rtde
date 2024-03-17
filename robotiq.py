import socket
import time

file="C:/Users/sarojd/Eva/HAL/Gripper.script" #Destination to the .script file
##################################
#Commands to control it:
#  rq_reset ()
#  rq_activate_and_wait ()
#  rq_set_speed_norm (100)
#  rq_set_force_norm (100)
#  rq_open_and_wait ()
#  rq_close()
#  rq_close_and_wait ()
#  rq_open()
#  rq_is_object_detected ()
#  rq_move_and_wait_norm (75)
#  rq_current_pos_norm ()
#  rq_current_pos_mm ()
#  rq_current_pos_inches ()
#  rq_move_and_wait_mm (50)
#  rq_current_pos_inches (1)
#  rq_move(127,gripper_socket="1")
################################################################

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

def Activate():
    HOST = "192.168.1.111" # The UR IP address
    PORT = 30002 # UR secondary client
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    command='   rq_activate_and_wait()\n'
    replace_line(file,2374,command)
    f_activate = open (file, "rb")
    l_activate = f_activate.read(1024)
    while (l_activate):
        s.send(l_activate)
        l_activate = f_activate.read(1024)
    s.close()
    
def Open():
    HOST = "192.168.1.111" # The UR IP address
    PORT = 30002 # UR secondary client
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    command='   rq_open()\n'
    replace_line(file,2374,command)
    f_open = open (file, "rb")
    l_open = f_open.read(1024)
    while (l_open):
        s.send(l_open)
        l_open = f_open.read(1024)
    s.close()
###############################################Needed to be edited
def Close():
    HOST = "192.168.1.111" # The UR IP address
    PORT = 30002 # UR secondary client
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    command='   rq_close()\n'
    replace_line(file,2374,command)
    f_close = open (file, "rb")
    l_close = f_close.read(1024)
    while (l_close):
        s.send(l_close)
        l_close = f_close.read(1024)
    s.close()
def reset():
    HOST = "192.168.1.111" # The UR IP address
    PORT = 30002 # UR secondary client
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    command='   rq_reset()\n'
    replace_line(file,2374,command)
    f_reset = open (file, "rb")
    l_reset = f_reset.read(1024)
    while (l_reset):
        s.send(l_reset)
        l_reset = f_reset.read(1024)
    s.close()
def move(n):
    HOST = "169.254.240.99" # The UR IP address
    PORT = 30002 # UR secondary client
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    i=int(int(n)*255/100)
    pos=f'rq_move({i},gripper_socket="1")'
    command=f'   {pos}\n'
    replace_line(file,2374,command)
    f_cw = open (file, "rb")
    l_cw = f_cw.read(1024)
    while (l_cw):
        s.send(l_cw)
        l_cw = f_cw.read(1024)
    s.close()
    