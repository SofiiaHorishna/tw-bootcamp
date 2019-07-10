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


def task3():

    r = requests.get(url + "/bank" + token)
    bankList = json.loads(r.text)

    r = requests.get(url + "/bankAccount" + token)
    bankAccountList = json.loads(r.text)

    r = requests.get(url + "/payment" + token)
    paymentList = json.loads(r.text)

    i = 0
    while i < paymentList.__len__():

        j = 0
        while j < bankList.__len__():
            if paymentList[i]["recipientBankId"] == bankList[j]["id"]:
                bankName = bankList[j]["name"]
                break
            j += 1

        j = 0
        while j < bankAccountList.__len__():
            if (bankAccountList[j]["accountName"] == "TransferWise Ltd"and
                bankAccountList[j]["bankId"] == paymentList[i]["recipientBankId"] and
                bankAccountList[j]["currency"] == paymentList[i]["targetCurrency"]):
                sourceAccountNumber = bankAccountList[j]["accountNumber"]
                break
            j += 1

        r = requests.post(url + "/bank/" + bankName + "/transfer/" + sourceAccountNumber + "/" + bankName + "/" +
                          paymentList[i]["iban"] + "/" + str(paymentList[i]["amount"]) + token)
        print(r.text)

        i += 1


taskStart(3)
task3()
taskFinish()
