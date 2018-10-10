import threading
import telnetlib
import time

TIMEOUT = 1

hostList = list()
hostList.append("s.jpush.cn")
hostList.append("im.jpush.cn")
hostList.append("stats.jpush.cn")


portList = list()
portList.append("19000")

for i in range(3000, 3021, 1):
    portList.append(str(i))

for i in range(7000, 7021, 1):
    portList.append(str(i))

for i in range(8000, 8021, 1):
    portList.append(str(i))


def telnetFunc(host, port):
    try:
        tn.open(host, port, TIMEOUT)
        print(host, port," ok")
    except BaseException as e:
        pass

threadList = []
for host in hostList:
    for port in portList:
        tn = telnetlib.Telnet()
        thread = threading.Thread(target=telnetFunc, args=(host, port))
        thread.start()
        threadList.append(thread)


for t in threadList:
    t.join()
