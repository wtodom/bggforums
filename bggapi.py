import requests
from bs4 import BeautifulSoup

BASE_URL = "http://www.boardgamegeek.com/xmlapi2/"

def get_forums(game_id):
	url = BASE_URL + "forumlist?type=thing&id={0}".format(game_id)
	r = requests.get(url)
	xml = r.text
	soup = BeautifulSoup(xml)
	forums_xml = soup.select("forum")
	forums = []
	for item in forums_xml:
		forum = {
			"name": item["title"],
			"id": item["id"]
		}
		forums.append(forum)
	return forums

def get_threads(forum_id):
	url = BASE_URL + "forum?id={0}".format(forum_id)
	r = requests.get(url)
	xml = r.text
	soup = BeautifulSoup(xml)
	threads_xml = soup.select("thread")
	threads = []
	for item in threads_xml:
		thread = {
			"author": item["author"],
			"title": item["subject"],
			"posted_on": item["postdate"],
			"last_activity": item["lastpostdate"],
			"id": item["id"]
		}
		threads.append(thread)
	return threads

def get_posts(thread_id):
	url = BASE_URL + "thread?id={0}".format(thread_id)
	r = requests.get(url)
	xml = r.text
	soup = BeautifulSoup(xml)
	all_posts = soup.select("article")
	posts = []
	for item in all_posts:
		post = {
			"username": item["username"],
			"title": item.subject.text,
			"body": item.body.text,
			"post_date": item["postdate"],
			"edit_date": item["editdate"],
			"num_edits": item["numedits"],
			"link": item["link"],
			"id": item["id"]
		}
		posts.append(post)
	return posts
