from importlib.metadata import metadata, PackageNotFoundError
from typing import Dict, Any

PACKAGE_NAME = "marqforge"

def get_project() -> Dict[str, Any]:
    try:
        meta = metadata(PACKAGE_NAME)
        
        name = meta.get("Name", "MarqForge")
        description = meta.get("Summary", "Web security discovery framework")
        author = meta.get("Author", "Marq")
        homepage = meta.get("Home-page")
        repository = None
        if "Project-URL" in meta:
            project_urls = meta.get_all("Project-URL") or []
            for url_entry in project_urls:
                if "repository" in url_entry.lower() or "github" in url_entry.lower():
                    repository = url_entry.split(",")[-1].strip()
                    break

    except PackageNotFoundError:
        name = "MarqForge"
        description = "Web security discovery framework"
        author = "Marq"
        homepage = None
        repository = None

    return {
        "name": name,
        "slug": name.lower().replace(" ", "-"),
        "description": description,
        "author": author,
        "organization": "Paguyuban Warga Comatcommit (PWC)",
        "homepage": homepage,
        "repository": repository,
    }
