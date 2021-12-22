class BasePizza:
    """
    Базовый класс для всех пицц, предполагается что есть два размера: 'L' и 'XL'
    для размера 'XL' требуется в полтора раза больше ингридиентов чем для размера 'L'
    """

    def __init__(self, dop_ingredients: dict,
                 size: str = 'L', name: str = None):
        self.size = size
        self.name = name
        self.ingredients = {'🥫 tomato sauce': 50, '🧀 mozzarella': 100}
        self.ingredients.update(dop_ingredients)
        if self.size == 'XL':
            self.ingredients = {k: 1.5 * v for k, v in self.ingredients.items()}

    @property
    def ingredient(self) -> dict:
        """
        Функция, возвращающая рецепт пиццы в виде словаря
        """
        return self.ingredients

    def __eq__(self, other) -> bool:
        """
        Функция сравнивает две пиццы, учитывая набор ингридиентов и размер
        """
        return self.size == other.size and self.ingredients == other.ingredients


class Margherita(BasePizza):
    """
    Класс для пиццы Маргарита
    """

    def __init__(self, size: str = "L"):
        self.name = "Margherita 🧀"
        self.dop_ingredients = {"🍅 tomatoes": 75}
        super().__init__(self.dop_ingredients, size, self.name)


class Pepperoni(BasePizza):
    """
    Классдля пиццы Пепперони
    """

    def __init__(self, size: str = "L"):
        self.name = "Pepperoni 🍕"
        self.dop_ingredients = {"🍪 pepperoni": 70}
        super().__init__(self.dop_ingredients, size, self.name)


class Hawaiian(BasePizza):
    """
    Класс для для пиццы Гавайская
    """

    def __init__(self, size: str = "L"):
        self.name = "Hawaiian 🍍"
        self.dop_ingredients = {"🍗 chicken": 50, "🍍 pineapples": 50}
        super().__init__(self.dop_ingredients, size, self.name)