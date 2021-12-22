import click
from log import bake, delivery_, pickup
from pizza import BasePizza, Margherita, Pepperoni, Hawaiian
from random import randint


@click.group()
def cli():
    pass


@cli.command()
def menu():
    print('Меню: ')
    print('Можно выбрать один из двух размеров: ')
    print('Средний - "L" или Большой - "XL"')
    print()
    print("Пиццы: ")

    pizzas = [Margherita(),
              Hawaiian(),
              Pepperoni()]

    for pizza in pizzas:
        print(pizza.name, end = ': ')
        print(' '.join(pizza.ingredients.keys()))


@cli.command()
@click.option("--delivery", default=False, is_flag=False)
@click.argument('pizza', nargs=1)
@click.argument('size', nargs=1)
def order(pizza: str, size: str, delivery: bool):
    """Готовит и доставляет пиццу"""
    pizza = pizza.lower()
    if pizza == 'pepperoni':
        pizza = Pepperoni(size = size)
    elif pizza == 'margherita':
        pizza = Margherita(size = size)
    elif pizza == 'hawaiian':
        pizza = Hawaiian(size = size)
    print(bake(pizza))
    if delivery:
        print(delivery_(pizza))
    else:
        print(pickup(pizza))


if __name__ == "__main__":
    cli()