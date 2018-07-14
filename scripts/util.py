from scrape import get_sonnets, get_titles
import os


def avg_sonnet_char_length():
    sonnets = get_sonnets()
    total = 0

    for s in sonnets:
        total += len(s)

    return total / len(sonnets)

def save_sonnets():
    sonnets = get_titles()

    for title in sonnets:
        text = sonnets[title]
        path = os.path.abspath('sonnets/' + title + '.txt')
        print("Saving: " + path)
        with open(path, 'w+') as f:
            f.write(text)

if __name__ == '__main__':
    save_sonnets()
