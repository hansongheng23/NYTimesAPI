import csv
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def write_csv(data, filename):  #this function is used to transfer .json file in .csv file.
	with open(filename, 'w') as outf:
		result = True
		for item in data:
			writter = csv.DictWriter(outf, item.keys(),extrasaction='ignore')
			#item = unicode(item).replace("\r", " ").replace("\n", " ").replace("\t", "").replace("\"", "")
			if result == True:
				writter.writeheader() #write headers of .csv file
				result = False
			else:
				writter.writerow(item) #write rows of .csv file



data = json.loads(open('results.json').read()) #read data from .json file
data = data['response']['docs']   #this is used to specify that we are converting contents under 'docs' into .csv file
write_csv(data,'results.csv')  #write data into .csv file
