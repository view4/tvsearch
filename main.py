import os
from bottle import (get, post, redirect, request, route, run, static_file,
                    template)
import utils

# Static Routes

@get("/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="./js")

@get("/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="./css")

@get("/images/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="./images")

@route('/')
def index():
    sectionTemplate = "./templates/home.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData = {})

@route('/browse')
def browse():
    sectionTemplate = "./templates/browse.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData = {})
@route('/search')
def search():
    sectionTemplate = "./templates/search.tpl"
    print("called")
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData = {})

for show in utils.AVAILABE_SHOWS:
    print(('/show/{0}'.format(show)))
    @route('/show/{0}'.format(show))
    def shows():
        sectionTemplate = "./templates/show.tpl"
        return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData = {})




run(host='localhost', port=os.environ.get('PORT', 5000))
