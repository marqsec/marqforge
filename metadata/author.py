from importlib.metadata import metadata, PackageNotFoundError
from typing import Dict, Any

PACKAGE_NAME = "marqforge"

def get_author() -> Dict[str, Any]:
    try:
        meta = metadata(PACKAGE_NAME)
        raw_author = meta.get("Author", "Marq")
        if "(" in raw_author and ")" in raw_author:
            name, org_part = raw_author.split("(", 1)
            name = name.strip()
            organization = org_part.replace(")", "").strip()
        else:
            name = raw_author
            organization = "Paguyuban Warga Comatcommit (PWC)"
            
    except PackageNotFoundError:
        name = "Marq"
        organization = "Paguyuban Warga Comatcommit (PWC)"

    return {
        "name": name,
        "organization": organization,
    }
