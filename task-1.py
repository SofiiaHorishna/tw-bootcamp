import requests

url = "http://54.229.242.6"
token = "/?token=06530a7ae985ed3592b519f99ae86e2e"


def taskFinish():
    r = requests.post(url + "/task/finish" + token)
    print(r.text)


def taskStart(taskId):
    r = requests.post(url + "/task/" + str(taskId) + "/start" + token)
    print(r.text)


def task1():
    name = "Sofiia"
    r = requests.post(url + "/name/" + name + token)
    print(r.text)


taskStart(1)
task1()
taskFinish()
