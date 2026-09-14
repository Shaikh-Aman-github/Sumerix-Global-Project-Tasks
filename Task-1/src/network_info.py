import socket
import uuid


def get_primary_ip():
    """Return the primary local IPv4 address when available."""

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.connect(("8.8.8.8", 80))
            return sock.getsockname()[0]
    except OSError:
        return "Unavailable"


def get_mac_address():
    """Return the system MAC address."""

    mac_number = uuid.getnode()

    mac_address = ":".join(
        f"{(mac_number >> offset) & 0xff:02x}"
        for offset in range(40, -1, -8)
    )

    return mac_address


def get_network_interfaces():
    """Return a list of network interfaces available on the system."""

    try:
        interfaces = socket.if_nameindex()
        return [name for _, name in interfaces]
    except OSError:
        return []


def get_interface_details():
    """Return basic information about each network interface."""

    interfaces = get_network_interfaces()

    interface_details = []

    for interface in interfaces:
        interface_details.append({
            "name": interface
        })

    return interface_details


def get_network_info():
    """Collect basic network information."""

    return {
        "primary_ip": get_primary_ip(),
        "mac_address": get_mac_address(),
        "hostname": socket.gethostname(),
        "interfaces": get_interface_details(),
    }