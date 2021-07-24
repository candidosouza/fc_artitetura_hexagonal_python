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


@ProductInterface.register
class Product:
    def __str__(self) -> str:
        return f'Product'
    
    def is_valid() -> bool:
        pass

    def enable() -> bool:
        pass

    def disable() -> bool:
        pass

    def get_id() -> str:
        pass

    def get_name() -> str:
        pass

    def get_status() -> str:
        pass

    def get_price() -> str:
        pass




print(issubclass(Product, ProductInterface))
