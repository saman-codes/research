import os
import argparse


def main():
    parser = argparse.ArgumentParser()
    for p in ["category", "subcategory", "name", "url", "harvard"]:
        parser.add_argument(p, type=str, default=None, help=p)

    args = parser.parse_args()
    cwd = os.path.dirname(os.path.realpath(__file__))
    category = os.path.join(cwd, args.category)
    subcategory = os.path.join(category, args.subcategory)
    directory = os.path.join(subcategory, args.name)
    for d in [category, subcategory, directory]:
        if not os.path.exists(d):
            os.mkdir(d)

    url = args.url
    harvard = args.harvard
    summary_fname = os.path.join(directory, 'summary.md')
    index_fname = os.path.join(subdirectory, 'index.md')

    with open(summary_fname, 'w') as f:
        f.write(
            '[' + str(harvard) + ']' + '(' + url +
            ')\n\n---\n\n**Problem:**\n\n**Solution:**\n\n**Results:**\n\n**Architecture:**\n\n---\n\n[BACK](../index.md)\n[HOME](../../../README.md)'
        )

    with open(subdirectory, 'a') as f:
        f.write('[' + str(harvard) + ']' + '(' + url + ')\n')


if __name__ == '__main__':
    main()