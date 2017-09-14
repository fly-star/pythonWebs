# coding=utf-8
import urllib.parse

from werkzeug.routing import BaseConverter


class ListConverter(BaseConverter):

    def __init__(self, url_map, separator='+'):
        super(ListConverter, self).__init__(url_map)
        self.separator = urllib.parse.unquote(separator) #解码

    def to_python(self, value):
        return value.split(self.separator)

    def to_url(self, values):
        return self.separator.join(BaseConverter.to_url(value) for value in values)