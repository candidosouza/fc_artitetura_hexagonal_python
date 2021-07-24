import abc

class ProductInterface(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
                hasattr(subclass, 'is_valid') and
                callable(subclass.is_valid) and
                hasattr(subclass, 'enable') and
                callable(subclass.enable) and
                hasattr(subclass, 'disable') and
                callable(subclass.disable) and
                hasattr(subclass, 'get_id') and
                callable(subclass.get_id) and
                hasattr(subclass, 'get_name') and
                callable(subclass.get_name) and
                hasattr(subclass, 'get_status') and
                callable(subclass.get_status) and
                hasattr(subclass, 'get_price') and
                callable(subclass.get_price) or 
                NotImplemented
        )


DISABLED = "disabled"
ENABLE = "enable"


@ProductInterface.register
class Product:
    def __init__(self):
        pass

    def __str__(self) -> str:
        return f'Product'
    
    def is_valid(self) -> bool:
        pass

    def enable(self) -> bool:
        pass

    def disable(self) -> bool:
        pass

    def get_id(self) -> str:
        pass

    def get_name(self) -> str:
        pass

    def get_status(self) -> str:
        pass

    def get_price(self) -> str:
        pass


print(issubclass(Product, ProductInterface))
