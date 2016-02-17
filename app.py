from flask import Flask, render_template, url_for, request, redirect
import os
import glob
import time
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    posts_list = sort_posts_by_date('posts')
    blog = create_blog_list(posts_list)
    return render_template('index.html', blog=blog)

@app.route('/submission')
def submit_blog_entry_page():
    return render_template('submission.html')

@app.route('/submitBlog', methods=['POST'])
def submit_blog_post():
    content = request.form['content']
    save_blog_post(content)
    return redirect('/')

def create_blog_list(posts):
    x = []
    for post in posts:
        fp = open(post, "r")
        content = fp.read()
        fp.close()
        x.append(content)
    return x

def save_blog_post(content):
    directory_check()
    filename = "posts/" + str(int(time.time())) + ".txt"
    post = open(filename, "wb")
    post.write(content)
    post.close()

def directory_check():
    if not os.path.exists("posts"):
        os.makedirs("posts")

def sort_posts_by_date(directory):
    files = filter(os.path.isfile, glob.glob(directory + "/*.txt"))
    files.sort(key=lambda x: os.path.getctime(x), reverse=True)
    return files

if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    app.run(debug=True)
