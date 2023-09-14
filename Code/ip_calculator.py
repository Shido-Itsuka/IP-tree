class IP_Calculator:
    def __init__(self, ip, nmask):
        self.ip_address = ip
        self.network_mask = nmask

    def dec_ip_to_bin_ip(self):
        return [format(i, "b") for i in self.ip_address]

    def dec_mask_to_bin_mask(self):
        return [format(i, "b") for i in self.network_mask]

    def ip_bin(self, ip):
        bites = ip.split('.')
        bin_bite = []
        for bite in bites:
            bin_bite.append(format(int(bite), 'b').zfill(8))
        bin_ip = '.'.join(bin_bite)
        return bin_ip

    def border(self, ip, prefix):
        sus = ip.replace('.', '')
        sus = sus[:prefix].ljust(32, '0')
        sus.insert(sus.find())
        return sus



