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
    data=[]
    for show in utils.AVAILABLE_SHOWS:## loop to collect all the data and store in the 'data' array.
        showInfo=utils.getJsonFromFile(show)
        data.append(json.loads(showInfo))
    print(data)
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData = data)##data passed to the template page here

@route('/search')
def search():
    sectionTemplate = "./templates/search.tpl"
#   query="";
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData = {})


"""query="star"
data=[]
for show in utils.AVAILABLE_SHOWS:## loop to collect all the data and store in the 'data' array.

        showInfo=utils.getJsonFromFile(show)
        showInfo=json.loads(showInfo)
        episodes=showInfo["_embedded"]["episodes"]
        for episode in episodes:##looping through each of the episodes in each series
            name =episode["name"]
            summary=episode["summary"]
            print(name)
            print(summary)
            if name is not None and summary is not None:
                if query in name or query in summary:
                    ##return the episode if it contains the search parameter
                    data.append(episode)

        print(data)"""
@route('/search', method='POST')
def default():
    query =request.forms.get('q')
    print(query)
    data=[]
    for show in utils.AVAILABLE_SHOWS:## loop to collect all the data and store in the 'data' array.

        showInfo=utils.getJsonFromFile(show)
        showInfo=json.loads(showInfo)
        episodes=showInfo["_embedded"]["episodes"]
        for episode in episodes:##looping through each of the episodes in each series
                name =episode["name"]
                summary=episode["summary"]
                print(name)
                print(summary)
                if name is not None and summary is not None:
                    if query in name or query in summary:
                        ##return the episode if it contains the search parameter

                        object={
                            "showid":show,
                            "episodeid":episode["id"],
                            "text":name,

                        }
                        data.append(object)
    print(data)
    sectionTemplate = "./templates/search_result.tpl"

    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData = data, query=query, results=data)##data passed to the template page here



@route('/show/<show>')
def shows(show):
    sectionTemplate = "./templates/show.tpl" #should be show, but does not work at the moment
    data=utils.getJsonFromFile(show)
    data=json.loads(data)
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData = data)




run(host='localhost', port=os.environ.get('PORT', 5000))
