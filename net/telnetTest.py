import telnetlib

TIMEOUT = 1

hostList = list()
hostList.append("10.21.25.234")
hostList.append("s.jpush.cn")
hostList.append("im.jpush.cn")
hostList.append("stats.jpush.cn")


portList = list()
portList.append("1433")
portList.append("19000")
portList.append("3000")
portList.append("7000")
portList.append("8000")
portList.append("6379")

for host in hostList:
    for port in portList:
        tn = telnetlib.Telnet()
        try:
            print(host + " : " + port + " testing")
            tn.open(host, port, TIMEOUT)
            print(host + " : " + port + " ok")
        except BaseException as e:
            print(host + " : " + port + " fail ")
            pass

