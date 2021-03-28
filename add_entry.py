#! /usr/local/bin/python3

import os
import logging
import argparse
import subprocess
import arxiv

logging.basicConfig(format='%(message)s', level=logging.INFO)
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
        self.summary_fpath = os.path.join(self.directory_path, 'summary.md')
        self.set_refs()

    def set_refs(self):
        article_id = self.url.split('/')[-1][:-4]
        results = arxiv.query(query="",
                              id_list=[article_id],
                              max_results=1,
                              start=0,
                              sort_by="relevance",
                              sort_order="descending",
                              prune=True,
                              iterative=False,
                              max_chunk_results=1)[0]
        self.title = results.title
        self.abstract = results.summary
        self.authors = ', '.join(results.authors)
        self.year = results.updated_parsed.tm_year

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
                logging.info(f'New {k} --> {self.truncate_path(v)}')

    @staticmethod
    def truncate_path(path):
        return '/'.join(path.split('/')[5:])

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
                    '\n---\n[BACK](../index.md)\n\n[HOME]( ../../index.md)'
                ]
                idx = -4

        summary_relpath = f'{self.directory}/summary.md'
        index_relpath = f'{self.subcategory}/index.md'
        if k == 'subcategory':
            content.insert(idx, f'\n[{self.subcategory}]({index_relpath})\n')
        elif k == 'directory':
            content.insert(
                idx, f'\n[{self.title} ({self.year})]({summary_relpath})\n')
        content = "".join(content)

        with open(index_path, "w") as f:
            f.write(content)

        logging.info(f'Index {self.truncate_path(index_path)} updated')

    def update_summary(self):
        # Add content to summary file
        if not os.path.exists(self.summary_fpath):
            with open(self.summary_fpath, 'w') as f:
                f.write(
                    f'[{self.title}]({self.url})\n{self.year} - {self.authors}\n\n---\n\n👁️\n\n**Problem:**\n\n\n**Solution:**\n\n\n**Architecture:**\n\n\n**Results:**\n\n\n**Notes:**\n\n\n---\n\n[BACK](../index.md)\n\n[HOME](../../../index.md)'
                )
            logging.info(
                f'Summary {self.truncate_path(self.summary_fpath)} created')
        else:
            logging.warning(
                f' !!! Summary file {self.truncate_path(self.summary_fpath)} already exists: not overwriting !!!'
            )


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', dest='open', action='store_true')
    for p in ["category", "subcategory", "directory", "url"]:
        parser.add_argument(p, type=str, default=None, help=p)
    args = parser.parse_args()
    em = EntryManager(args)
    if args.open:
        subprocess.call(['code', em.summary_fpath])
