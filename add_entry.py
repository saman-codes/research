#! /usr/bin/python3

import os
import argparse
'''
Examples:
    Category: CV, RL 
    Subcategory: architectures, latent_spaces, medical
    Directory: pathak_et_al_2017, schmidhuber_1991
'''


class EntryManager:
    def __init__(self, args):
        self.args = args
        self.set_args()
        self.create_dirs()
        self.update_summary()

    def set_args(self):
        self.cwd = os.path.dirname(os.path.realpath(__file__))

        self.category = self.args.category
        self.category_path = os.path.join(self.cwd, self.category)

        self.subcategory = self.args.subcategory
        self.subcategory_path = os.path.join(self.category_path,
                                             self.subcategory)

        self.directory = self.args.directory
        self.directory_path = os.path.join(self.subcategory_path,
                                           self.directory)
        self.url = self.args.url
        self.harvard = self.args.harvard
        self.summary_fpath = os.path.join(self.directory_path, 'summary.md')

    def create_dirs(self):
        # Create directories that don't exist
        for k, v in {
                'category': self.category_path,
                'subcategory': self.subcategory_path,
                'directory': self.directory_path,
        }.items():
            if not os.path.exists(v):
                os.mkdir(v)
                # Only update indeces when a new dir is created
                self.update_index(k)

    def update_index(self, k):
        parent_path = getattr(self, f'{k}_path')
        index_path = os.path.split(parent_path)[0]
        index_path = os.path.join(index_path, 'index.md')
        if os.path.exists(index_path):
            with open(index_path, 'r') as f:
                content = list(f)
                if k == 'subcategory':
                    idx = -4
                elif k == 'directory':
                    idx = 0
        else:
            if k == 'subcategory':
                content = [
                    '<center>\n<h2>\n[object-based](object_based/index.md)\n</center>\n[HOME]( ../../index.md)'
                ]
                idx = -2
            elif k == 'directory':
                content = [
                    '\n---\n[BACK](../index.md)\n[HOME]( ../../index.md)'
                ]
                idx = -4

        for i, c in enumerate(self.harvard.split('.')):
            if '19' in c or '20' in c:
                c = c.strip(' ').strip(',')
                auth_and_name = ' '.join(self.harvard.split('.')[:i + 1])
                # stop loop to avoid a match after the date, which would overwrite auth_and_name
                break

        summary_relpath = f'{self.directory}/summary.md'
        index_relpath = f'{self.subcategory}/index.md'
        if k == 'subcategory':
            content.insert(idx, f'[{self.subcategory}]({index_relpath})\n')
        elif k == 'directory':
            content.insert(idx, f'[{auth_and_name}]({summary_relpath})\n')
        content = "".join(content)

        with open(index_path, "w") as f:
            f.write(content)

    def update_summary(self):
        # Add content to summary file
        with open(self.summary_fpath, 'w') as f:
            f.write(
                f'[{str(self.harvard)}]({self.url})\n\n---\n\n**Problem:**\n\n**Solution:**\n\n**Results:**\n\n**Architecture:**\n\n---\n\n[BACK](../index.md)\n[HOME](../../../index.md)'
            )


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    for p in ["category", "subcategory", "directory", "url", "harvard"]:
        parser.add_argument(p, type=str, default=None, help=p)
    args = parser.parse_args()
    em = EntryManager(args)