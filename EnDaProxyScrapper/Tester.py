#The tester file, tests the EnDaProxyScrapper module

#Import all needed modules
from ProxyScrapper import *
import time
from colorama import init, Fore, Back, Style

init(convert=True)

# The list of the possible Errors:
# [1] >> EnDaProxyScrapper : GetHttpServerListError
# [2] >> EnDaProxyScrapper : GetSocks4ServerListError
# [3] >> EnDaProxyScrapper : GetSocks5ServerListError
# [4] >> False
# [5] >> False
# [6] >> EnDaProxyScrapper : GetWorkingProxyServersListError / False
# [7] >> EnDaProxyScrapper : SaveProxyServerListError / False
# [8] >> EnDaProxyScrapper : GetProxyServerListFromFileError / False

def correct(test_id=0,message="was terminated without any error!"):
    print(Fore.WHITE + "    [" + Fore.GREEN + "+" + Fore.WHITE + "] >> " +  Fore.LIGHTGREEN_EX + "(" + Fore.WHITE + str(test_id) + Fore.LIGHTGREEN_EX + ") test " + message)
    print()

def wrong(test_id=0,message="was terminated with an error!",error=""):
    print(Fore.WHITE + "    [" + Fore.RED + "-" + Fore.WHITE + "] >> " +  Fore.LIGHTRED_EX + "(" + Fore.WHITE + str(test_id) + Fore.LIGHTRED_EX + ") test " + message + " " + Fore.WHITE + f"[" + error + Fore.WHITE + "]")
    print()

#Print the list of the tests
# Test (1) -> Get the http servers
# Test (2) -> Get the socks4 servers
# Test (3) -> Get the socks5 servers
# Test (4) -> Get the server status (offline)
# Test (5) -> Get the server status (online)
# Test (6) -> Get the internet connection
# Test (7) -> Get the working server list
# Test (8) -> Save the working server list
# Test (9) -> Get the list from a file

print("""
Test (1) -> Get the http servers
Test (2) -> Get the socks4 servers
Test (3) -> Get the socks5 servers
Test (4) -> Get the server status (offline)
Test (5) -> Get the server status (online)
Test (6) -> Get the internet connection
Test (7) -> Get the working server list
Test (8) -> Save the working server list
Test (9) -> Get the list from a file
""")

#The tests
ProxyScrapper = EnDaProxyScrapper()

# Test (1) -> Get the http servers
if ProxyScrapper.get_httpServerList(timeout=500) == "EnDaProxyScrapper : GetHttpServerListError":
    wrong(test_id=1,error="EnDaProxyScrapper : GetHttpServerListError")
else:
    correct(test_id=1)

# Test (2) -> Get the socks4 servers
if ProxyScrapper.get_socks4ServerList(timeout=500) == "EnDaProxyScrapper : GetSocks4ServerListError":
    wrong(test_id=2,error="EnDaProxyScrapper : GetSocks4ServerListError")
else:
    correct(test_id=2)

# Test (3) -> Get the socks5 servers
if ProxyScrapper.get_socks5ServerList(timeout=500) == "EnDaProxyScrapper : GetSocks5ServerListError":
    wrong(test_id=3,error="EnDaProxyScrapper : GetSocks5ServerListError")
else:
    correct(test_id=3)

# Test (4) -> Get the server status (offline)
if ProxyScrapper.get_serverStatus(port=81) == False:
    wrong(test_id=4,error="Offline Server")
else:
    correct(test_id=4)
print(Fore.WHITE + "    [!] >> It's ok to be offline on test 4!")
print()

# Test (5) -> Get the server status (online)
if ProxyScrapper.get_serverStatus(ip="google.com",port="443") == False:
    wrong(test_id=5,error="Offline Server")
else:
    correct(test_id=5)

# Test (6) -> Get the internet connection
if ProxyScrapper.get_internetConnectionStatus() == False:
    wrong(test_id=6,error="No internet connection")
else:
    correct(test_id=6)

# Test (7) -> Get the working server list
if ProxyScrapper.get_workingProxyList(timeout=500) == "EnDaProxyScrapper : GetWorkingProxyServersListError":
    wrong(test_id=7,error="EnDaProxyScrapper : GetWorkingProxyServersListError")
else:
    correct(test_id=7)

# Test (8) -> Save the working server list
if ProxyScrapper.save_proxyServerList(timeout=500) == "EnDaProxyScrapper : SaveProxyServerListError" or ProxyScrapper.save_proxyServerList(timeout=500) == False:
    wrong(test_id=8,error="EnDaProxyScrapper : SaveProxyServerListError")
else:
    correct(test_id=8)

# Test (9) -> Get the list from a file
if ProxyScrapper.get_proxyServersListFile() in ("EnDaProxyScrapper : GetProxyServerListFromFileError",False):
    wrong(test_id=9,error="EnDaProxyScrapper : GetProxyServerListFromFileError")
else:
    correct(test_id=9)

ok = input(Fore.MAGENTA + "[*] All ok >> ")