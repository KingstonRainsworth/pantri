import requests
from bs4 import BeautifulSoup
import time
import re
import sys

def recipe_spider(recipe_url):
	source_coder = requests.get(recipe_url)
	recipe_text = source_coder.text
	soup = BeautifulSoup(recipe_text)
	for meal in soup.findAll('h1',{'class': 'entry-title'}):
		print("DISH: ")
		print(meal.string)
	for ingredients in soup.findAll('li',{'class': 'ingredient'}):
		print(ingredients.string)
	for instruction in soup.findAll('li',{'class': 'instruction'}):
		print(instruction.string)
def link_spider():
	url = 'http://www.everydaymaven.com/recipe-index-text-based/'
	source_code = requests.get(url)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text)
	for link in soup.findAll(href = re.compile("http://www\.everydaymaven\.com/\d")):
		traversable = link.get('href')
		print(traversable)
		recipe_spider(traversable)
		# Adding time.sleep for five seconds so that we don't get denied
		# access, also for demoing the project
		time.sleep(5)
link_spider()

#def link_spider():
#	url = 'http://www.everydaymaven.com/recipe-index-text-based/'
#	source_code = requests.get(url)
#	plain_text = source_code.text
#	soup = BeautifulSoup(plain_text)
#	for link in soup.findAll('a'):
#		href = link.get('href')
#		print(href)
