import string
import numpy

from matplotlib import pyplot
from collections import Counter

from app.data import Sonnets


def calculate_frequency(text):
    text = [c.upper() for c in text if c.upper() in string.ascii_uppercase]
    frequency = Counter(text)
    listed_items = frequency.items()
    listed_items = sorted(listed_items, key=lambda x: x[1], reverse=True)
    return list(zip(*listed_items))

def plot_graph(subplot, title, text, color):
    letters, frequency = calculate_frequency(text)
    index = numpy.arange(len(letters))
    bar_width = 0.5

    subplot.bar(index, frequency, bar_width, color=color)
    subplot.set_xticks(index)
    subplot.set_xticklabels(letters)
    subplot.set_ylabel('Frequency')
    subplot.set_title(title)

def save_graph(subplot, title, text, color, fig):
    letters, frequency = calculate_frequency(text)
    index = numpy.arange(len(letters))
    bar_width = 0.5
    subplot.bar(index, frequency, bar_width, color=color)
    subplot.set_xticks(index)
    subplot.set_xticklabels(letters)
    subplot.set_ylabel('Frequency')
    subplot.set_title(title)
    fig.savefig('data/' + str(title) + '.png')



def analyze_texts(texts):
    full = ''
    for t in texts:
        full += texts[t]
        fig = pyplot.figure()
        ax1 = fig.add_subplot(2, 1, 1)
        print('Creating graph for Sonnet #' + str(t))
        save_graph(ax1, "Sonnet - " + str(t), texts[t], "blue", fig)

    fig = pyplot.figure()
    ax1 = fig.add_subplot(2, 1, 1)
    print('Creating graph for all Sonnets')
    save_graph(ax1, "Every Sonnet", full, "orange", fig)


def run():
    analyze_texts(Sonnets)

run()
