from random import randint
import click


class Pizza:
    """
    базовые параметры пиццы
    """
    def __init__(self, size):
        if not (size == 'L' or size == 'XL'):
            raise ValueError('Выберите размер: L/XL')


class Margherita(Pizza):
    """Рецепт пиццы Маргарита"""
    recipe = {
        'Margherita 🧀': ['tomato sauce', 'mozzarella', 'tomatoes']
    }

    def __init__(self, size):
        super().__init__(size)

    @staticmethod
    def __dict__():
        return Margherita.recipe


class Pepperoni(Pizza):
    """Рецепт пиццы Пипперони"""
    recipe = {
        'Pepperoni 🍕': ['tomato sauce', 'mozzarella', 'pepperoni']
    }

    def __init__(self, size):
        super().__init__(size)

    @staticmethod
    def __dict__():
        return Pepperoni.recipe


class Hawaiian(Pizza):
    """Рецепт пиццы Гавайская"""
    recipe = {
        'Hawaiian 🍍': ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']
    }

    def __init__(self, size):
        super().__init__(size)

    @staticmethod
    def __dict__():
        return Hawaiian.recipe


def log(text):
    """Выводит рандомное время выполнения"""
    def decorator(function):
        def wrapper(*args, **kwargs):
            function(*args, **kwargs)
            time = randint(1, 60)
            print(text.format(str(time)))
        return wrapper
    return decorator


@log('🍳 Готовили {}с!')
def bake(pizza_: str) -> int:
    """Готовит пиццу, возвращает время приготовления"""
    return randint(1, 60)


@log('🛵 Доставили за {}с!')
def delivery(pizza_: str) -> int:
    """Доставляет пиццу, возвращает время доставки"""
    return randint(1, 60)


@log('🏠 Забрали за {}с!')
def pickup(pizza_: str) -> int:
    """Самовывоз"""
    return randint(1, 60)


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery_', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery_):
    """Готовит и доставляет пиццу"""
    if pizza == 'Margherita' or pizza == 'Pepperoni' or pizza == 'Hawaiian':
        bake(pizza)
        if delivery_:
            delivery(pizza)
        else:
            pickup(pizza)
    else:
        click.echo('Margherita, Pepperoni, Hawaiian only!')



@cli.command()
def menu():
    """Выводит меню"""
    pizzaM = Margherita("L")
    pizzaP = Pepperoni("L")
    pizzaH = Hawaiian("L")
    click.echo(pizzaM.__dict__())
    click.echo(pizzaH.__dict__())
    click.echo(pizzaP.__dict__())


if __name__ == '__main__':
    cli()