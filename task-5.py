import requests
import json

url = "http://54.229.242.6"
token = "/?token=06530a7ae985ed3592b519f99ae86e2e"


def taskFinish():
    r = requests.post(url + "/task/finish" + token)
    print(r.text)


def taskStart(taskId):
    r = requests.post(url + "/task/" + str(taskId) + "/start" + token)
    print(r.text)


def task5():

    r = requests.get(url + "/task/5" + token)
    pepsList = json.loads(r.text)["peps"]

    r = requests.get(url + "/payment" + token)
    paymentList = json.loads(r.text)

    peps = []
    i = 0
    while i < pepsList.__len__():
        peps.append(pepsList[i].split(" - "))
        i += 1

    idListPut = set()
    idListDelete = set()

    i = 0
    while i < paymentList.__len__():
        idListDelete.add(paymentList[i]["id"])
        j = 0
        while j < peps.__len__():
            if (paymentList[i]["recipientName"] == peps[j][0] and
                paymentList[i]["recipientCountry"] == peps[j][1]):
                idListPut.add(paymentList[i]["id"])
            j += 1
        i += 1

    idListDelete = idListDelete - idListPut

    for elem in idListPut:
        r = requests.put(
            url + "/payment/" + elem + "/aml" + token)
        print(r.text)

    for elem in idListDelete:
        r = requests.delete(
            url + "/payment/" + elem + "/aml" + token)
        print(r.text)


taskStart(5)
task5()
taskFinish()
