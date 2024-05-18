import subprocess,platform

class TerminalUtils:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TerminalUtils, cls).__new__(cls)
        return cls._instance
    

    @staticmethod
    def clear() -> None:
        if platform.system()=="Windows":
            if platform.release() in {"10", "11"}:
                subprocess.run("", shell=True) #Needed to fix a bug regarding Windows 10; not sure about Windows 11
                print("\033c", end="")
            else:
                subprocess.run(["cls"])
        else: #Linux and Mac
            print("\033c", end="")

terminal = TerminalUtils()