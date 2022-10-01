from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):

    @property  # property позволяет превратить метод класса в атрибут класса

    @abstractmethod  # Абстрактным называется объявленный, но не реализованный метод
    def product(self) -> None:
        pass

    @abstractmethod  # Абстрактным называется объявленный, но не реализованный метод
    def wardrobe(self) -> None:  # шкаф
        pass

    @abstractmethod
    def chair(self) -> None:  # стул
        pass

    @abstractmethod
    def bed(self) -> None:  # кровать
        pass


class Furniture_Builder(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Shop()

    @property  # property позволяет превратить метод класса в атрибут класса
    def product(self) -> Shop:
        product = self._product
        self.reset()
        return product

    def wardrobe(self) -> None:
        self._product.add("шкаф")

    def chair(self) -> None:
        self._product.add("стул")

    def bed(self) -> None:
        self._product.add("кровать")


class Shop():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"В магазине продаются: {', '.join(self.parts)}", end="")


class Director:

    def __init__(self) -> None:
        self._builder = None

    @property  # property позволяет превратить метод класса в атрибут класса
    def builder(self) -> Builder:
        return self._builder

    @builder.setter  # применяется сеттер к методу builder, то есть делаем метод доступным для записи
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def Shatura(self) -> None:
        self.builder.chair()
        self.builder.wardrobe()

    def Lasurit(self) -> None:
        self.builder.bed()
        self.builder.chair()


if __name__ == "__main__":
    director = Director()
    builder = Furniture_Builder()
    director.builder = builder

    print("Шатура: ")
    director.Shatura()
    builder.product.list_parts()

    print("\n\nЛазурит: ")
    director.Lasurit()
    builder.product.list_parts()


