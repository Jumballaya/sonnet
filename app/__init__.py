from cache import build_word_cache
from sonnet import generate_sonnet
from scrape import get_sonnets_from_files


if __name__ == '__main__':
    cache = build_word_cache(get_sonnets_from_files())
    print(generate_sonnet(cache))
