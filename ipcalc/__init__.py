import ipaddress


def make_subnet(net: ipaddress.IPv6Network, offset: int, prefix: int) -> ipaddress.IPv6Network:
    if (net.prefixlen > prefix):
        raise ValueError(f'{prefix} < {net}')

    offset = (offset * (1 << (128-prefix))) & (~net.netmask._ip)

    return ipaddress.IPv6Network((net.network_address._ip | offset, prefix))


def make_iface(net: ipaddress.IPv6Network, offset: int) -> ipaddress.IPv6Interface:
    offset = offset & (~net.netmask._ip)
    return ipaddress.IPv6Interface((net.network_address._ip | offset, net.prefixlen))
