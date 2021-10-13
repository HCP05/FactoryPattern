from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    """
    The AbstractFactory class declares the factory method that is supposed to return an
    object of a Product class. The AbstractFactory's subclasses usually provide the
    implementation of this method.
    """

    @abstractmethod
    def factory_method(self):
        """
        Note that the AbstractFactory may also provide some default implementation of
        the factory method.
        """

        pass

    def some_operation(self) -> str:
        """
        Also note that, despite its name, the AbstractFactory's primary responsibility
        is not creating products. Usually, it contains some core business logic
        that relies on Product objects, returned by the factory method.
        Subclasses can indirectly change that business logic by overriding the
        factory method and returning a different type of product from it.
        """

        # Call the factory method to create a Product object.
        product = self.factory_method()

        # Now, use the product.
        result = f"AbstractFactory: The same AbstractFactory's code has just worked with {product.operation()}"

        return result


"""
Concrete AbstractFactorys override the factory method in order to change the resulting
product's type.
"""


class Factory1(AbstractFactory):
    """
    Note that the signature of the method still uses the abstract product type,
    even though the concrete product is actually returned from the method. This
    way the AbstractFactory can stay independent of concrete product classes.
    """

    def factory_method(self) -> Product:
        return Produs1()


class Facory2(AbstractFactory):
    def factory_method(self) -> Product:
        return Produs2()


class Product(ABC):
    """
    The Product interface declares the operations that all concrete products
    must implement.
    """

    @abstractmethod
    def operation(self) -> str:
        pass


"""
Concrete Products provide various implementations of the Product interface.
"""


class Produs1(Product):
    def operation(self) -> str:
        return "{Result of the Produs1}"


class Produs2(Product):
    def operation(self) -> str:
        return "{Result of the Produs2}"


def client_code(AbstractFactory: AbstractFactory) -> None:
    """
    The client code works with an instance of a concrete AbstractFactory, albeit through
    its base interface. As long as the client keeps working with the AbstractFactory via
    the base interface, you can pass it any AbstractFactory's subclass.
    """

    print(f"Client: I'm not aware of the AbstractFactory's class, but it still works.\n"
          f"{AbstractFactory.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the Factory1.")
    client_code(Factory1())
    print("\n")

    print("App: Launched with the Facory2.")
    client_code(Facory2())
