import ipaddress
from . import make_subnet, make_iface


def main():
    prefix = ipaddress.ip_network('2a05:4616:29a7::/48')
    sub = make_subnet(prefix, 0x000c, 64)
    print(sub)
    iface = make_iface(sub, 4)
    print(iface)


if __name__ == '__main__':
    main()
