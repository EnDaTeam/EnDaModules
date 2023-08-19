#An useful module which gets a list of free proxy servers
#This module is using a free API from proxyscrape.com

#Import all needed modules
import os
import requests
import socket

# The list of the possible Errors:
# [1] >> EnDaProxyScrapper : GetHttpServerListError
# [2] >> EnDaProxyScrapper : GetSocks4ServerListError
# [3] >> EnDaProxyScrapper : GetSocks5ServerListError
# [4] >> EnDaProxyScrapper : GetWorkingProxyServersListError
# [5] >> EnDaProxyScrapper : SaveProxyServerListError
# [6] >> EnDaProxyScrapper : GetProxyServerListFromFileError

#Create the main class
class EnDaProxyScrapper():
    """
    An useful class which gets a list of free proxy servers
    This module is using a free API from proxyscrape.com
    """
    def __init__(self,path=""):
        self.path = path
        if path == "":
            self.path = os.getcwd()
    
    #Define a function which gets the list of http servers
    def get_httpServerList(self,timeout=500):
        """
        Gets the list of proxy servers which are using http protocol

        Timeout : X (in ms)
        """
        try:
            url = f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout={timeout}&country=all&ssl=all&anonymity=all"
            payload={}
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload).text
            response.replace("\r\n","")
            s = response.split("\r\n")
            k = []
            for i in s:
                r = i.split(":")
                k.append(r)
            k.pop()
            return k
        except:
            return "EnDaProxyScrapper : GetHttpServerListError"

    #Define a function which gets the list of socks4 servers
    def get_socks4ServerList(self,timeout=500):
        """
        Gets the list of proxy servers which are using socks4 protocol

        Timeout : X (in ms)
        """
        try:
            url = f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout={timeout}&country=all&ssl=all&anonymity=all"
            payload={}
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload).text
            response.replace("\r\n","")
            s = response.split("\r\n")
            k = []
            for i in s:
                r = i.split(":")
                k.append(r)
            k.pop()
            return k
        except:
            return "EnDaProxyScrapper : GetSocks4ServerListError"
        
    #Define a function which gets the list of socks5 servers
    def get_socks5ServerList(self,timeout=1000):
        """
        Gets the list of proxy servers which are using socks5 protocol

        Timeout : X (in ms)
        """
        try:
            url = f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout={timeout}&country=all&ssl=all&anonymity=all"
            payload={}
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload).text
            response.replace("\r\n","")
            s = response.split("\r\n")
            k = []
            for i in s:
                r = i.split(":")
                k.append(r)
            k.pop()
            return k
        except:
            return "EnDaProxyScrapper : GetSocks5ServerListError"
        
    #Define a function which verifies the connection between us and the proxy server
    def get_serverStatus(self,ip="8.8.8.8",port="80"):
        """
        Gets the status of a proxy server (online or not)

        IP : X (ex : 8.8.8.8 etc.)
        Port : Y (int : 80 etc.)
        """
        try:
            sock = socket.create_connection((ip, int(port)), timeout=1)
            sock.close()
            return True
        except:
            return False
        
    #Define a function which gets the info about the internet connection
    def get_internetConnectionStatus(self):
        """
        Gets the status of internet connection (if you are connected or not)
        """
        try:
            sock = socket.create_connection(("8.8.8.8", 53), timeout=1)
            sock.close()
            return True
        except OSError:
            return False
        
    #Define a function which gets the normal proxy list and transform it into a working proxy list 
    def get_workingProxyList(self,protocol="http",timeout=500):
        """
        Gets the list of proxy servers which are using a protocol and test them and generated a new list

        Protocol : X (http, socks4, socks5)
        Timeout = Y (in ms)
        """
        try:
            try:
                int(timeout)
            except:
                return False
            if protocol.strip().lower() in ("http",""):
                lista = EnDaProxyScrapper.get_httpServerList(self,timeout=timeout)
            elif protocol.strip().lower() == "socks4":
                lista = EnDaProxyScrapper.get_socks4ServerList(self,timeout=timeout)
            elif protocol.strip().lower() == "socks5":
                lista = EnDaProxyScrapper.get_socks5ServerList(self,timeout=timeout)
            else:
                return False
            k = []
            for i in lista:
                if EnDaProxyScrapper.get_serverStatus(self,ip=i[0],port=i[1]):
                    k.append([i[0],i[1]])
            return k
        except:
            return "EnDaProxyScrapper : GetWorkingProxyServersListError"


    #Define a function which saves the proxy list into a file
    def save_proxyServerList(self,protocol="http",timeout=500,delete_previous=False):
        """
        Creates a file named "ProxyServersList.txt" and saves the working proxy servers

        Protocol : X (http, socks4, socks5)
        Timeout = Y (in ms)
        delete_previous : Z (True or False -> If file exists delete it and create a new one or not)
        """
        try:
            if os.path.isfile(self.path + "/ProxyServersList.txt"):
                if delete_previous == True:
                    os.remove(self.path + "/ProxyServersList.txt")
                else:
                    return False
            f = open(self.path + "/ProxyServersList.txt","w+")
            lista = EnDaProxyScrapper.get_workingProxyList(self,protocol=protocol,timeout=timeout)
            for i in lista:
                f.write(i[0] + ":" + i[1] + "\n")
            return True
        except:
            return "EnDaProxyScrapper : SaveProxyServerListError"

    #Define a function which gets the saved proxy list
    def get_proxyServersListFile(self):
        """
        Reads the saved file and gets proxy servers and returns a list of them
        """
        try:
            if not os.path.isfile(self.path + "/ProxyServersList.txt"):
                return False
            f = open(self.path + "/ProxyServersList.txt","r+")
            k = []
            for i in f.readlines():
                i = i.split(":")
                k.append([i[0],i[1].strip()])
            f.close()
            return k
        except:
            return "EnDaProxyScrapper : GetProxyServerListFromFileError"