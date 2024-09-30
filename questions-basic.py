import ipaddress
import random

def getRandomNetwork(minPrefixLen=1,maxPrefixLen=30,type='regular'):
    while True:
        hostPrefix = random.randrange(minPrefixLen,maxPrefixLen+1)
        hostIntAddress = random.randrange(1,4294967296)
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

def bitsForSubnets(minBits,maxBits):
    # Choose a random number of bits to borrow between minBits and maxBits, return the number of bits borrowed and the number of subnets created
    # Tip: for CLASS A borrow 1-22 bits, CLASS B 1-14 bits, and CLASS C 1-6 bits
    bitsBorrowed = random.randrange(minBits,maxBits+1)
    subnetsCreated = 2**bitsBorrowed
    return {'bitsBorrowed': bitsBorrowed, 'subnetsCreated': subnetsCreated}

def genMCSABitsForSubnets(minBits,maxBits):
    # Generate a MCSA question of the style "How many bits need to be borrowed to create X subnets?"
    # Tip: for CLASS A borrow 1-22 bits, CLASS B 1-14 bits, and CLASS C 1-6 bits
    bFS = bitsForSubnets(minBits,maxBits)
    question = {}
    question['stem'] = 'How many bits need to be borrowed to create {} subnets?'.format(bFS['subnetsCreated'])
    question['answers'] = {}
    question['answers']['correct'] = bFS['bitsBorrowed']
    question['answers']['distractor1'] = random.choice(list(set([x for x in range(minBits, maxBits+1)]) - set([question['answers']['correct']])))
    question['answers']['distractor2'] = random.choice(list(set([x for x in range(minBits, maxBits+1)]) - set([question['answers']['correct'],question['answers']['distractor1']])))
    question['answers']['distractor3'] = random.choice(list(set([x for x in range(minBits, maxBits+1)]) - set([question['answers']['correct'],question['answers']['distractor1'],question['answers']['distractor2']])))
    return question

def genMCSASubnetsForBits(minBits,maxBits):
    # Generate a MCSA question of the style "How many subnets are created if we borrow X bits?"
    # Tip: for CLASS A borrow 1-22 bits, CLASS B 1-14 bits, and CLASS C 1-6 bits
    bFS = bitsForSubnets(minBits,maxBits)
    question = {}
    question['stem'] = 'How many subnets are created if we borrow {} bits?'.format(bFS['bitsBorrowed'])
    question['answers'] = {}
    question['answers']['correct'] = bFS['subnetsCreated']
    possibleAnswers = []
    for x in range(minBits,maxBits+1):
        possibleAnswers.append(2**x)
    question['answers']['distractor1'] = random.choice(list(set(possibleAnswers) - set([question['answers']['correct']])))
    question['answers']['distractor2'] = random.choice(list(set(possibleAnswers) - set([question['answers']['correct'],question['answers']['distractor1']])))
    question['answers']['distractor3'] = random.choice(list(set(possibleAnswers) - set([question['answers']['correct'],question['answers']['distractor1'],question['answers']['distractor2']])))
    return question

def printMCSAQuestion(question):
    print(question['stem'])
    choices = list(range(0,len(question['answers'])))
    random.shuffle(choices)
    choice = []
    choice.append(list(question['answers'].keys())[choices[0]])
    choice.append(list(question['answers'].keys())[choices[1]])
    choice.append(list(question['answers'].keys())[choices[2]])
    choice.append(list(question['answers'].keys())[choices[3]])
    print('A. '+str(question['answers'][choice[0]]))
    print('B. '+str(question['answers'][choice[1]]))
    print('C. '+str(question['answers'][choice[2]]))
    print('D. '+str(question['answers'][choice[3]]))
    print('CORRECT: '+str(question['answers']['correct']))
    return

printMCSAQuestion(genMCSABitsForSubnets(1,6))
printMCSAQuestion(genMCSASubnetsForBits(1,6))

#print(getRandomNetwork(minPrefixLen=8,maxPrefixLen=24,type='regular'))
#print(getRandomNetwork(minPrefixLen=8,maxPrefixLen=24,type='rfc1918'))

# Simple Types of questions to generate:
# * DONE -- How many bits need to be borrowed to create X subnets
# * DONE -- How many subnets are created by borrowing X bits
# * What subnet mask allows for X usable host addresses
# * How many usable host addresses are there given a network and mask or / notation
# * What is the slash notation for a certain mask
# * What is the mask for a certain slash notation
# * What is the broadcast address for a given network address/mask
# * For a given network/mask identify a valid host address on that network
# * For a given host address (no mask) what subnet/mask would it be usable in
# * From a starting classful network address and a known number of needed subnets identify a valid subnet/mask or / notation
# * For a given address and mask or / notation determine if it is a host, network, or broadcast address
# * Identify if an address is a valid public, private, multicast, loopback, experimental, TEST-NET, or link-local address
# * For a given address/mask what is the last usable host on the network

# Complex Types of Questions to Generate
# * For a certain nework address and mask what are the subnet addresses and masks if the networks need x hosts, y hosts, z hosts etc