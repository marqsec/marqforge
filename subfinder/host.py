from typing import Dict, Any, Optional, List
from terminal import Commandline
from configure.cfgtools import Tools
from urllib.parse import urlparse

class Checkhost:
    def __init__(self, domain: str = "marqsec.id") -> None:
        self.domain: str = urlparse(domain).netloc
        self.cmd = Commandline()
        
        