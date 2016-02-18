from flask import Flask, render_template
import os
import glob

app = Flask(__name__)

@app.route('/')
def index():
    posts_list = list_posts('posts')
    blog = create_blog_list(posts_list)
    return render_template('index.html', blog=blog)

def create_blog_list(posts):
    x = []
    for post in posts:
        fp = open(post, "r")
        content = fp.read()
        fp.close()
        x.append(content)
    return x

def list_posts(directory):
    files = filter(os.path.isfile, glob.glob(directory + "/*.txt"))
    return files

if __name__ == '__main__':
    app.run(debug=True)
