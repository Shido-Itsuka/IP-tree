
def border(ip, prefix):
    sus = ip.replace('.', '')
    sus = sus[:prefix].ljust(32, '0')
    sus.insert(sus.find())
    return sus


print(border('11111111.11111111.11111111.11111111', 28))
