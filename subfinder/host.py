from typing import Dict, Any, Optional, List
from unittest import result
from terminal import Commandline
from configure.cfgtools import Tools
from urllib.parse import urlparse

class Checkhost:
    def __init__(self, domain: str = "marqsec.id") -> None:
        self.domain: str = urlparse(domain).netloc
        self.cmd = Commandline()
        self.listhost_active: List[Dict[str, Any]] = []
        
    def check(self):
        result = self.cmd.execute(Tools("marqsec.id").host)
        
        