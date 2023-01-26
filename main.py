import LogicUnit as LGu

if __name__ == '__main__':
    # LGu.collect_tweets()
    results_es = LGu.get_top_tweets(3)
    for _res in results_es:
        print(_res['_source']['content'])

