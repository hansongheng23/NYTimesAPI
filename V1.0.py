import csv
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def write_csv(data, filename):
	with open(filename, 'w') as outf:
		result = True
		for item in data:
			print type(item)
			writter = csv.DictWriter(outf, item.keys(),extrasaction='ignore')
			if result == True:
				writter.writeheader()
				result = False
			else:
				writter.writerow(item)

def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)

data = json.loads(open('results.json').read())
data = data['response']['docs']
i = 0
for items in data:
	while i < len(data):
		if type(items.keys()) == dict or list:
			#print data[i]
			items = flatten_json(items)
			#print data[i]
			i = i+1
		else:
			i=i+1

write_csv(data,'results.csv')
