import pytest
from pizza import BasePizza, Margherita, Pepperoni, Hawaiian
from log  import bake, delivery_, pickup
from unittest.mock import patch
import random
from click.testing import CliRunner
from cli import order, menu

def test_dict():
    """Тестирует свойство ingredient, которое выводит рецепт"""
    assert Hawaiian(size="L").dict() == {
        '🥫 tomato sauce': 50,
        '🧀 mozzarella': 100,
        '🍗 chicken': 50,
        '🍍 pineapples': 50,
    }
    assert Pepperoni(size="XL").dict() == {
        '🥫 tomato sauce': 75,
        '🧀 mozzarella': 150,
        '🍪 pepperoni': 75,
    }
    assert "🍅 tomatoes" in Margherita().dict()


def test_eq():
    """Тестирует метод eq, который сравнивает пиццы между собой на основании состава и размера"""
    assert Pepperoni(size="XL") == Pepperoni(size="XL")
    assert Pepperoni(size="L") != Pepperoni(size="XL")
    assert Pepperoni(size="XL") != Hawaiian(size="XL")
    assert Pepperoni(size="XL") != Margherita(size="L")


def test_bake():
    """Тестирует функцию bake"""
    my_number = 5
    with patch.object(random, "randint", return_value = my_number):
        assert (
            bake(Pepperoni()) == '🍳Готовит пиццу за 5 мин ⏳!'
        )


def test_delivery_():
    """Тестирует функцию delivery_"""
    my_number = 42
    with patch.object(random, "randint", return_value = my_number):
        assert (
            delivery_(Pepperoni()) == '🚚Доставляет пиццу за 42 мин ⏳!'
        )


def test_pickup():
    """Тестирует функцию pickup"""
    my_number = 20
    with patch.object(random, "randint", return_value = my_number):
        assert (
            pickup(Pepperoni()) == '🏃Самовывоз пиццы через 20 min ⌛!'
        )


def test_menu():
    """Тестирует функцию menu"""
    runner = CliRunner()
    result = runner.invoke(menu)
    assert (
        result.output == 'Меню: \n' +
        'Можно выбрать один из двух размеров: \n' +
        'Средний - "L" или Большой - "XL"\n' +
        '\n' +
        'Пиццы: \n' +
        'Margherita 🧀: 🥫 tomato sauce 🧀 mozzarella 🍅 tomatoes\n' +
        'Hawaiian 🍍: 🥫 tomato sauce 🧀 mozzarella 🍗 chicken ' +
        '🍍 pineapples\n' +
        'Pepperoni 🍕: 🥫 tomato sauce 🧀 mozzarella 🍪 pepperoni\n'
    )
