# gopage
	
## description
A tool to download and parse web page from search engines like Google, Baidu, Sogou and so on.

	
## Main Classes

### PageSearcher
* Description
	* Given a list of query keywords, download corresponding web pages from search engines.
* PageSearcher(output\_dir, keyword\_list, search\_helper)
	* output_dir: where your downloaded pages will be stored. PageSearcher will create the folder if needed.
	* keyword\_list: a list of keywords, one for each query.
	* search_helper: depends on which search engine you wanna use(GoogleHelper, BaiduHelper, SogouHelper, etc).
* Example:

		from page_searcher.page_searcher import PageSearcher
		from search_helper.search_helper import GoogleHelper
		keyword_list = ['Tsinghua', 'PKU', 'hello world']
		searcher = PageSearcher('output_dir', keyword_list, GoogleHelper())
		searcher.get_page()
	
###GoogleItemParser
* Description
	* Given the content of a web page from Google, parse the page to the form of a list of items(snippets).
	* Each item is a dict with 'title', 'content', 'cite_url' etc.
* Example
	
		with open('test.html') as f:
			content = f.read()
			parser = GoogleItemParser()
			parser.feed(content)
			item_list = parser.get_items()
		