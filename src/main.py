import os
from os.path import isdir
import shutil
from argparse import ArgumentError
from markdown_blocks import generate_page
from markdown_blocks import generate_pages_recursive


def rcopy(f, t):
    if not os.path.exists(f):
        raise Exception(f"Path [{f}] does not exist")
    if os.path.exists(t):
        shutil.rmtree(t)
    if not os.path.exists(t):
        os.mkdir(t)

    for path in os.listdir(f):
        full_f = f"{f}{os.sep}{path}"
        full_t = f"{t}{os.sep}{path}"
        if os.path.isdir(full_f) and not os.path.exists(full_t):
            rcopy(full_f, full_t)
        else:
            shutil.copy(full_f, full_t)


def main():
    rcopy("static", "public")
    generate_pages_recursive("content", "template.html", "public")


main()
