import string
import random
from graph import Graph, Vertex
#step 1: get words from text
#step 2: make a graph using those words
#step 3: get the next word for x number of words (defined by user)
#step 4: show the user!
def get_words_from_text (text_path):
    with open (text_path, 'r') as f:
        text=f.read()
        text = ' '. join (text.split()) #this is saying turn whitespace into just spaces
        text = text.lower()
        text = text.translate (str.maketrans('', '', string.punctuation))
    words = text.split()
    return words

def make_graph(words):
    #for each word, check that word is in the graph, and if not then add it. if there was a previous word, then add an edge if it does not already exist. in the graph, otherwise increment weight by 1, set our word to the previous word and iterate.
    g = Graph()
    previous_word = None
    for word in words:
        word_vertex = g.get_vertex(word)
        if previous_word:
            previous_word.increment_edge(word_vertex)
        previous_word = word_vertex
    g.generate_probability_mappings()
    return g

def compose (g, words, length =50):
    composition = []
    word = g.get_vertex(random.choice(words))
    for _ in range (length):
        composition.append(word.value)
        word = g.get_next_word(word)
    return composition


def main ():
    #get words form text
    words = get_words_from_text ('texts/hp_sorcerer_stone.txt')
    #make a graph using those words
    g = make_graph (words)
    #get the next word for x number of words (defined by user)
    composition = compose(g, words, 100)
    return ' '.join(composition) #returns a string, where all the words are separated by a space!!

if __name__ == '__main__':
    print (main())