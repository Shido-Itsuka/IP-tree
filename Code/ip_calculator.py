class IP_Calculator:
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

    def __init__(self, ip):
        self.ip_address = ip
        self.prefix = None
        self.netmask = None
        self.bin_ip_address = None
        self.bordered_ip_address = None
        self.bin_netmask = None
        self.network = None
        self.broadcast = None
        self.hostmin = None
        self.hostmax = None
        self.hosts = None

    @staticmethod
    def ip_bin(ip):
        bites = ip.split('.')
        bin_bite = []
        for bite in bites:
            bin_bite.append(format(int(bite), 'b').zfill(8))
        bin_ip = '.'.join(bin_bite)
        return bin_ip

    @staticmethod
    def ip_dec(ip):
        bites = ip.split('.')
        dec_bite = []
        for bite in bites:
            dec_bite.append(int(bite, 2))
        dec_ip = '.'.join(map(str, dec_bite))
        return dec_ip

    @staticmethod
    def border(ip, prefix, number_after_border='0'):
        sus = ip.replace('.', '')
        sus = sus[:prefix].ljust(32, number_after_border)
        return f'{sus[:8]}.{sus[8:16]}.{sus[16:24]}.{sus[24:32]}'

    def hmin_hmax(self, network, broadcast):
        hmin, hmax = network.split('.'), network.split('.')
        hmin[3] = str(int(hmin[3]) + 1)
        hmax[3] = str(int(hmax[3]) - 1)




    @staticmethod
    def host_counter(prefix):
        return (2**(32-prefix))-2

    def prettyprint(self, array, columns, separators='  ', welcome=None):
        if welcome:
            print(welcome)
        diff = len(array) // columns
        for _ in range(diff):
            for __ in range(columns):
                if self.masks[_ + __ * diff][0] < 10:
                    print(' ', end='')
                print(*self.masks[_ + __ * diff], sep=' - ', end='')
                if __ != columns - 1:
                    print(separators, end='')
            print()

    def main(self):
        self.prettyprint(self.masks, 3, separators=' | ', welcome='Выберете и введите префикс:')
        self.prefix = int(input('Ваш выбор: '))
        self.netmask = self.masks[self.prefix][1]
        self.bin_ip_address = self.ip_bin(self.ip_address)
        self.network = self.ip_dec(self.border(self.bin_ip_address, self.prefix))
        self.broadcast = self.ip_dec(self.border(self.bin_ip_address, self.prefix, '1'))
        self.hostmin = None
        self.hosts = self.host_counter(self.prefix)

        self.output()

    def output(self):
        print(66 * '-',
              f'\nIP: {self.ip_address}'
              f'\nПрефикс: {self.prefix}'
              f'\nМаска: {self.netmask}'
              f'\nIP в бинарном виде: {self.bin_ip_address}'
              f'\nМаска в бинарном виде: {self.bin_netmask}'
              f'\nНомер сети: {self.network}'
              f'\nШироковещательный IP-адрес: {self.broadcast}'
              f'\nIP адрес первого хоста: {self.hostmin}'
              f'\nIP адрес последнего хоста: {self.hostmax}'
              f'\nКоличество хостов: {self.hosts}'
              f'\n', 66 * '-')


c1 = IP_Calculator('192.168.1.1')
c1.main()
