
#send prompt to the user
#have them input an IP address, give user options as to what to have the script do

class IPInfo:

        def __init__(self, userIP, mask):
            self.userIP = userIP
            self.mask = mask

        def getOctets(self):
            octets = self.userIP.split(".")
            for i in range(4):
                octets[i] = int(octets[i])
            return octets

        #Maybe make so that it returns subnet address and mask
        #Default subnet masks per class
        #Class A subnet - 255.0.0.0 /8
        #Class B subnet - 255.255.0.0 /16
        #Class C subnet - 255.255.255.0 /24
        def subnet(self):
            #Do subnet calculations
            submask =0

            if self.mask != 0:
                print(f"Subnet address is:  /{self.mask}")
                return self.mask

            classType = self.classType()
            if classType == "A":
                submask = 8
                print("Subnet Address: .0.0.0 /8")
                print(f"----Each subnet can have {2^(32-submask)} hosts ")
            if classType == "B":
                submask = 16
                print("Subnet Address: .0.0 /16")
                print(f"----Each subnet can have {2^(32-submask)} hosts ")
            if classType == "C":
                submask = 24
                print("Subnet Address: .0 /24")
                print(f"----Each subnet can have {2^(32-submask)} hosts ")

            return submask

        #Class default net portions from figure 4.9 in
        #https://www.sciencedirect.com/topics/computer-science/subnet-mask
        #Class    IP        Net ID    Host ID
        #   A   a.b.c.d        a       b.c.d
        #   B   a.b.c.d       a.b       c.d
        #   C   a.b.c.d      a.b.c       d
        def netID(self):
            if self.mask != 0:
                #do netID calculation using self.mask
                return 0
            #Use default net part
            octets = self.getOctets()
            classType = self.classType()
            if classType == "A":
                print(f"Network Address: {octets[0]}.0.0.0 /8")
            if classType == "B":
                print(f"Network Address: {octets[0]}.{octets[1]}.0.0 /16")
            if classType == "C":
                print(f"Network Address: {octets[0]}.{octets[1]}.{octets[2]}.0 /24")
            #if classType == "D":
            #do network part calculations

        #Class default Host ID from figure 4.9 in
        #https://www.sciencedirect.com/topics/computer-science/subnet-mask
        # Class    IP        Net ID    Host ID
        #   A   a.b.c.d        a       b.c.d
        #   B   a.b.c.d       a.b       c.d
        #   C   a.b.c.d      a.b.c       d
        def hostID(self):
            if self.mask != 0:
                #Do host id part calculations
                return 0
            #Use default host values
            octets = self.getOctets()
            classType = self.classType()
            if classType == "A":
                print(f"{octets[2]}")
            if classType == "B":
                print("")
            if classType == "C":
                print("")
            #use default

            pass

        #Class A up to 127.255.255.255
        #Class B up to 191.255.255.255
        #Class C up to 223.255.255.255
        def classType(self):
            octets = self.getOctets()

            if octets[0] >= 224:
                classType = "D"
                print("class D")
            elif octets[0] >= 192:
                classType = "C"
                print("class C")
            elif octets[0] >= 128:
                classType = "B"
                print("class B")
            else:
                classType = "A"
                print("class A")

            return classType
        #change to be able to run unittests?


        def sameSubnet(self, other):
            pass
            ''' print("checking for same subnet")
            mask = self.subnet()'''



        #Private range from 10.0.0.0 to 10.255.255.255
        #172.16.0.0 to 172.31.255.255
        #192.168.0.0 to 192.168.255.255
        def privacy(self):
            #determine whether this IP is public or Private
            octets = self.getOctets()
            if octets[0] == 10:
                #if 0 <= octets[2] < 255:
               return True

            if octets[0] == 172:
                if 16 <= octets[1] <= 31:
                    return True

            if octets[0] == 192:
                if octets[1] == 168:
                    if 0 <= octets[2] <= 255:
                        return True
            return False


        def inputIP(self):
            print("What would you like to do with this IP?")
            print("(s) determine the subnet of this IP")
            print("(n) find the network portion of this IP")
            print("(h) find the host portion of this IP")
            print("(p) determine whether this IP is public or private")
            print("(d) determine whether this IP is on a specific subnet")
            print("(a) find all")
            option = input("")
            self.printInfo(option.lower())


        def printInfo(self, option):
            print(f"Your IP: {self.userIP}")

            if option == "s":
                print(f"{self.subnet()}")
            elif option == "n":
                print(f"{self.netID()}")
            elif option == "h":
                print(f"{self.hostID()}")
            elif option == "p":
                print(f"{self.privacy()}")
            elif option =="d":
                other = input("Enter the second IP: ")
                print(f"{self.sameSubnet(other)}")
            elif option == "a":
                print(f"{self.subnet()}")
                print(f"{self.netID()}")
                print(f"{self.hostID()}")
                print(f"{self.privacy()}")
            else:
                print("Invalid Option chosen, try again...")
                self.inputIP()



userIP = input("Enter an IP: ")
answer = input("Would you like to specify a subnet mask? (y) or (n)")
if answer.lower() == "y":
    print("Enter subnet mask value (for example for a /24 mask enter 24): ")
    subnet = input("")
    ip = IPInfo(userIP, subnet)
else:
    ip = IPInfo(userIP, 0)
ip.inputIP()

