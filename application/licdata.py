import sys
import inspect
import pkgutil
import os
sys.path.insert(0, "domain")
from client_repo import ClientRepo
from incident_repo import IncidentRepo
from license_repo import LicenseRepo
from order_repo import OrderRepo
from pc_repo import PcRepo
from prelicense_repo import PrelicenseRepo
from product_repo import ProductRepo
from product_type_repo import ProductTypeRepo
for folder in os.scandir("infrastructure"):
    if folder.is_dir():
        sys.path.insert(0, folder.path)


def get_repo_interfaces():
    repos = []
    for _, name, _ in pkgutil.iter_modules(path=["domain"]):
        if name != "this":
            try:
                module = __import__(name)
                for class_name, cls in inspect.getmembers(module, inspect.isclass):
                    if (inspect.getmodule(cls) == module and
                        issubclass(cls, Repo) and
                        cls != Repo):
                        repos.append(cls)
            except ImportError:
                pass
    return repos


def get_implementations(interface):
    implementations = []
    for _, name, _ in pkgutil.iter_modules(path=sys.path):
        if name != "this":
            try:
                module = __import__(name)
                for class_name, cls in inspect.getmembers(module, inspect.isclass):
                    if (inspect.getmodule(cls) == module and
                        issubclass(cls, interface) and
                        cls != interface):
                        implementations.append(cls)
            except ImportError:
                pass
    return implementations

class Licdata():

    _singleton = None


    def __init__(self):
        self._repos = {}


    def get_repo(self, cls):
        return self._repos[cls]


    @classmethod
    def initialize(cls):
        cls._singleton = Licdata()
        for repo in get_repo_interfaces():
            cls._singleton._repos[repo] = get_implementations(repo)[0]
            print(f"Bound {repo} to {cls._singleton._repos[repo]}")


    @classmethod
    def instance(cls):
        return cls._singleton


Licdata.initialize()
