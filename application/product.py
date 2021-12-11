import uuid
#https://github.com/CSenshi/Validator
from validator import validate, validate_many

class ProductMeta(type):
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (
            hasattr(subclass, 'id') and callable(subclass.id) and
            hasattr(subclass, 'name') and callable(subclass.name) and
            hasattr(subclass, 'status') and callable(subclass.status) and
            hasattr(subclass, 'price') and callable(subclass.price) and
            hasattr(subclass, 'is_valid') and callable(subclass.is_valid) and
            hasattr(subclass, 'enabled') and callable(subclass.enabled) and
            hasattr(subclass, 'disabled') and callable(subclass.disabled) or
            NotImplemented
        )


class ProductInterface(metaclass=ProductMeta):

    def __str__(self) -> str:
        return 'ProductInterface'

    def id(self):
        pass  # this function is empty

    def name(self) -> str:
        pass  # this function is empty

    def status(self) -> str:
        pass  # this function is empty

    def price(self) -> str:
        pass  # this function is empty

    def is_valid(self) -> bool:
        pass  # this function is empty

    def enabled(self) -> None:
        pass  # this function is empty

    def disabled(self) -> None:
        pass  # this function is empty


DISABLED = "disabled"
ENABLED = "enable"


class Product(ProductInterface):
    __slots__ = ['__id', '__name', '__status', '__price']

    rules = {
        "__name": "required|min:3",
        "__status": "required|min:6|max:9",
        "__price": "required"
    }

    def __init__(self, name, status, price):
        self.__id = uuid.uuid4()
        self.__name = name
        self.__status = status
        self.__price = price

    def __str__(self) -> str:
        return 'Product'

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

    def data(self):
        return {
            "__name": self.name,
            "__status": self.status,
            "__price": self.price
        }

    def is_valid(self) -> bool:
        if self.status == 0:
            self.__status = DISABLED
        if self.status not in [ENABLED, DISABLED]:
            raise ValueError("The status must be enable or disabled")
        if self.price < 0:
            raise ValueError("The price must be greater or equal zero")
        result, validated_data, errors = validate(self.data(), self.rules, return_info=True)
        if not result:
            return errors
        return True

    def enabled(self) -> None:
        if self.__price > 0:
            self.__status = ENABLED
            return None
        raise ValueError(
            "The price must be greater than zero to enable the product")

    def disabled(self) -> None:
        if self.__price == 0:
            self.__status = DISABLED
            return None
        raise ValueError(
            "The price must be zero in order to have the product disabled")

