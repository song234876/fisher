import os

from flask import request, jsonify, flash, render_template

from app.forms.book import ClassForm
from app.web import web

# base_dir = os.path.abspath(os.path.dirname(__file__))
base_dir = 'D:\\AndroidProject\\PythonProject\\Fisher\\app\\static\\photo\\'


@web.route('/search', methods=['GET', 'POST'])
def search():
    args = request.args
    form = ClassForm(args)
    if form.validate():
        name = form.name.data.strip()
        age = form.age.data
        resp = {"name": name, "age": age}
        # return jsonify(resp)
        return render_template('book.html', user=resp)
    else:
        flash('搜索的关键字不符合要求，请重新输入关键字')
    return "hello world"

@web.route('/hello')
def hello():
    return "hello world"


@web.route('/upload', methods=['POST'])
def uploadPic():
    file = request.files.get('file')
    path = base_dir + file.filename
    file.save(path)
    return '上传成功：'+path
