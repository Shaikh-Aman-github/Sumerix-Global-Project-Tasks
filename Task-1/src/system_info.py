import platform
import socket
from datetime import datetime


def get_system_info():
    """Collect basic information about the current system."""

    return {
        "hostname": socket.gethostname(),
        "operating_system": platform.system(),
        "os_release": platform.release(),
        "os_version": platform.version(),
        "architecture": platform.machine(),
        "python_version": platform.python_version(),
        "scan_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }