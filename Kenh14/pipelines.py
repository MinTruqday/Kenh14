# Define your k14item pipelines here
#
# Don't forget to add your pipeline to the k14item_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/k14item-pipeline.html
import scrapy
import json
# useful for handling different k14item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import csv


class Kenh14DataJSONPipeline:
    def process_item(self, k14item, spider):
        with open('Kenh14DataJSON.json', 'a', encoding='utf-8') as file:
            line = json.dumps(dict(k14item), ensure_ascii=False) + '\n'
            file.write(line)
        return k14item

class Kenh14DataCSVPipeline:
    def process_item(self, k14item, spider):
        with open('Kenh14DataCSV.csv', 'a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter='$')
            writer.writerow([
                k14item['URL'],
                k14item['Title'],
                k14item['Consult'],
                k14item['AuthorName'],
                k14item['DateTime'],
                k14item['Intro'],
                k14item['Opening'],
                k14item['Body'],
                k14item['Ending'],
                k14item['Source']
            ])
        return k14item
    pass
