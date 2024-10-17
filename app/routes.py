from flask import render_template, request
from app import app

posts = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        age = request.form.get('age')
        if name and city and hobby and age:
            posts.append({'name': name, 'city': city, 'hobby': hobby, 'age': age})

    return render_template('blog.html', posts=posts)
