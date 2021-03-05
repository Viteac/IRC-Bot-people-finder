import socket
import sys
import time
import os
import subprocess
import json
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('1. Freenode\n2.Dalnet')

choice = input('What network?\n> ')
if choice == '1':
    HOST = 'chat.freenode.net'
    file_name = 'f'
else:
    HOST = 'irc.dal.net'
    file_name = 'd'

#HOST = 'irc.dal.net'
PORT = 6667
nick = "ratouolxsss"
NICK = 'Bira'
CHANNEL = '#pronhj'
s.connect((HOST, PORT))
s.send(bytes("NICK " + nick + "\r\n", 'UTF-8'))
s.send(bytes("USER " + nick + " " + nick + " " + nick + " :" + nick + "\r\n", 'UTF-8'))
s.send(bytes("JOIN " + CHANNEL + "\r\n", "UTF-8"))
print('-----------------')

# time.sleep(60)
imina = []

odczyt = s.makefile(mode='rw', buffering=1, encoding='utf-8', newline='\r\n')
s.send(bytes("NAMES " + CHANNEL + "\r\n", "UTF-8"))
for line in odczyt:
    if line.split()[1] == '353':
        print('Checked Whois >>>>>>', line)
        od = line
        w = od.find(':', 1)

        a = od[w + 1:].split()

        for i in a:
            if i[0] in ['@', '&', '+']:
                ind = a.index(i)
                a[ind] = i[1:]
            imina.append(i)
        break

print('W pokoju:')
for i in imina:
    print(i)

users = {}

# with open('freenode_users.txt', 'a') as f:
#     save = f.writelines()
# save = open('freenode_users.txt', 'a')
co = 0
for i in imina:

    print(i)
    s.send(bytes("WHOIS " + i + "\r\n", "UTF-8"))

print(imina)
for x, y in users.items():
    print(x, y)


while 1:
    for line in odczyt:
        line = line.strip()
        #print('>>', line)
        if '311' in line:
            print('tu>>>>>>>>', line)
            m = line.split()
            # print('>>>>>>', m)
            ip = m[5]
            us = m[3]
            hostname = m[4]
            r = line.find(':', 1)
            real = line[r + 1:]
            cet = 'geoiplookup ' + ip
            komenda = subprocess.check_output(cet, shell=True).decode('UTF-8')


            country = ' '.join(komenda.split()[4:])
            # country = komenda.split()[4:]
            if country == 'resolve':
                country = 'Unknown'

            print(f'User: {us}, IP: {ip},Country: {country}, Hostname: {hostname}, RealName: {real}')
            free = f'User: {us}, IP: {ip},Country: {country}, Hostname: {hostname}, RealName: {real}\n'
            users[us] = {'User': us, 'IP': ip, 'Hostname': hostname, 'Country': country, 'Realname': real}
            with open('freenode_users.txt', 'a') as f:
                f.write(free)

        print(type(users))
        print(users)
        # file_name = 'd'
        jason = json.dumps(users)
        f = open(file_name + ".json", "w")
        f.write(jason)
        f.close()
        if 'PING :' in line:
            print('Found', line)
            s.send(bytes('PONG ' + line.split()[1] + '\r\n', 'UTF-8'))
