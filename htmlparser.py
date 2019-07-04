# -*- coding: utf-8 -*-

"""
@author: taoqi
@file: htmlparser.py
@time: 2019-07-02 17:17
"""

from treelib import Tree
from bs4 import BeautifulSoup
import bs4


class DOMTree:
    def __init__(self, label, attrs):
        self.label = label
        self.attrs = attrs


class HTMLParser:

    def __init__(self, html):
        self.dom_id = 1
        self.dom_tree = Tree()
        self.bs_html = BeautifulSoup(html, 'lxml')

    def get_dom_structure_tree(self):
        for content in self.bs_html.contents:
            if isinstance(content, bs4.element.Tag):
                self.bs_html = content
        self.recursive_descendants(self.bs_html, 1)
        return self.dom_tree

    def recursive_descendants(self, descendants, parent_id):
        if self.dom_id == 1:
            self.dom_tree.create_node(descendants.name, self.dom_id, data=DOMTree(descendants.name, descendants.attrs))
            self.dom_id = self.dom_id + 1
        for child in descendants.contents:
            if isinstance(child, bs4.element.Tag):
                self.dom_tree.create_node(child.name, self.dom_id, parent_id, data=DOMTree(child.name, child.attrs))
                self.dom_id = self.dom_id + 1
                self.recursive_descendants(child, self.dom_id - 1)
