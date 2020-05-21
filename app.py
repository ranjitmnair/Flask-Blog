from flask import *
app=Flask(__name__)

blog={
    'name': 'My awesome blog',
    'posts':{}
    }


@app.route('/')
def index():
    return render_template('home.html',blog=blog)

@app.route('/post/<int:post_id>')
def posts(post_id):
    post= blog['posts'].get(post_id)
    if not post:
        return '<h1>Post does not exist</h1>'
    return render_template('post.html',post=post)

@app.route('/post/create',methods=['GET','POST'])
def create():
    if request.method=='POST':
        title=request.form.get('title')
        content=request.form.get('content')
        post_id=len(blog['posts'])
        blog['posts'][post_id]={'post_id':post_id,'title':title,'content':content}
        return redirect(url_for('posts',post_id=post_id))
    return render_template('create.html')

app.run()