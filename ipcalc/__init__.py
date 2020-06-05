from ipaddress import IPv6Interface, IPv6Address, IPv6Network
from dataclasses import dataclass
from typing import Dict


def make_subnet(net: IPv6Network, offset: int, prefix: int) -> IPv6Network:
    if (net.prefixlen > prefix):
        raise ValueError(f'{prefix} < {net}')

    offset = (offset * (1 << (128-prefix))) & (~net.netmask._ip)

    return IPv6Network((net.network_address._ip | offset, prefix))


def make_iface(net: IPv6Network, offset: int) -> IPv6Interface:
    offset = offset & (~net.netmask._ip)
    return IPv6Interface((net.network_address._ip | offset, net.prefixlen))


@dataclass
class IFace:
    mac: int = None
    ip: int = None

    def iface(self, prefix: IPv6Network) -> IPv6Interface:
        ip = None

        if self.ip is not None:
            ip = self.ip

        if ip is None and self.mac is not None:
            ip = 0xfffe000000 | self.mac

        return make_iface(prefix, ip)


@dataclass
class Net:
    offset: int
    prefix: int
    ifaces: Dict[str, IFace]

    def iface(self, prefix: IPv6Network, name: str) -> IPv6Interface:
        sub = make_subnet(prefix, self.offset, self.prefix)
        return self.ifaces[name].iface(sub)


@dataclass
class Zone:
    prefix: IPv6Network
    nets: Dict[str, Net]

    def iface(self, net: str, name: str) -> IPv6Interface:
        return self.nets[net].iface(self.prefix, name)
