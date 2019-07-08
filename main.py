import os
from bottle import (get, post, redirect, request, route, run, static_file,
                    template)
import utils
import json

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
    ##data=[]
    ##for show in utils.AVAILABLE_SHOWS:
       ## data.append(show)
    ##data=json.load(data)

    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData = {})
@route('/search')
def search():
    sectionTemplate = "./templates/search.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData = {})
result={
    "name":"hey"
}
""""
#creates route for each of the tv shows
for show in utils.AVAILABLE_SHOWS:
    @route('/show/<param>'.format(show))
    def shows():
        sectionTemplate = "./templates/show.tpl" #should be show, but does not work at the moment
        print(utils.getJsonFromFile(show))
        print(show)
        data=utils.getJsonFromFile(show)
        data=json.loads(data)
        return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData = data)
"""
@route('/show/<show>')
def shows(show):
    sectionTemplate = "./templates/show.tpl" #should be show, but does not work at the moment
    print(utils.getJsonFromFile(show))
    print(show)
    data=utils.getJsonFromFile(show)
    data=json.loads(data)
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData = data)




run(host='localhost', port=os.environ.get('PORT', 5000))
