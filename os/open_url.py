import webbrowser
# import json
# with open('my.json') as f:
    # data = json.load(f)
    # path = data['chrome']+' %s'
    # url = 'http://127.0.0.1:8000/admin/home'
chrome_path ="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"+" %s"
url ='https://www.youtube.com'
webbrowser.get(chrome_path).open(url)
