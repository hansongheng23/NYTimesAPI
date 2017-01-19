import csv
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def write_csv(data, filename):
	with open(filename, 'w') as outf:
		result = True
		for item in data:
			writter = csv.DictWriter(outf, item.keys(),extrasaction='ignore')
			#item = unicode(item).replace("\r", " ").replace("\n", " ").replace("\t", "").replace("\"", "")
			if result == True:
				writter.writeheader()
				result = False
			else:
				writter.writerow(item)



data = json.loads(open('results.json').read())
data = data['response']['docs']
# print data
#print data['response_docs'][0]
#data = read_json('results.json')
#print data,type(data)
write_csv(data,'results.csv')
