from pizza import BasePizza, Margherita, Pepperoni, Hawaiian
import time
import random
from typing import Callable
from functools import wraps


def log(params: str) -> Callable:

    def outer_wrapper(func: Callable) -> Callable:

        def inner_wrapper(pizza: BasePizza) -> str:
            """
            Вставляет случайное чилос в шаблон в зависимости от размера
            """

            if func.__name__ == 'bake':
                if pizza.size == 'XL':
                    return params.format(random.randint(11, 12))
                else:
                    return params.format(random.randint(5, 10))
            elif func.__name__ == 'delivery_':
                return params.format(random.randint(30, 60))
            elif func.__name__ == 'pickup':
                return params.format(random.randint(20, 30))

        return inner_wrapper

    return outer_wrapper


@log('🍳Готовит пиццу за {} мин ⏳!')
def bake(pizza: BasePizza) -> int:
    """Готовит пиццу"""


@log('🚚Доставляет пиццу за {} мин ⏳!')
def delivery_(pizza: BasePizza) -> int:
    """Доставляет пиццу"""


@log('🏃Самовывоз пиццы через {} min ⌛!')
def pickup(pizza: BasePizza) -> int:
    """Самовывоз"""

