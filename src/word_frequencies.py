#!/usr/bin/env python3

def word_frequencies(filename):
    pass

def main():
    d = word_frequencies("src/alice.txt")

    print("Occurrences of 'creating':", d["creating"])
    print("Occurrences of 'Carroll': ", d["Carroll"])
    print("Occurrences of 'sleepy':  ", d["sleepy"])
    print("Occurrences of 'Rabbit':  ", d["Rabbit"])
    print("Number of distinct words:", len(d))


if __name__ == "__main__":
    main()
