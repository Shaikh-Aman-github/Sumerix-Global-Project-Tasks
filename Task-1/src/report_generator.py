from pathlib import Path


def generate_report(system_info, network_info):
    """Generate a text report containing system and network information."""

    report_directory = Path("reports")
    report_directory.mkdir(exist_ok=True)

    report_file = report_directory / "system_inventory_report.txt"

    with report_file.open("w", encoding="utf-8") as file:
        file.write("=" * 60 + "\n")
        file.write("SECURE NETWORK ASSET INVENTORY REPORT\n")
        file.write("=" * 60 + "\n\n")

        file.write("SYSTEM INFORMATION\n")
        file.write("-" * 60 + "\n")

        for key, value in system_info.items():
            formatted_key = key.replace("_", " ").title()
            file.write(f"{formatted_key}: {value}\n")

        file.write("\nNETWORK INFORMATION\n")
        file.write("-" * 60 + "\n")

        for key, value in network_info.items():
            formatted_key = key.replace("_", " ").title()
            file.write(f"{formatted_key}: {value}\n")

    return report_file