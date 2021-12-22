import random
from abc import abstractmethod


class BasePokemon:
    def __init__(self, name: str, poketype: str):
        self.name = name
        self.poketype = poketype

    def __str__(self):
        return f'{self.name}/{self.poketype}'


class AnimeMon:
    @abstractmethod
    def inc_exp(cls, val):
        pass

    @property
    @abstractmethod
    def exp(self):
        return self.__exp

    @exp.setter
    def exp(self, val):
        self.__exp = val


class EmojiMixin:
    emoji = {'grass': '🌿', 'fire': '🔥', 'water': '💧', 'electric': '⚡'}

    def __str__(self):
        text_pocketype = super().__str__()
        return text_pocketype.replace(self.poketype, self.emoji[self.poketype])


class Pokemon(EmojiMixin, BasePokemon, AnimeMon):
    def __init__(self, name: str, poketype: str):
        self.name = name
        self.poketype = poketype
        self.exp = 0

    def inc_exp(self, value: int):
        self.exp += value


class Digimon(AnimeMon):
    def __init__(self, name: str):
        self.name = name
        self.exp = 0

    def __str__(self):
        return f'{self.name}'

    def inc_exp(self, value: int):
        self.exp += value * 8


def train(pokemon: Pokemon):
    step_size, level_size = 10, 100
    sparring_qty = (level_size - pokemon.exp % level_size) // step_size
    for i in range(sparring_qty):
        win = random.choice([True, False])
        if win:
            pokemon.inc_exp(step_size)


if __name__ == '__main__':
    bulbasaur = Pokemon(name='Bulbasaur', poketype='grass')
    print(bulbasaur)
    train(bulbasaur)
    print(bulbasaur.exp)
    agumon = Digimon(name='Agumon')
    train(agumon)
    print(agumon.exp)
