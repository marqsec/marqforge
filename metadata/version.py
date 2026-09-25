from importlib.metadata import version, PackageNotFoundError
from typing import Dict, Any

PACKAGE_NAME = "marqforge"

def get_version() -> Dict[str, Any]:
    try:
        raw_version = version(PACKAGE_NAME)
    except PackageNotFoundError:
        raw_version = "0.1.0-alpha"

    main_version, *release_part = raw_version.split("-")
    release = release_part[0] if release_part else "stable"
    parts = main_version.split(".")
    
    return {
        "major": int(parts[0]) if len(parts) > 0 else 0,
        "minor": int(parts[1]) if len(parts) > 1 else 0,
        "patch": int(parts[2]) if len(parts) > 2 else 0,
        "release": release,
        "full": raw_version
    }
