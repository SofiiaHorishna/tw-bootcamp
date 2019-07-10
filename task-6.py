import requests
import json
import re

url = "http://54.229.242.6"
token = "/?token=06530a7ae985ed3592b519f99ae86e2e"


def taskFinish():
    r = requests.post(url + "/task/finish" + token)
    print(r.text)


def taskStart(taskId):
    r = requests.post(url + "/task/" + str(taskId) + "/start" + token)
    print(r.text)


def task6():

    r = requests.get(url + "/payment" + token)
    print(r.text)
    payment = json.loads(r.text)

    r = requests.get(url + "/payment/history" + token)
    print(r.text)
    paymentHistory = json.loads(r.text)

    listPaymentHistoryFraud = []
    i = 0
    while i < paymentHistory.__len__():
        if paymentHistory[i]["fraud"]:
            listPaymentHistoryFraud.append(paymentHistory[i])
        i += 1

    idListPut = set()
    idListDelete = set()

    i = 0

    splitter = "."
    listIp = listPaymentHistoryFraud[i]["ip"].split(splitter)
    listIp.pop()
    templateIp = splitter.join(listIp)

    while i < payment.__len__():
        idListDelete.add(payment[i]["id"])
        result = re.match(templateIp, payment[i]["ip"])
        if result:
            idListPut.add(payment[i]["id"])
        i += 1

    idListDelete = idListDelete - idListPut

    for elem in idListPut:
        r = requests.put(
            url + "/payment/" + elem + "/fraud" + token)
        print(r.text)

    for elem in idListDelete:
        r = requests.delete(
            url + "/payment/" + elem + "/fraud" + token)
        print(r.text)


taskStart(6)
task6()
taskFinish()
