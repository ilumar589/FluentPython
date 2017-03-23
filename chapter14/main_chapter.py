from chapter14.sentence_iterable import Sentence


def execute():
    sentence = Sentence("This is a sentence")
    for word in sentence:
        print(word)

execute()