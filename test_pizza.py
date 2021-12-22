import pytest
from pizza import BasePizza, Margherita, Pepperoni, Hawaiian
from log  import bake, delivery_, pickup
from unittest.mock import patch
import random
from click.testing import CliRunner
from cli import order, menu

def test_dict():
    """Тестирует свойство ingredient, которое выводит рецепт"""
    assert Hawaiian(size="L").ingredient == {
        "🥫 tomato sauce": 50,
        "🧀 mozzarella": 100,
        "🍗 chicken": 50,
        "🍍 pineapples": 50,
    }
    assert Pepperoni(size="XL").ingredient == {
        "🥫 tomato sauce": 75,
        "🧀 mozzarella": 150,
        "🍪 pepperoni": 105,
    }
    assert "🍅 tomatoes" in Margherita().ingredient


def test_eq():
    """Тестирует метод eq, который сравнивает пиццы между собой на основании состава и размера"""
    assert Pepperoni(size="XL") == Pepperoni(size="XL")
    assert Pepperoni(size="L") != Pepperoni(size="XL")
    assert Pepperoni(size="XL") != Hawaiian(size="XL")
    assert Pepperoni(size="XL") != Margherita(size="L")


def test_bake():
    """Тестирует функцию bake"""
    my_number = 4
    with patch.object(random, "randint", return_value = my_number):
        assert (
            bake(Pepperoni()) == "🍳Готовит пиццу за 4 мин ⏳!"
        )


def test_delivery_():
    """Тестирует функцию delivery_"""
    my_number = 4
    with patch.object(random, "randint", return_value = my_number):
        assert (
            delivery_(Pepperoni()) == "🚚Доставляет пиццу за 4 мин ⏳!"
        )


def test_pickup():
    """Тестирует функцию pickup"""
    my_number = 4
    with patch.object(random, "randint", return_value = my_number):
        assert (
            pickup(Pepperoni()) == "🏃Самовывоз пиццы через 4 min ⌛!"
        )


def test_menu():
    """Тестирует функцию menu"""
    runner = CliRunner()
    result = runner.invoke(menu)
    assert (
        result.output == 'Меню: \n' +
        'Можно выбрать один из двух размеров: \n' +
        'Средний - "L" или Большой - "XL"\n' +
        "\n" +
        "Пиццы: \n" +
        "Margherita 🧀: 🥫 tomato sauce 🧀 mozzarella 🍅 tomatoes\n" +
        "Hawaiian 🍍: 🥫 tomato sauce 🧀 mozzarella 🍗 chicken " +
        "🍍 pineapples\n" +
        "Pepperoni 🍕: 🥫 tomato sauce 🧀 mozzarella 🍪 pepperoni\n"
    )