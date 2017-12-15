import json
import requests
import time
import re
tag = '벚꽃엔딩'
url = 'https://www.instagram.com/explore/tags/' + tag + '/?__a=1&max_id='


global request
request = requests.get(url)
global text
text = request.text
global allJson
allJson = json.loads(text)

numberOftag = allJson['tag']['media']['count'] # 벚꽃엔딩 태그된 개수
global numberOfposts
numberOfposts = 0

global tags
tags = []
global hasNext
hasNext = False
global end
end = ''



def filterr(st):
    st = st.replace('#', ' ')
    st = st.replace('\n', ' ')
    return st.split(' ')

def mku():
    global text
    global request
    global allJson
    request = requests.get(url + end)
    text = request.text
    allJson = json.loads(text)

def makeData(f = 1503145621, t = 1513350621):
    global hasNext
    global end
    global tags
    global allJson
    global text
    global url
    global request
    global numberOfposts
    target = allJson['tag']
    ttags = target['media']['nodes']
    for value in ttags:
        tdate = value['date']
        if tdate<= t and tdate >= f:
            numberOfposts = numberOfposts + 1
            if 'caption' in value:
                for stag in filterr(value['caption']):
                    if not stag == '':
                        tags.append(stag)
        else:
            print(tags)
            print(numberOfposts)
            print(len(tags))
            hasNext = False
            return
    hasNext = target['media']['page_info']['has_next_page']
    if hasNext == True:
        end = target['media']['page_info']['end_cursor']
        print(end)
        print(len(tags))
        mku()
        makeData()
    else:
        end = ''
        return

print(numberOftag)
makeData()
