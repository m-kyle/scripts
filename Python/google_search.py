# google_search.py
# Search Google from the command-line

import urllib2
import urllib
import json
import re

search_query = raw_input("Search Query: ")

def showsome(searchfor):
	query = urllib.urlencode({'q': searchfor})
	url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
	search_response = urllib.urlopen(url)
	search_results = search_response.read()
	results = json.loads(search_results)
	data = results['responseData']
	print 'Total results: %s' % data['cursor']['estimatedResultCount']
	hits = data['results']
	print 'Top %d results:' % len(hits)
	print ""

	for h in hits:
		print h['titleNoFormatting']
  		print h['url']
  		print re.sub('(<b>|<\/b>)', '', h['content'])
  		print ""
	
	print 'For more results, see %s' % data['cursor']['moreResultsUrl']

showsome(search_query)