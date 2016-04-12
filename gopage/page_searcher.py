# encoding: utf-8

import os
import random
import time
import json

from search_helper import BaiduHelper
from search_helper import HaosouHelper
from search_helper import SogouHelper

import sys
reload(sys)
sys.setdefaultencoding('utf8')


class PageSearcher:

    def __init__(self, result_dir, keyword_list, search_helper):
        self.keyword_list = keyword_list
        self.search_helper = search_helper
        self.result_path = result_dir
        # 建立搜索引擎文件夹
        if not os.path.exists(self.result_path):
            os.mkdir(self.result_path)

    def get_page_file_path(self, keyword):
        keyword = keyword.replace(' ', '_').replace('/', '.')
        if len(keyword) > 50:
            keyword = keyword[:50]
        path = unicode(os.path.join(self.result_path, keyword + '.html'))
        return path

    def get_page(self):

        for keyword in self.keyword_list:
            file_path = self.get_page_file_path(keyword)
            if os.path.exists(file_path):
                print '[EXIST]', keyword
                continue
            search_page_cache_file = open(self.get_page_file_path(keyword), 'w')
            try:
                search_page_content = self.search_helper.get_search_page_by_name(keyword)
                if search_page_content is None:
                    print '[Error]', self.search_helper, keyword
                    return False
                search_page_cache_file.write(search_page_content)
                search_page_cache_file.close()
                time.sleep(random.randint(1, 3))

            except Exception as e:
                print e
                if isinstance(e, KeyboardInterrupt):
                    exit()


if __name__ == '__main__':
    result_dir = 'result'
    if not os.path.exists(result_dir):
        os.mkdir(result_dir)
    search_helpers = [BaiduHelper(), SogouHelper(), HaosouHelper()]
    with open('keywords.txt') as f:
        keyword_list = [line.replace('\n', '') for line in f.readlines()]
        # keyword_list = [line.replace('\n', '').decode("gbk", "ignore").encode("utf-8") for line in f.readlines()]
    for search_helper in search_helpers:
        searcher = PageSearcher(result_dir, keyword_list, search_helper)
        searcher.get_page()
