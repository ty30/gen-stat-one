# Gen Stat One
# Flat-file static generator from python
# Ty C on Dec 2021

import sys
from flask import Flask, render_template, redirect
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from flask_minify import Minify

FLATPAGES_EXTENSION='.md'
FREEZER_DESTINATION_IGNORE=''

name = "URL"
app = Flask(__name__)
Minify(app=app, html=True, js=True, cssless=True)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)

# Index Page
@app.route('/')
def index():
	# Render the latest 3 blog posts
	latest=sorted(pages, reverse=True, key=lambda p: str(p.meta['date']))
	title='Home | '+name
	description='Index page'
	return render_template('index.html', pages=latest[:3], title=title, description=description)


# About Page
@app.route('/about/')
def about():
	title='About | '+name
	description='About page'
	return render_template('about.html', title=title, description=description)


# Terms Page
@app.route('/terms/')
def terms():
	title='Terms | '+name
	description='Terms and Conditions'
	return render_template('terms.html', title=title, description=description)


# Blog Post List
@app.route('/posts/')
def posts():
	latest=sorted(pages, reverse=True, key=lambda p: str(p.meta['date']))
	title='Posts | '+name
	return render_template('posts.html', pages=latest, title=title)


# Single Blog Post
@app.route('/<path:path>/')
def page(path):
	page=pages.get_or_404(path)
	return render_template('page.html', page=page, name=name)


# Tag List Page
@app.route('/tag/<string:tag>/')
def tag(tag):
	tagged = [p for p in pages if tag in p.meta.get('tags', [])]
	title='Tag: '+tag+' | '+name
	return render_template('tag.html', pages=tagged, tag=tag, title=title)


# 404 Error Page
@app.errorhandler(404)
def not_found(e):
	title='404 Error'
	return render_template("404.html", title=title)


if __name__=='__main__':
	if len(sys.argv) > 1 and sys.argv[1] == "build":
		freezer.freeze()
	else:
		app.run()
