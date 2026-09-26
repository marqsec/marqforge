from typing import List, TypeAlias

CommandPattern: TypeAlias = List[str]
ToolsExecute: TypeAlias = List[CommandPattern]

class Tools:
    def __init__(self, domains: List[str]) -> None:
        self.domains = domains

    @property
    def host(self) -> ToolsExecute:
        return [["host", domain] for domain in self.domains]

    