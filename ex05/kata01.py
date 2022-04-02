#! /usr/bin/env python

languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }
    
if __name__ == '__main__':

    for key, val in languages.items():
        print(f"{key} was created by {val}")