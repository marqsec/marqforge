import platform
import sys
from typing import Dict, Any

def get_runtime() -> Dict[str, Any]:
    bit_architecture, _ = platform.architecture()
    return {
        "python": platform.python_version(),
        "platform": platform.system(),
        "platform_release": platform.release(),
        "platform_version": platform.version(),
        "architecture": platform.machine(),
        "bits": bit_architecture,
        "implementation": sys.implementation.name,
    }
