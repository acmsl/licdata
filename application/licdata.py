import sys
from injector import Injector
import inspect
import pkgutil
import os
sys.path.insert(0, "domain")
from client_repo import ClientRepo
for folder in os.scandir("infrastructure"):
    if folder.is_dir():
        sys.path.insert(0, folder.path)


class Licdata():

    _singleton = None


    def __init__(
            self,
            clientRepo: ClientRepo,
            licenseRepo: LicenseRepo,
            orderRepo: OrderRepo,
            pcRepo: PcRepo,
            prelicenseRepo: PrelicenseRepo,
            productTypeRepo: ProductTypeRepo,
            productRepo: ProductRepo
    ):
        self._clientRepo = clientRepo
        self._licenseRepo = licenseRepo
        self._orderRepo = orderRepo
        self._pcRepo = pcRepo
        self._prelicenseRepo = prelicenseRepo
        self._productTypeRepo = productTypeRepo
        self._productRepo = productRepo


    @property
    def clientRepo(self):
        return self._clientRepo


    @property
    def licenseRepo(self):
        return self._licenseRepo


    @property
    def orderRepo(self):
        return self._orderRepo


    @property
    def orderRepo(self):
        return self._orderRepo


    @property
    def pcRepo(self):
        return self._pcRepo


    @property
    def prelicenseRepo(self):
        return self._prelicenseRepo


    @property
    def productTypeRepo(self):
        return self._productTypeRepo


    @property
    def productRepo(self):
        return self._productRepo


    @classmethod
    def initialize(
            cls,
            clientRepo: ClientRepo,
            licenseRepo: LicenseRepo,
            orderRepo: OrderRepo,
            pcRepo: PcRepo,
            prelicenseRepo: PrelicenseRepo,
            productTypeRepo: ProductTypeRepo,
            productRepo: ProductRepo
    ):
        cls._singleton = Licdata(
            clientRepo,
            licenseRepo,
            orderRepo,
            pcRepo,
            prelicenseRepo,
            productTypeRepo,
            productRepo)


    @classmethod
    def instance(cls):
        return cls._singleton


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

injector = Injector()
injector.binder.bind(ClientRepo, to=get_implementations(ClientRepo)[0])
injector.binder.bind(LicenseRepo, to=get_implementations(LicenseRepo)[0])
injector.binder.bind(OrderRepo, to=get_implementations(OrderRepo)[0])
injector.binder.bind(PcRepo, to=get_implementations(PcRepo)[0])
injector.binder.bind(PrelicenseRepo, to=get_implementations(PrelicenseRepo)[0])
injector.binder.bind(ProductTypeRepo, to=get_implementations(ProductTypeRepo)[0])
injector.binder.bind(ProductRepo, to=get_implementations(ProductRepo)[0])
Licdata.initialize(injector.get(ClientRepo))
