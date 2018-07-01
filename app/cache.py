# Build Cache
import re

START = '__START'
END = '__END'

'''
Parse Sonnet
'''
def parseSonnet(sonnet):
    sonnet = re.sub(r'([\.,:;!\+&]+)', r' \1 ', sonnet)
    sonnet = re.sub(r'\s+', ' ', sonnet)
    return sonnet.split(' ')

'''
Is End Punc
'''
def isEndPunc(word):
    if word in ['.', '!', '?']:
        return True
    return False

'''
Parse Word
'''
def parseWord(word):
    word = word.lower()
    return re.sub(r'[\-\'"]', '', word)


'''
Build Word Cache
'''
def build_word_cache(sonnets):
    # Create the base word cache, which is a dictionary of every word used
    word_cache = {}

    # Set up word and prev_word for parsing
    word = ''
    prev_word = START

    # Go through each input sonnet and build word_cache
    for sonnet in sonnets:
        parsed_sonnet = parseSonnet(sonnet)

        # Go through each word in the parsed_sonnet and add it to word_cache
        for index, word in enumerate(parsed_sonnet):
            # Set the entry on word_cache for the prev_word
            # Check for:
            # count
            # next_words
            # original_words
            if not prev_word in word_cache:
                word_cache[prev_word] = {}
            if not 'count' in word_cache[prev_word]:
                word_cache[prev_word]['count'] = 1
            else:
                word_cache[prev_word]['count'] += 1
            if not 'next_words' in word_cache[prev_word]:
                word_cache[prev_word]['next_words'] = {}
            if not 'original_words' in word_cache[prev_word]:
                word_cache[prev_word]['original_words'] = {}

            # Set word
            word = parsed_sonnet[index]

            # Check if the current word is the end of a line
            if index == len(parsed_sonnet) or isEndPunc(word):
                if not END in word_cache[prev_word]['next_words']:
                    word_cache[prev_word]['next_words'][END] = 0
                word_cache[prev_word]['next_words'][END] += 1
                if not END in word_cache:
                    word_cache[END] = {}
                if not 'count' in word_cache[END]:
                    word_cache[END]['count'] = 1
                else:
                    word_cache[END]['count'] += 1
                if not 'next_words' in word_cache[END]:
                    word_cache[END]['next_words'] = {}
                if not 'original_words' in word_cache[END]:
                    word_cache[END]['original_words'] = {}

                # Set Previous Word
                prev_word = START
            else:
                # Otherwise parse the word add it to word_cache
                parsed_word = parseWord(word)

                if parsed_word:
                    # Parse the word in the same way we did both times above
                    if not parsed_word in word_cache[prev_word]['next_words']:
                        word_cache[prev_word]['next_words'][parsed_word] = 1
                    else:
                        word_cache[prev_word]['next_words'][parsed_word] += 1
                    if not parsed_word in word_cache:
                        word_cache[parsed_word] = {}
                    if not 'count' in word_cache[parsed_word]:
                        word_cache[parsed_word]['count'] = 0
                    if not 'original_words' in word_cache[parsed_word]:
                        word_cache[parsed_word]['original_words'] = {}
                    if not 'next_words' in word_cache[parsed_word]:
                        word_cache[parsed_word]['next_words'] = {}
                    if not word in word_cache[parsed_word]['original_words']:
                        word_cache[parsed_word]['original_words'][word] = 0
                    else:
                        word_cache[parsed_word]['original_words'][word] += 1

                    # Set Previous Word
                    prev_word = parsed_word

        # After creating the base for the word_cache it must be filled in
        for key in word_cache:
            node = word_cache[key]
            cumulative_frequency = 0
            for next_word in node['next_words']:
                freq = node['next_words'][next_word]
                cumulative_frequency += freq

            _sum = 0
            for next_word in node['next_words']:
                freq = node['next_words'][next_word]
                _sum += freq
                node['next_words'][next_word] = {
                    'word': next_word,
                    'frequency': freq,
                    'weight': freq / cumulative_frequency,
                    'cumulative_weight': _sum / cumulative_frequency,
                    'node': word_cache[next_word]
                }

        word_cache[START]['next_words'].pop(END, None)
        return word_cache
