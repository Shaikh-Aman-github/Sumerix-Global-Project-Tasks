from system_info import get_system_info
from network_info import get_network_info
from report_generator import generate_report


def main():
    print("=" * 60)
    print("SECURE NETWORK ASSET INVENTORY")
    print("=" * 60)

    print("\nCollecting system information...")
    system_info = get_system_info()

    print("Collecting network information...")
    network_info = get_network_info()

    print("\nSYSTEM INFORMATION")
    print("-" * 60)

    for key, value in system_info.items():
        print(f"{key.replace('_', ' ').title()}: {value}")

    print("\nNETWORK INFORMATION")
    print("-" * 60)

    print(f"Primary IP: {network_info['primary_ip']}")
    print(f"MAC Address: {network_info['mac_address']}")
    print(f"Hostname: {network_info['hostname']}")

    print("\nNETWORK INTERFACES")
    print("-" * 60)

    for interface in network_info["interfaces"]:
        print(f"- {interface['name']}")

    report_file = generate_report(system_info, network_info)

    print("\n" + "=" * 60)
    print(f"Report successfully generated: {report_file}")
    print("=" * 60)


if __name__ == "__main__":
    main()