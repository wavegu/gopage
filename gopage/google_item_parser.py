# encoding: utf-8


import re
import os
import json
from HTMLParser import HTMLParser

import sys

reload(sys)
sys.setdefaultencoding('utf8')


class GoogleItem:

    def __init__(self):
        self.title = ''
        self.content = ''
        self.cite_url = ''
        self.cite_name = ''
        self.email_list = []

    def to_dict(self):
        return {
            'title': self.title,
            'content': self.content,
            'cite_url': self.cite_url,
            'cite_name': self.cite_name,
        }


class GoogleItemParser(HTMLParser):
    """
    parse items(snippets) from a single web page from Google
    """

    def __init__(self):
        HTMLParser.__init__(self)
        self.tem_googleItem = GoogleItem()
        self.is_in_title = False
        self.is_in_content = False
        self.is_in_cite_url = False
        self.is_in_cite_name = False
        self.google_item_list = []
        self.content_span_num = 0

    def handle_starttag(self, tag, attrs):
        if tag == 'span':
            for (variable, value) in attrs:
                if variable == "class" and value == "st":
                    self.is_in_content = True
                    break
            if self.is_in_content:
                self.content_span_num += 1

        elif tag == 'div':
            for (variable, value) in attrs:
                if variable == "class" and value == "rc":
                    self.is_in_title = True
                    self.tem_googleItem = GoogleItem()
                    break
                if variable == 'class' and value == 'crl':
                    self.is_in_cite_name = True
                    break

        elif tag == 'cite':
            for (variable, value) in attrs:
                if variable == 'class' and value == '_Rm':
                    self.is_in_cite_url = True
                    break

    def handle_endtag(self, tag):
        if self.is_in_title and tag == 'a':
            self.is_in_title = False
            return

        if self.is_in_cite_url and tag == 'cite':
            self.is_in_cite_url = False
            return

        if self.is_in_cite_name and tag == 'div':
            self.is_in_cite_name = False
            return

        if self.is_in_content and tag == 'span':
            self.content_span_num -= 1
            if self.content_span_num > 0:
                return
            self.is_in_content = False
            if self.tem_googleItem.content == '':
                return
            try:
                self.tem_googleItem.content = str(self.tem_googleItem.content).lower()
            except Exception as e:
                print e
                print self.tem_googleItem.content
                return []

            self.google_item_list.append(self.tem_googleItem)


    def handle_data(self, data):
        if self.is_in_title:
            self.tem_googleItem.title += data
        if self.is_in_cite_url:
            self.tem_googleItem.cite_url += data
        if self.is_in_cite_name:
            self.tem_googleItem.cite_name += data
        if self.is_in_content:
            self.tem_googleItem.content += data

    def get_items(self):
        google_item_dict_list = [google_item.to_dict() for google_item in self.google_item_list]
        self.google_item_list = []
        return google_item_dict_list


# if __name__ == '__main__':
    # parser = GoogleSearchPageMailParser()
    # parser.handle_data(data)
    # print parser.emails
    # parse_mails_from_search_page('google')