import ipaddress
import random

def getRandomNetwork(minPrefixLen=1,maxPrefixLen=30,type='regular'):
    while True:
        hostPrefix = random.randrange(minPrefixLen,maxPrefixLen)
        hostIntAddress = random.randrange(1,4294967295)
        somehost = ipaddress.ip_interface((hostIntAddress,hostPrefix))
        if (somehost.is_global==True or checkRfc1918(somehost.network)) and type=='regular':
            break
        elif (somehost.is_global==True) and type=='global':
            break
        elif (checkRfc1918(somehost.network)) and type=='rfc1918':
            break
    return somehost.network

def checkRfc1918(network):
    #Check if a network is RFC1918 private address space
    if network.subnet_of(ipaddress.ip_network('10.0.0.0/8')) or network == ipaddress.ip_network('10.0.0.0/8'):
        return True
    elif network.subnet_of(ipaddress.ip_network('172.16.0.0/20')) or network == ipaddress.ip_network('172.16.0.0/20'):
        return True
    elif network.subnet_of(ipaddress.ip_network('192.168.0.0/16')) or network == ipaddress.ip_network('192.168.0.0/16'):
        return True
    else:
        return False

print(getRandomNetwork(minPrefixLen=8,maxPrefixLen=24,type='regular'))