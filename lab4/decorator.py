class Furniture():
    """
    Базовый интерфейс Компонента определяет поведение, которое изменяется
    декораторами.
    """
    def operation(self) -> str:
        pass


class Furniture(Furniture):
    """
       Конкретные Компоненты предоставляют реализации поведения по умолчанию. Может
       быть несколько вариаций этих классов.
       """
    def operation(self) -> str:
        return "Furniture"


class Decorator(Furniture):
    """Основная цель этого класса - определить интерфейс обёртки для
    всех конкретных декораторов. Реализация кода обёртки по умолчанию может
    включать в себя поле для хранения завёрнутого компонента и средства его
    инициализации.
    """
    _component: Furniture = None

    def __init__(self, component: Furniture) -> None:
        self._component = component

    @property    #превращает метод класса в атрибут класса.
    def component(self) -> str:
        return self._component

    def operation(self) -> str:
        return self._component.operation()


class Chair(Decorator):
    def operation(self) -> str:
        return f"Chair({self.component.operation()})"


class Armchair(Decorator):
    def operation(self) -> str:
        return f"Armchair({self.component.operation()})"


def show(component: Furniture) -> None:
    print(f"RESULT: {component.operation()}", end="")


if __name__ == "__main__":
    # Таким образом, клиентский код может поддерживать как простые компоненты...
    simple = Furniture()
    print("Client: I've got a simple component:")
    show(simple)
    print("\n")
    # ...так и декорированные.
    #
    # Декораторы могут обёртывать не только простые
    # компоненты, но и другие декораторы.
    decorator1 = Chair(simple)
    decorator2 = Armchair(decorator1)
    print("Client: Now I've got a decorated component:")
    show(decorator2)