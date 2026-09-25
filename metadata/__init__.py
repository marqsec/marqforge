"""
MarqForge Framework
~~~~~~~~~~~~~~~~~~~
Web security discovery framework.
"""

from typing import List
from .author import get_author
from .license import get_license
from .project import get_project
from .runtime import get_runtime
from .version import get_version

__all__: List[str] = [
    "get_author",
    "get_license",
    "get_project",
    "get_runtime",
    "get_version",
]

try:
    __version__ = get_version()["full"]
    __author__ = get_author()["name"]
except Exception:
    __version__ = "0.1.0-alpha"
    __author__ = "Marq"
