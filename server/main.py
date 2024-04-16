from models import apk, Blog, db
from flask import redirect, render_template, request, url_for

@apk.route("/home")
def all():
    post = db.session.execute(db.select(Blog).order_by(Blog.title)).scalars()
    return render_template("index.html", post=post)

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