# 44.142.192.42

def getOctets(IP):
    octets = IP.split(".")
    for i in range(4):
        octets[i] = int(octets[i])
    return octets

def calcSubMask(IP, sub):
    ans = int(sub/8)
    bits = sub % 8
    comp = (2**bits) -1
    comp = comp << (8-bits)
    octs = getOctets(IP)
    subAddress = octs[:ans]
    subAddress.append(octs[ans]& (comp))
    for i in range(3-ans):
        subAddress.append(0)
    return subAddress

IPA = input("Enter first IP: ")
IPB = input("Enter second IP: ")
submask = int(input("Enter subnet: "))
subA = calcSubMask(IPA, submask)
subB = calcSubMask(IPB, submask)
addA = ".".join(str(oct) for oct in subA)
addB = ".".join(str(octb) for octb in subB)
print("Subnet Address A:", addA)
print("Subnet Address B:", addB)
if subA != subB:
    print("different subnets")
else:
    print("same subnet!")
