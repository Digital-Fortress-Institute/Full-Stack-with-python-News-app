from models import apk, Blog, db
from flask import redirect, render_template, request, url_for

@apk.route("/home")
def all():
    posts = db.session.execute(db.select(Blog).order_by(Blog.title)).scalars()
    return render_template("index.html", posts=posts)

@apk.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        blog = Blog(
            title=request.form["title"],
            body=request.form["body"],
            image=request.form["image"]  
        )
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for("all"))
    return render_template('upload.html')

@apk.route("/blog/<int:id>")
def user_detail(id):
    post = Blog.query.get_or_404(id)
    return render_template("detail.html", post=post)