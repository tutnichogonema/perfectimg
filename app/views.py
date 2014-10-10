# coding=utf-8
import os
from werkzeug.utils import secure_filename, redirect
from app import app
from app.pagination import Pagination

__author__ = 'lxz'
from flask import render_template, request, url_for, send_from_directory


@app.route('/test_page')
@app.route('/test_page/<int:page>')
def test_page(page=1):
    # set up the pagination params, set count later
    p = Pagination(per_page=10, current_page=page)
    timeline = RedisTimeline.find_paginated(p)
    # pass the pagination object to the view, so a list of links can be displayed
    return render_template('index.html', timeline=timeline, pagination=p)

@app.route('/')
def index():
    FILES_DIR = app.config['UPLOAD_FOLDER']
    file_names_list = [x for x in os.listdir(FILES_DIR)]
    items = [{'image_href': '/uploads/' + image,
            'image_description': image} for image in file_names_list]
    return render_template("pinterest.html",
                           items=items)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('index'))
    else:
        return redirect(url_for('admin'))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)