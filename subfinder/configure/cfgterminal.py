from typing import List, TypeAlias

CommandPattern: TypeAlias = List[str]
AllowlistConfig: TypeAlias = List[CommandPattern]
ALLOWED_COMMANDS: AllowlistConfig = [
    ["host"],
]
