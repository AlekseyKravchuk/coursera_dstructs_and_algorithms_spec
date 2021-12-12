class IPAddress:
    def __init__(self, ip):
        self.ip = ip

    def __str__(self):
        return f'IP_address: {self.ip}'


if __name__ == '__main__':
    ip1 = IPAddress('10.1.1.1')
    ip2 = IPAddress('10.2.2.2')

    print(ip1)

