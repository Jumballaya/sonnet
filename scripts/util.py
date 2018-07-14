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

def make_file():
    sonnets = get_titles()
    dataFile = os.path.abspath('app/data.py')

    with open(dataFile, 'w+') as f:
        f.write("'''")
        f.write('\n')
        f.write('Sonnets data -- Text of all the sonnets')
        f.write('\n')
        f.write("'''")
        f.write('\n')
        f.write('\n')
        f.write('Sonnets = {')
        f.write('\n')

        for title in sonnets:
            text = sonnets[title]
            f.write('\t"' + title + '":' + "'''" + text + "''',\n")

        f.write('}')



if __name__ == '__main__':
    make_file()
