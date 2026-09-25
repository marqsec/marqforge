from importlib.metadata import metadata, PackageNotFoundError
from typing import Dict, Any, Final

PACKAGE_NAME = "marqforge"

LICENSE_RULES: Final[Dict[str, Dict[str, bool]]] = {
    "MIT": {
        "commercial_use": True,
        "modification": True,
        "distribution": True,
        "private_use": True,
    },
    "Apache-2.0": {
        "commercial_use": True,
        "modification": True,
        "distribution": True,
        "private_use": True,
    },
    "GPL-3.0": {
        "commercial_use": True,
        "modification": True,
        "distribution": True,
        "private_use": True,
    }
}

def get_license() -> Dict[str, Any]:
    try:
        pkg_metadata = metadata(PACKAGE_NAME)
        license_name = pkg_metadata.get("License", "MIT")
    except PackageNotFoundError:
        license_name = "MIT"

    rules = LICENSE_RULES.get(license_name, {
        "commercial_use": False,
        "modification": False,
        "distribution": False,
        "private_use": True,
    })

    return {
        "name": license_name,
        "spdx": license_name,
        "url": f"https://opensource.org{license_name.lower()}",
        **rules
    }
