from cache import build_word_cache
from sonnet import generate_sonnet
from scrape import get_sonnets_from_files
import random



def gen_cache(text, times=0):
    base_cache = build_word_cache(text)
    if times <= 0: return base_cache

    new_text = []
    for i in range(150):
        new_text.append(generate_sonnet(base_cache))

    all_text = new_text + text
    random.shuffle(all_text)
    return gen_cache(all_text, times - 1)


if __name__ == '__main__':
    cache = build_word_cache(get_sonnets_from_files())
    print(generate_sonnet(cache))
