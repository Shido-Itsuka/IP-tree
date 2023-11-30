import re


def validate_ip(ip):
    pattern = r"^[0-9\.]*$"
    if re.match(pattern, ip):
        return True
    else:
        return False


validate_ip(input("Enter IP address: "))
