import bggapi
from flask import Flask, request, session, g, redirect, url_for, \
	 abort, render_template, flash

# Config
DEBUG = True

# Create app
app = Flask(__name__)


def get_games():
	return [
		{
			"name": "Android: Netrunner",
			"id": "124742",
			"short_name": "ANR"
		},
		{
			"name": "Candyland",
			"id": "5048",
			"short_name": "CL"
		}
	]

def sidebar_data():
	game_list = get_games()
	for game in game_list:
		game_id = game["id"]
		forums = bggapi.get_forums(game_id)
		game["forum_list"] = forums
	return game_list

# Define routes
@app.route("/")
def index():
	return render_template("base.html", sidebar_links=sidebar_data())

@app.route("/forum/<forum_id>")
def view_forum(forum_id):
	threads = bggapi.get_threads(forum_id)
	return render_template("forum.html", forum=forum_id, sidebar_links=sidebar_data(), threads=threads)

@app.route("/forum/<forum_id>/thread/<thread_id>")
def view_thread(forum_id, thread_id):
	posts = bggapi.get_posts(thread_id)
	return render_template("thread.html", forum=forum_id, thread=thread_id, sidebar_links=sidebar_data(), posts=posts)


# Run it.
if __name__ == "__main__":
	app.run()
