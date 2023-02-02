#!/usr/bin/python3
'''
Recursively querying the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords (case-insensitive, delimited
by spaces. Javascript should count as javascript, but java should not)
'''
import json
import requests


def count_words(subreddit, word_list, after="", count=[]):
    '''
    Recursive function that queries the Reddit API, parses the title
    of all hot articles, and prints a sorted count of given keywords
    '''

    if after == "":
        count = [0] * len(word_list)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    request = requests.get(url,
                           params={'after': after},
                           allow_redirects=False,
                           headers={'user-agent': 'bhalut'})

    if request.status_code == 200:
        data = request.json()

        for topic in (data['data']['children']):
            for word in topic['data']['title'].split():
                for n in range(len(word_list)):
                    if word_list[n].lower() == word.lower():
                        count[n] += 1

        after = data['data']['after']
        if after is None:
            save = []
            for n in range(len(word_list)):
                for m in range(n + 1, len(word_list)):
                    if word_list[n].lower() == word_list[m].lower():
                        save.append(m)
                        count[n] += count[m]

            for n in range(len(word_list)):
                for m in range(n, len(word_list)):
                    if (count[m] > count[n] or
                            (word_list[n] > word_list[m] and
                             count[m] == count[n])):
                        temp = count[n]
                        count[n] = count[m]
                        count[m] = temp
                        temp = word_list[n]
                        word_list[n] = word_list[m]
                        word_list[m] = temp

            for n in range(len(word_list)):
                if (count[n] > 0) and n not in save:
                    print("{}: {}".format(word_list[n].lower(), count[n]))
        else:
            count_words(subreddit, word_list, after, count)
