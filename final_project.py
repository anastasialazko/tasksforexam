from random import randint
import click


class Pizza:
    """
    базовые параметры пиццы
    """
    def __init__(self, name: str, size: str):
        if not (size == 'L' or size == 'XL'):
            raise ValueError('Choose the size of pizza: L/XL')
        if not (name == 'Margherita' or name == 'Pepperoni' or name == 'Hawaiian'):
            raise ValueError('Choose pizza from menu: Margherita, Pepperoni или Hawaiian')

        self.name = name
        self.ingredients = ['tomato sauce', 'mozzarella']

        if name == 'Margherita':
            self.name = '{0}{1}'.format(self.name, ' 🍕')
            self.ingredients.append('tomatoes')

        if name == 'Pepperoni':
            self.name = '{0}{1}'.format(self.name, ' 🧀')
            self.ingredients.append('pepperoni')

        if name == 'Hawaiian':
            self.name = '{0}{1}'.format(self.name, ' 🍍')
            self.ingredients.append('chicken')
            self.ingredients.append('pineapples')

        def dict(self):
            """Выводит рецепт"""
            recipe = {self.name: ', '.join(x for x in self.ingredients)}
            return recipe


def log(text):
    """Выводит время выполнения"""
    def decorator(function):
        def wrapper(*args, **kwargs):
            function(*args, **kwargs)
            time = randint(1, 60)
            print(text.format(str(time)))
        return wrapper
    return decorator


@log('🍳 Готовили {}с!')
def bake(pizza: str, size: str) -> int:
    """Готовит пиццу, возвращает время приготовления"""
    return randint(1, 60)


@log('🛵 Доставили за {}с!')
def delivery(pizza: str, size: str) -> int:
    """Доставляет пиццу, возвращает время доставки"""
    return randint(1, 60)


@log('🏠 Забрали за {}с!')
def pickup(pizza: str, size: str) -> int:
    """Самовывоз"""
    return randint(1, 60)


@click.group()
def cli():
    pass


@cli.command()
@click.option('=delivery_', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
@click.argument('size', default='L')
def order(pizza: str, size: str, delivery_: bool):
    """Готовит и доставляет пиццу"""
    if pizza == 'Margherita' or pizza == 'Pepperoni' or pizza == 'Hawaiian':
        bake(pizza, size)
        if delivery_:
            delivery(pizza, size)
        else:
            pickup(pizza, size)
    else:
        click.echo('Margherita, Pepperoni, Hawaiian only!')



@cli.command()
def menu():
    """Выводит меню"""
    pizzas = [Pizza('Margherita', 'L'), Pizza('Pepperoni', 'L'), Pizza('Hawaiian', 'L')]
    for pizza in pizzas:
       print(f'{pizza.name}: ' + ', '.join(x for x in pizza.ingredients))
    print('All kinds of pizza have L or XL size')


if __name__ == '__main__':
    cli()
