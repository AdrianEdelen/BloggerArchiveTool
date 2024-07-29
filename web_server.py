from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

# Load blog posts from JSON file
def load_posts():
    with open('data/blog_posts.json', 'r', encoding='utf-8') as file:
        posts = json.load(file)
    return posts

# Home route to list all posts
@app.route('/')
def home():
    posts = load_posts()
    return render_template('index.html', posts=posts)

# Route to display a single post
@app.route('/post/<post_id>')
def post(post_id):
    posts = load_posts()
    post = next((p for p in posts if p['id'] == post_id), None)
    if post:
        return render_template('post.html', post=post)
    else:
        return "Post not found", 404

if __name__ == '__main__':
    app.run(debug=True)
