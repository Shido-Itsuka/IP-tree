class IP_Calculator:
    # A matrix consists of lists.
    # The mask prefix is on the 1st place, and the mask itself is on the 2nd.
    masks = [
        [0, "000.000.000.000"], [1, "128.000.000.000"], [2, "192.000.000.000"],
        [3, "224.000.000.000"], [4, "240.000.000.000"], [5, "248.000.000.000"],
        [6, "252.000.000.000"], [7, "254.000.000.000"], [8, "255.000.000.000"],
        [9, "255.128.000.000"], [10, "255.192.000.000"], [11, "255.224.000.000"],
        [12, "255.240.000.000"], [13, "255.248.000.000"], [14, "255.252.000.000"],
        [15, "255.254.000.000"], [16, "255.255.000.000"], [17, "255.255.128.000"],
        [18, "255.255.192.000"], [19, "255.255.224.000"], [20, "255.255.240.000"],
        [21, "255.255.248.000"], [22, "255.255.252.000"], [23, "255.255.254.000"],
        [24, "255.255.255.000"], [25, "255.255.255.128"], [26, "255.255.255.192"],
        [27, "255.255.255.224"], [28, "255.255.255.240"], [29, "255.255.255.248"],
        [30, "255.255.255.252"], [31, "255.255.255.254"], [32, "255.255.255.255"]
    ]

    def __init__(self, ip, prefix):
        self.ip_address = None
        self.netmask = None
        self.wildcard = None
        self.bin_ip_address = None
        self.bordered_ip_address = None
        self.bin_netmask = None
        self.bin_wildcard = None
        self.bin_network = None
        self.bin_broadcast = None
        self.bin_hostmin = None
        self.bin_hostmax = None
        self.network = None
        self.broadcast = None
        self.hostmin = None
        self.hostmax = None
        self.hosts = None

        # Вводимый IP-адрес
        self.ip_input = ip

        # Вводимый префикс
        self.prefix = prefix

    @staticmethod
    def ip_bin(ip) -> str:
        bites = ip.split('.')
        bin_bite = []
        for bite in bites:
            bin_bite.append(format(int(bite), 'b').zfill(8))
        bin_ip = '.'.join(bin_bite)
        return bin_ip

    @staticmethod
    def ip_dec(ip) -> str:
        bites = ip.split('.')
        dec_bite = []
        for bite in bites:
            dec_bite.append(int(bite, 2))
        dec_ip = '.'.join(map(str, dec_bite))
        return dec_ip

    @staticmethod
    def border(ip, prefix, number='0') -> str:
        sus = ip.replace('.', '')
        sus = sus[:prefix].ljust(32, number)
        return f'{sus[:8]}.{sus[8:16]}.{sus[16:24]}.{sus[24:32]}'

    @staticmethod
    def wildcard_create(prefix) -> str:
        sus = f'{prefix * "0"}' + f'{(32 - prefix) * "1"}'
        return f'{sus[:8]}.{sus[8:16]}.{sus[16:24]}.{sus[24:32]}'

    @staticmethod
    def hmin_hmax(network, broadcast) -> (str, str):
        hmin, hmax = network.split('.'), broadcast.split('.')
        if hmin[3] == "255":
            hmin[3] = "0"
            if hmin[2] == "255":
                hmin[2] = "0"
                if hmin[1] == "255":
                    hmin[1] = "0"
                    if hmin[0] == "255":
                        hmin[0] = "0"
                    else:
                        hmin[0] = str(int(hmin[0]) + 1)
                else:
                    hmin[1] = str(int(hmin[1]) + 1)
            else:
                hmin[2] = str(int(hmin[2]) + 1)
        else:
            hmin[3] = str(int(hmin[3]) + 1)

        if hmax[3] == "0":
            hmax[3] = "255"
            if hmax[2] == "0":
                hmax[2] = "255"
                if hmax[1] == "0":
                    hmax[1] = "255"
                    if hmax[0] == "0":
                        hmax[0] = "255"
                    else:
                        hmax[0] = str(int(hmax[0]) - 1)
                else:
                    hmax[1] = str(int(hmax[1]) - 1)
            else:
                hmax[2] = str(int(hmax[2]) - 1)
        else:
            hmax[3] = str(int(hmax[3]) - 1)

        if network == broadcast:  # pervyi kostyl'
            hmin, hmax = hmax, hmin

        return ".".join(hmin), ".".join(hmax)

    @staticmethod
    def host_counter(prefix) -> int:
        if prefix == 32:
            return 0
        else:
            return (2 ** (32 - prefix)) - 2

    def ip_check(self) -> str:
        ip = self.ip_input
        if ip.count('.') == 3:
            bites = ip.split('.')
            valid_ip = True
            for bite in bites:
                if not bite.isdigit() or int(bite) not in range(0, 256):
                    valid_ip = False
                    break
            if valid_ip:
                return ip
            else:
                raise ValueError('Такого IP-адреса не существует, повторите ввод.')
        else:
            raise ValueError('Такого IP-адреса не существует, повторите ввод.')

    def main(self):
        self.ip_address = self.ip_check()
        self.netmask = self.masks[self.prefix][1]
        self.wildcard = self.ip_dec(self.wildcard_create(self.prefix))
        self.bin_ip_address = self.ip_bin(self.ip_address)
        self.bin_netmask = self.ip_bin(self.netmask)
        self.network = self.ip_dec(self.border(self.bin_ip_address, self.prefix))
        self.broadcast = self.ip_dec(self.border(self.bin_ip_address, self.prefix, '1'))
        self.hosts = self.host_counter(self.prefix)

        if self.hosts == 0:
            self.hostmin, self.hostmax = 'N/A', 'N/A'
            self.bin_hostmin, self.bin_hostmax = 'N/A', 'N/A'
        else:
            self.hostmin, self.hostmax = self.hmin_hmax(self.network, self.broadcast)
            self.bin_hostmin = self.ip_bin(self.hostmin)
            self.bin_hostmax = self.ip_bin(self.hostmax)

        self.bin_wildcard = self.ip_bin(self.wildcard)
        self.bin_network = self.ip_bin(self.network)
        self.bin_broadcast = self.ip_bin(self.broadcast)
        return self.output()

    def output(self):
        return [[self.ip_address, self.bin_ip_address],  # IP-адрес dec и bin
                [self.prefix, None],  # префикс
                [self.netmask, self.bin_netmask],  # Маска dec и bin
                [self.wildcard, self.bin_wildcard],  # Обратная маска dec и bin
                [self.network, self.bin_network],  # Номер сети dec и bin
                [self.broadcast, self.bin_broadcast],  # Широковещательный IP-адрес dec и bin
                [self.hostmin, self.bin_hostmin],  # IP адрес первого хоста dec и bin
                [self.hostmax, self.bin_hostmax],  # IP адрес последнего хоста dec и bin
                [self.hosts, None],  # Количество хостов
                ]


if __name__ == '__main__':
    c1 = IP_Calculator('192.168.0.1', 24)
    c1.main()
