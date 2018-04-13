from collections import defaultdict
from glob import glob

import click
import yaml


def insert(data, memo, path, filename):
    if type(data) != dict:
        return
    for key in data:
        fullkey = '.'.join(path + [key])
        memo[fullkey].append(filename)
        insert(data[key], memo, path + [key], filename)


@click.command()
@click.argument('dir', default='.')
def main(dir):

    memo = defaultdict(list)  # ['x.y.z'] = "hoge.yml"

    for f in glob(f"{dir}/**/*.yml", recursive=True):
        data = yaml.load(open(f))
        insert(data, memo, [], f)

    for key in memo:
        if len(memo[key]) > 1:
            print(f"Error: `{key}` appeared in: {', '.join(memo[key])}")


if __name__ == '__main__':
    main()
