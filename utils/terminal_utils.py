import platform
import subprocess
import sys


class TerminalUtils:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TerminalUtils, cls).__new__(cls)
        return cls._instance

    @staticmethod
    def clear() -> None:
        if platform.system() == "Windows":
            if platform.release() in {"10", "11"}:
                subprocess.run("", shell=True)
                print("\033c", end="")
            else:
                subprocess.run(["cls"])
        else:
            print("\033c", end="")
        sys.stdout.flush()


terminal = TerminalUtils()
