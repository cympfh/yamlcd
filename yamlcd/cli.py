from collections import defaultdict
from glob import glob

import yaml


def insert(data, memo, path, filename):
    if type(data) != dict:
        return
    for key in data:
        fullkey = '.'.join(path + [key])
        memo[fullkey].append(filename)
        insert(data[key], memo, path + [key], filename)


def main():

    memo = defaultdict(list)  # ['x.y.z'] = "hoge.yml"

    for f in glob('**/*.yml', recursive=True):
        data = yaml.load(open(f))
        insert(data, memo, [], f)

    for key in memo:
        if len(memo[key]) > 1:
            print(f"Error: `{key}` appeared in: {', '.join(memo[key])}")


if __name__ == '__main__':
    main()
