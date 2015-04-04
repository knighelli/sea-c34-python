#!/usr/bin/env python
import sys
"""
Python class example.

"""


class Element(object):
    tag = "html"
    indent = "  "

    def __init__(self, content=None):
        self.content = []

        if content is not None:
            self.content.append(content)

    def append(self, string):
        ''' Adds another string to the existing content '''
        self.content.append(string)

    def render(self, file_out, ind=""):
        file_out.write(ind)
        file_out.write("<%s>\n" % (self.tag))
        for item in self.content:
            if isinstance(item, Element):
                item.render(file_out, ind+self.indent)
            else:
                file_out.write(ind+self.indent)
                file_out.write(item)
                file_out.write("\n")
        file_out.write(ind)
        file_out.write("</%s>\n" % (self.tag))

class Html(Element):
    tag = "html"

class Body(Element):
    tag = "body"

class P(Element):
    tag = "p"

elem = Html()
'''
elem.append("Hello")
elem.append("world")
body_tag = Body("Dat booty")
p_tag = P("Pee")
body_tag.append(p_tag)
elem.append(body_tag)
elem.render(sys.stdout)
'''


