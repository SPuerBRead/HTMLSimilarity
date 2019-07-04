# -*- coding: utf-8 -*-

"""
@author: taoqi
@file: HTMLSimilarity.py
@time: 2019-07-02 16:57
"""

from htmlparser import HTMLParser
from domtree2data import Converter
from calc import calculated_similarity


def get_html_similarity(html_doc1, html_doc2, dimension=5000):
    hp1 = HTMLParser(html_doc1)
    html_doc1_dom_tree = hp1.get_dom_structure_tree()
    hp2 = HTMLParser(html_doc2)
    html_doc2_dom_tree = hp2.get_dom_structure_tree()
    converter = Converter(html_doc1_dom_tree, dimension)
    dom1_eigenvector = converter.get_eigenvector()
    converter = Converter(html_doc2_dom_tree, dimension)
    dom2_eigenvector = converter.get_eigenvector()
    value = calculated_similarity(dom1_eigenvector, dom2_eigenvector, dimension)
    if value > 0.2:
        return False, value
    else:
        return True, value
