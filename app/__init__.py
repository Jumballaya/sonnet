from cache import build_word_cache
from sonnet import generate_sonnet
from data import Sonnets


if __name__ == '__main__':
    s = list(Sonnets.values())
    sonnets = []
    for sonnet in s:
        sonnets.extend(sonnet.split('\n'))
    cache = build_word_cache([" ".join(sonnets)])

    print(generate_sonnet(cache))
