#!/usr/bin/env python
import sys
"""
Python class example.

"""


class Element(object):
    tag = "html"
    indent = 0

    def __init__(self, content=None):
        self.content = []

        if content is not None:
            self.content.append(content)

    def append(self, string):
        ''' Adds another string to the existing content '''
        self.content.append(string)

    def render(self, file_out, ind=""):
        file_out.write("<%s>\n" % (self.tag))
        for item in self.content:
            file_out.write(item)
            file_out.write("\n")
        file_out.write("</%s>\n" % (self.tag))

an_elem = Element()
print an_elem.content
an_elem.append("Bae")
an_elem.append("Sexy")
print an_elem.content
print an_elem.render(sys.stdout)



