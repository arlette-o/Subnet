import unittest
from unittest.mock import patch
from ipInfo import IPInfo

class TestIpInfo(unittest.TestCase):

    #getOctets() tests

    #subnet() tests

    #netID() tests

    #hostID() tests


    #classType() tests
    def test_classType1(self):
        userIP = "127.255.255.255"
        ip = IPInfo(userIP, 0)
        self.assertEqual(ip.classType(), "A")

    def test_classType2(self):
        userIP = "127.0.0.0"
        ip = IPInfo(userIP, 0)
        self.assertEqual(ip.classType(), "A")

    def test_classType3(self):
        userIP = "126.255.255.255"
        ip = IPInfo(userIP, 0)
        self.assertEqual(ip.classType(), "A")

    def test_classType4(self):
        userIP = "191.255.255.255"
        ip = IPInfo(userIP, 0)
        self.assertEqual(ip.classType(), "B")

    def test_classType5(self):
        userIP = "191.0.0.0"
        ip = IPInfo(userIP, 0)
        self.assertEqual(ip.classType(), "B")

    def test_classType6(self):
        userIP = "191.255.255.255"
        ip = IPInfo(userIP, 0)
        self.assertEqual(ip.classType(), "B")

    def test_classType7(self):
        userIP = "223.255.255.255"
        ip = IPInfo(userIP, 0)
        self.assertEqual(ip.classType(), "C")

    def test_classType8(self):
        userIP = "223.0.0.0"
        ip = IPInfo(userIP, 0)
        self.assertEqual(ip.classType(), "C")

    def test_classType9(self):
        userIP = "222.255.255.255"
        ip = IPInfo(userIP, 0)
        self.assertEqual(ip.classType(), "C")


    #privacy() tests
    def test_privacy1(self):
        userIP = "172.16.0.0"
        ip = IPInfo(userIP, 0)
        self.assertTrue(ip.privacy())

    def test_privacy2(self):
        userIP = "10.0.0.0"
        ip = IPInfo(userIP, 0)
        self.assertTrue(ip.privacy())

    def test_privacy3(self):
        userIP = "192.168.0.0"
        ip = IPInfo(userIP, 0)
        self.assertTrue(ip.privacy())

    def test_privacy4(self):
        userIP = "9.0.0.0"
        ip = IPInfo(userIP, 0)
        self.assertFalse(ip.privacy())

    def test_privacy5(self):
        userIP = "11.0.0.0"
        ip = IPInfo(userIP, 0)
        self.assertFalse(ip.privacy())

    def test_privacy6(self):
        userIP = "172.32.0.0"
        ip = IPInfo(userIP, 0)
        self.assertFalse(ip.privacy())

    def test_privacy7(self):
        userIP = "172.15.255.255"
        ip = IPInfo(userIP, 0)
        self.assertFalse(ip.privacy())

    def test_privacy8(self):
        userIP = "192.167.255.255"
        ip = IPInfo(userIP, 0)
        self.assertFalse(ip.privacy())

    def test_privacy9(self):
        userIP = "192.169.0.0"
        ip = IPInfo(userIP, 0)
        self.assertFalse(ip.privacy())

if __name__ == "__main__":
    unittest.main()