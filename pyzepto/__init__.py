import os
import sys
import imp
import subprocess

def zepto(code):
    code = code[-1] if code.endswith("\n") else code
    code = "(begin {})".format(code)
    ret = subprocess.check_output(["zepto", "-s", code]).decode("utf-8")
    ret = ret.split("\n")
    output = "\n".join(ret[:-2])
    ret = ret[-2]
    print(output)
    return ret

def _install_importer():
    """Installs the module finder."""
    sys.meta_path.insert(0, Finder())

class Finder:
    """Custom module finder for zepto files."""
    @classmethod
    def find_module(cls, fullname, path):
        for dirname in sys.path:
            filename = os.path.join(dirname, fullname)
            if os.path.exists(filename):
                return ZeptoLoader(filename)
            elif os.path.exists(filename + ".zp"):
                return ZeptoLoader(filename + ".zp")

class ZeptoLoader:
    """Custom module loader for zepto files."""
    def __init__(self, filename):
        self.filename = filename

    def load_module(self, fullname):
        if fullname in sys.modules:
            mod = sys.modules[fullname]
        else:
            mod = imp.new_module(fullname)
            sys.modules[fullname] = mod
        mod.__file__ = self.filename
        mod.__loader__ = self
        with open(self.filename) as f:
            zepto(f.read())
        return

_install_importer()
