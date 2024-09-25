import ipaddress
import random

#set a host address and mask
somehost = ipaddress.ip_interface('192.168.1.230/24')

#Get the network address for the host
print(somehost.network)

#Get the network address for the host without the prefix
print(somehost.network.network_address)

#get the subnet mask instead of slash notation
print(somehost.netmask)

#get the first usable host address
print(somehost.network[1])

#get the last usable host address
print(somehost.network[-2])

#get the boardcast address
print(somehost.network.broadcast_address)

#get the total number of usable hosts in the network
print(somehost.network.num_addresses-2)

#get a random usable host address in the network
randomhost = random.randrange(1,somehost.network.num_addresses-2)
print(somehost.network[randomhost])

#check if an address is in a network (true/false)
addr = ipaddress.ip_address('192.168.1.5')
if addr in somehost.network:
    print('The address is in the network')
if not addr in somehost.network:
    print('The address is NOT in the network')

#give the address in binary
print('{:b}'.format(somehost.ip))

#
# SUBNETTING
#
#get subnets of the current network (just one bit borrowed) -- returns list of network objects
print(list(somehost.network.subnets()))
#get subnets of the current network (arbitrary number of bits borrowed eg 4)
print(list(somehost.network.subnets(prefixlen_diff=4)))
#get subnets of the current network (arbitrary prefix length longer than source network eg 25)
print(list(somehost.network.subnets(new_prefix=25)))
# Check if another network is a subnet of this network (can also check if it is a supernet of this network)
anothernet = ipaddress.ip_network('192.168.1.16/28')
print(anothernet.subnet_of(somehost.network))