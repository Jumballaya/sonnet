from app.cache import build_word_cache
from app.sonnet import generate_sonnet
from app.data import Sonnets


def generate():
    s = list(Sonnets.values())
    sonnets = []
    for sonnet in s:
        sonnets.extend(sonnet.split('\n'))
    cache = build_word_cache([" ".join(sonnets)])

    return generate_sonnet(cache)
