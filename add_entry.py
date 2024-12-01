# Standard Library
import argparse
import os
import subprocess
from dataclasses import dataclass
from datetime import datetime
from io import StringIO
import xml.etree.ElementTree as ET
import urllib.request as libreq

"""
Examples:
    Category: CV, RL 
    Subcategory: architectures, latent_spaces, medical
    Directory: lang1988spiral, schmidhuber1991everything, pathak_et_al_2017
"""


@dataclass
class Paper:
    title: str
    authors: list[str]
    published: datetime.date
    abstract: str


class EntryManager:

    def __init__(self, args):
        self.category = args.category
        self.subcategory = args.subcategory
        self.url = args.url
        self.set_paper()
        self.set_directory()
        self.set_paths()
        self.create_dirs()
        self.create_and_update_subcategory_index_file()
        self.create_and_update_directory_index_file()
        self.create_summary_file_if_not_exists()

    @staticmethod
    def get_parsed_dict(url):
        article_id = url.split("/")[-1]
        url = f"http://export.arxiv.org/api/query?id_list={article_id}&start=0&max_results=1"
        parsed_dict = dict()
        with libreq.urlopen(url) as req:
            response = req.read().decode("utf-8")
            it = ET.iterparse(StringIO(response))
            for _, el in it:
                _, _, el.tag = el.tag.rpartition("}")
            root = it.root
        parsed_dict["title"] = root.find(".//entry/title").text
        parsed_dict["abstract"] = root.find(".//summary").text
        parsed_dict["published"] = datetime.date(
            datetime.strptime(root.find(".//published").text, "%Y-%m-%dT%H:%M:%SZ")
        )
        parsed_dict["authors"] = [
            el.find("name").text for el in root.findall(".//author")
        ]
        return parsed_dict

    @staticmethod
    def truncate_path(path):
        return "/".join(path.split("/")[5:])

    def set_paths(self):
        self.cwd = os.path.dirname(os.path.realpath(__file__))
        self.category_path = os.path.join(self.cwd, self.category)
        self.subcategory_path = os.path.join(self.category_path, self.subcategory)
        self.directory_path = os.path.join(self.subcategory_path, self.directory)
        self.summary_fpath = os.path.join(self.directory_path, "summary.md")

    def set_paper(self):
        self.paper = Paper(**self.get_parsed_dict(self.url))

    def set_directory(self):
        first_author_surname = self.paper.authors[0].split(" ")[-1].lower()
        year = self.paper.published.year
        self.directory = f"{first_author_surname}{year}"
        self.paper_details_string = f"\n[{self.paper.title} ({self.paper.published.year})]({f"{self.directory}/summary.md"})\n"

    def create_dirs(self):
        for k in ["category", "subcategory", "directory"]:
            path = getattr(self, f"{k}_path")
            os.makedirs(path, exist_ok=True)

    @staticmethod
    def _join_and_write_content(content, path):
        content = "".join(content)
        with open(path, "w") as f:
            f.write(content)

    def create_and_update_subcategory_index_file(self):
        index_file_path = os.path.join(
            os.path.split(self.subcategory_path)[0], "index.md"
        )
        if not os.path.exists(index_file_path):
            self.create_subcategory_index_file(index_file_path)
        self.update_subcategory_index_file(index_file_path)

    def create_subcategory_index_file(self, index_file_path):
        content = ["\n---\n[HOME]( ../../index.md)"]
        self._join_and_write_content(content, index_file_path)

    def update_subcategory_index_file(self, index_file_path):
        index_relative_path = f"{self.subcategory}/index.md"
        with open(index_file_path, "r") as f:
            content = list(f)
        content.insert(-4, f"\n[{self.subcategory}]({index_relative_path})\n")
        self._join_and_write_content(content, index_file_path)

    def create_directory_index_file(self, index_file_path):
        content = ["\n---\n[BACK](../index.md)\n\n[HOME]( ../../index.md)"]
        self._join_and_write_content(content, index_file_path)

    def update_directory_index_file(self, index_file_path):
        with open(index_file_path, "r") as f:
            content = list(f)
        content.insert(0, self.paper_details_string)
        self._join_and_write_content(content, index_file_path)

    def create_and_update_directory_index_file(self):
        index_file_path = os.path.join(
            os.path.split(self.directory_path)[0], "index.md"
        )
        if not os.path.exists(index_file_path):
            self.create_directory_index_file(index_file_path)
        self.update_directory_index_file(index_file_path)

    def create_summary_file_if_not_exists(self):
        if not os.path.exists(self.summary_fpath):
            with open(self.summary_fpath, "w") as f:
                f.write(
                    "\n\n".join(
                        [
                            f"[{self.paper.title}]({self.url})\n{self.paper.published.year} - {", ".join(self.paper.authors)}\n\n---",
                            "👁️",
                            "**Abstract**",
                            self.paper.abstract,
                            "**Problem:**\n\n\n**Solution:**\n\n\n**Architecture:**\n\n\n**Results:**\n\n\n**Notes:**\n\n\n---",
                            "[BACK](../index.md)",
                            "[HOME](../../../index.md)",
                        ]
                    )
                )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", dest="open", action="store_true")
    for p in ["category", "subcategory", "url"]:
        parser.add_argument(p, type=str, default=None, help=p)
    args = parser.parse_args()
    em = EntryManager(args)
    if args.open:
        subprocess.call(["nvim", em.summary_fpath])
