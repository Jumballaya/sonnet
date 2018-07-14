from cache import build_word_cache
from sonnet import generate_sonnet
from data import Sonnets


if __name__ == '__main__':
    cache = build_word_cache(Sonnets)
    print(generate_sonnet(cache))
