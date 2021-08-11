
class ProductMeta(type):
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (
            hasattr(subclass, 'id') and callable(subclass.id) and
            hasattr(subclass, 'name') and callable(subclass.name) and
            hasattr(subclass, 'status') and callable(subclass.status) and
            hasattr(subclass, 'price') and callable(subclass.price)and
            hasattr(subclass, 'is_valid') and callable(subclass.is_valid) and
            hasattr(subclass, 'enabled') and callable(subclass.enabled) and
            hasattr(subclass, 'disabled') and callable(subclass.disabled) or
            NotImplemented
        )

class ProductInterface(metaclass=ProductMeta):

    def __str__(self) -> str:
        return f'ProductInterface'

    def id(self):
        return NotImplementedError

    def name(self) -> str:
        pass

    def status(self) -> str:
        pass

    def price(self) -> str:
        pass

    def is_valid(self) -> bool:
        pass

    def enabled(self) -> bool:
        pass

    def disabled(self) -> bool:
        pass


class Product(ProductInterface):
    __slots__ = ['__id', '__name', '__status', '__price']

    DISABLED = "disabled"
    ENABLED = "enable"

    def __init__(self, id, name, status, price):
       self.__id = id
       self.__name = name
       self.__status = status
       self.__price = price

    def __str__(self) -> str:
        return f'Product'

    def id(self):
        return self.__id

    def name(self):
        return self.__name

    def status(self):
        return self.__name

    def price(self):
        return self.__price

    def is_valid(self) -> bool:
        pass

    def enabled(self) -> bool:
        if self.__price > 0:
            self.__status = self.ENABLED
            return True
        raise ValueError("The price must be greater than zero to enable the product")

    def disabled(self) -> bool:
        pass


print(issubclass(Product, ProductInterface))
