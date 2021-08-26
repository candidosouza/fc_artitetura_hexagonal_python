import uuid

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
        pass

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

DISABLED = "disabled"
ENABLED = "enable"

class Product(ProductInterface):
    __slots__ = ['__id', '__name', '__status', '__price']

    def __init__(self, name, status, price):
       self.__id = uuid.uuid1()
       self.__name = name
       self.__status = status
       self.__price = price

    def __str__(self) -> str:
        return f'Product'

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def status(self):
        return self.__status

    @property
    def price(self):
        return self.__price

    def is_valid(self) -> bool:
        pass

    def enabled(self) -> None:
        if self.__price > 0:
            self.__status = ENABLED
            return None
        raise ValueError("The price must be greater than zero to enable the product")

    def disabled(self) -> None:
        if self.__price == 0:
            self.__status = DISABLED
            return None
        raise ValueError("The price must be zero in order to have the product disabled")

    @price.setter
    def price(self, value):
        self._price = value


print(issubclass(Product, ProductInterface))
