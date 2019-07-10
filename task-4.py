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


def task4():

    r = requests.get(url + "/currency" + token)
    print(r.text)
    currencyList = json.loads(r.text)

    r = requests.get(url + "/company" + token)
    print(r.text)
    companies = json.loads(r.text)

    rateList = []
    rateReverseList = []

    i = 0
    while i < currencyList.__len__():

        j = 0
        while j < currencyList.__len__():
            if i != j:
                r = requests.get(url + "/rate/midMarket/" + currencyList[i] + "/" + currencyList[j] + token)
                rate = json.loads(r.text)
                rateList.append({'sourceCurrency': currencyList[i], 'targetCurrency': currencyList[j], 'rate': rate["rate"]})

                r = requests.get(url + "/rate/midMarket/" + currencyList[j] + "/" + currencyList[i] + token)
                rate = json.loads(r.text)
                rateReverseList.append({'sourceCurrency': currencyList[j], 'targetCurrency': currencyList[i], 'rate': rate["rate"]})
            j += 1
        i += 1

    quoteList = []
    i = 0
    while i < rateList.__len__():

        r = requests.get(
            url + "/quote/100/" + rateList[i]["sourceCurrency"] + "/" + rateList[i]["targetCurrency"] + token)
        print(r.text)
        quote = json.loads(r.text)
        quoteList.append(quote)

        i += 1

    companyList = companies["companies"][1: len(companies["companies"]) - 1]
    companyList = companyList.split(", ")

    i = 0
    while i < companyList.__len__():
        j = 0
        while j < rateList.__len__():

            hiddenFeePercentage = (100 * rateList[j]["rate"] - quoteList[j][companyList[i]]["recipientReceives"]) * rateReverseList[j]["rate"]

            r = requests.post(url + "/hiddenFee/forCompany/" + companyList[i] + "/100/" + rateList[j]["sourceCurrency"] + "/" + rateList[j]["targetCurrency"] + "/" + str(hiddenFeePercentage) + token)
            print(r.text)
            r = requests.post(url + "/hiddenFee/forCompany/" + companyList[i] + "/1000/" + rateList[j]["sourceCurrency"] + "/" + rateList[j]["targetCurrency"] + "/" + str(hiddenFeePercentage) + token)
            print(r.text)
            r = requests.post(url + "/hiddenFee/forCompany/" + companyList[i] + "/10000/" + rateList[j]["sourceCurrency"] + "/" + rateList[j]["targetCurrency"] + "/" + str(hiddenFeePercentage) + token)
            print(r.text)

            j += 1

        i += 1


taskStart(4)
task4()
taskFinish()
