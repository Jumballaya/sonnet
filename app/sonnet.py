# Sonnet
import random
from app.cache import START, END

'''
To Original Words
'''
def to_original_words(line, word_cache):
    def choose_original(choices):
        word_list = list(choices.keys())
        word_count = 0
        for v in choices.values():
            word_count += v
        r = random.uniform(0, 1) * word_count
        s = 0
        for word in choices:
            count = choices[word]
            s += count
            if r < s: return word
        return word_list[0]

    original = []
    for word in line:
        choices = word_cache[word]['original_words']
        original.append(choose_original(choices))

    return original

'''
Generate Sonnet
'''
def generate_sonnet(word_cache):

    def choose_next(word):
        node = word_cache[word]
        r = random.uniform(0, 1)
        next_words = node['next_words']
        next_word_list = list(next_words.keys())

        for i, next_word in enumerate(next_word_list):
            info = next_words[next_word]
            if info['cumulative_weight'] >= r:
                return next_word

    def generate_line(min_length):
        word = START
        line = []
        length = 0
        for i in range(30):
            word = choose_next(word)
            length += len(word)
            if (len(line) + length - 1) > 30: return line
            if word == END: break
            line.append(word)
        if len(line) < min_length: return generate_line(min_length)
        return line

    sonnet = []
    for i in range(random.randint(4, 16)):
        line = generate_line(30)
        line = to_original_words(line, word_cache)
        finished = ''
        for w in line:
            if w in ['.', '?', '!', ',', ':', ';']:
                finished += w
            else:
                finished += ' ' + w
        sonnet.append(finished.strip())
    return '\n'.join(sonnet)
