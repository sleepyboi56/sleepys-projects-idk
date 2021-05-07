
#access files remotely
# * Gain access to different directories
# * View Files
# * Download Files
# * Remove Files
# * Remove Directories
# * Send Files 
# * Create Directory

#shut down remotely

import os
import socket

s = socket.socket()
host = socket.gethostname()
port = 9999
s.bind((host,port))
print("")
print(" Server is currently running @ ", host)
print(" Waiting for any incoming connections... ")
s.listen(1)
conn, addr = s.accept()
print("")
print(addr, "Has connected to the server succesfully ")

# connection has been completed

# command handling

while 1:
    print("")
    command = input(str("Command >> "))
    if command == "view_cwd":
        conn.send(command.encode())
        print("")
        print(" Command sent waiting for execution... ")
        print("")
        files = conn.recv(5000)
        files = files.decode()
        print("Command output : ", files)
        
    elif command == "custom_dir":
        conn.send(command.encode())
        print("")
        user_input = input(str("Custom Dir : "))
        conn.send(user_input.encode())
        print("")
        print("Command has been sent")
        print("")
        files = conn.recv(5000)
        files = files.decode()
        print("Custom Dir Results : ", files)

    elif command == "download_files":
        conn.send(command.encode())
        print("")
        filepath = input(str("Please enter the file path including the filename : "))
        conn.send(filepath.encode())
        file = conn.recv(100000)
        print("")
        filename = input(str("Please enter a filename for the incoming file including the extension : "))
        new_file = open(filename, "wb")
        new_file.write(file)
        new_file.close()
        print("")
        print(filename, " Has been downloaded and saved ")
        print("")

    elif command == "remove_files":
        conn.send(command.encode())
        fileanddir = input(str("Please enter the filename and directory : "))
        conn.send(fileanddir.encode())
        print("")
        print(" Command has been executed successfully : File Removed ")

    elif command == "send_files":
        conn.send(command.encode())
        file = input(str("Please enter the filename and directory of the file : "))
        filename = input(str("Please enter the filename for the file being sent : "))
        data = open(file, "rb")
        file_data = data.read(7000) #change when file is too big
        conn.send(filename.encode()) 
        print(file, "Has been sent successfully")  
        conn.send(file_data)     
    
    elif command == "shutdown":
        conn.send(command.encode())

    else:
        print("")
        print("Command not recognized")
