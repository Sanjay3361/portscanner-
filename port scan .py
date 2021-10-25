#! /usr/bin/python3
'''basic port scanner based on python '''
#  some build in module ..                  
import queue 
import socket
import threading
from queue import Queue

target =input("Type IP Address  : ") # take ip address from the user 
goal = input("how many port you want to scan : ") 
# limite those written in range function ..
queue=Queue()
port_open =[] # port will assign here when it find a port ..

def portscan(port): 
    try:
        sock =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((target,port))
        return True
    except:
        return False # in some of a condition.  (reason most of a ip has some open port  of atleat one )

def port_queue(port_list):
    for port in port_list:
        queue.put(port)

def network():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Port {} is open.".format(port))
            port_open.append(port)

port_list = range(1,1000)#it will  scan from one. at there where use was specified.
port_queue(port_list)

thread_list=[]

for r in range(250):
    thread =threading.Thread(target=network)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print(" In  ip port open are   : ",port_open) # port_open whether the ip port are open or..
exit()
