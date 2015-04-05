#!/usr/bin/env python
import sys
"""
Python class example.

"""


class Element(object):
    tag = ""
    indent = "    "

    def __init__(self, content=None, **attrs):
        self.content = []
        self.attributes = attrs

        if content is not None:
            self.content.append(content)

    def append(self, string):
        ''' Adds another string to the existing content '''
        self.content.append(string)

    def render(self, file_out, ind=""):
        file_out.write(ind)
        file_out.write("<%s" % (self.tag))
        for key, value in self.attributes.items():
            file_out.write(' %s="%s"' % (key, value))
        file_out.write(">\n")
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


class Head(Element):
    tag = "head"


class OneLineTag(Element):

    def render(self, file_out, ind=""):
        file_out.write(ind)
        file_out.write("<%s" % (self.tag))
        for key, value in self.attributes.items():
            file_out.write(' %s="%s"' % (key, value))
        file_out.write(">")
        for item in self.content:
            file_out.write(item)
        file_out.write("</%s>\n" % (self.tag))


class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):

    def __init__(self, **attrs):
        self.attributes = attrs

    def render(self, file_out, ind=""):
        file_out.write(ind)
        file_out.write("<%s" % (self.tag))
        for key, value in self.attributes.items():
            file_out.write(' %s="%s"' % (key, value))
        file_out.write(" />\n")

class Hr(SelfClosingTag):
    tag = "hr"

class Br(SelfClosingTag):
    tag = "br"

class A(OneLineTag):
    tag = "a"
    def __init__(self, link, content):
        Element.__init__(self, content, href=link)
