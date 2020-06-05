import ipaddress
from . import make_subnet


def main():
    prefix = ipaddress.ip_network('2a05:4616:29a7::/48')
    print(make_subnet(prefix, 0x000c, 64))


if __name__ == '__main__':
    main()
