# This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.
import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host='172.17.2.87'
portlist=[21,22,23,25,53,80,110,143,3389,5631]
r=0
def greeting():
    global backup
    global portlist
    global host
    global r
    q=input("Check a different IP? y/n")
    if q=='y':
        e=str(input("What IP?"))
        if e not in host:
            host=e
    elif q=='n':
        pass
    else:
        greeting()
    w=input("Check more ports? y/n")
    if w=="y":
        while True:
            try:
                r=int(input("What port? (if done type a letter)"))
                if r not in portlist:
                    portlist.append(r)
                    backup=portlist
            except:
                break
    elif w=='n':
        pass
    else:
        greeting()

def checker():
    global backup
    global s
    global portlist
    global host
    while portlist:
        s.close()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((host,portlist[0]))
            print(str(portlist[0])+' is open')
            del portlist[0]
        except (ConnectionRefusedError,TimeoutError):
            del portlist[0]

greeting()
checker()