from telnetlib import Telnet
with Telnet('112.74.191.64', 3306) as tn:
     tn.interact()