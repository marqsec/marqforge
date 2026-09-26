from typing import List, Optional
from configure.cfgterminal import ALLOWED_COMMANDS
import subprocess

class Commandline:
    def __init__(self) -> None:
        self.allowed_commands = {cmd[0] for cmd in ALLOWED_COMMANDS if cmd}

    def execute(self, cmd_args: List[str], timeout: Optional[float] = None) -> subprocess.CompletedProcess:
        if not cmd_args:
            raise ValueError("Argumen perintah tidak boleh kosong.")

        base_command = cmd_args[0]
        if base_command not in self.allowed_commands:
            raise PermissionError(f"Keamanan Ketat: Perintah '{base_command}' tidak diizinkan untuk dieksekusi!")

        try:
            result = subprocess.run(
                cmd_args,
                shell=False,
                capture_output=True,
                text=True,
                check=True,
                timeout=timeout
            )
            return result

        except subprocess.TimeoutExpired as e:
            raise e
        except subprocess.CalledProcessError as e:
            raise e