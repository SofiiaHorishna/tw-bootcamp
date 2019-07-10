import requests

url = "http://54.229.242.6"
token = "/?token=06530a7ae985ed3592b519f99ae86e2e"


def taskFinish():
    r = requests.post(url + "/task/finish" + token)
    print(r.text)


def taskStart(taskId):
    r = requests.post(url + "/task/" + str(taskId) + "/start" + token)
    print(r.text)


def task2():
    chairs = []
    i = 0
    while i < 100:
        chairs.append(i + 1)
        i += 1

    k = 1
    while chairs.__len__() > 1:
        chairs.pop(0)
        k += 1
        i = 1
        while i < k:
            chairs.append(chairs[0])
            chairs.pop(0)
            i += 1

    r = requests.post(url + "/survivor/" + str(chairs[0]) + token)
    print(r.text)


taskStart(2)
task2()
taskFinish()
