import requests
from termcolor import colored
from config import config


def virus_domain(domain):
    try:
        url = 'https://www.virustotal.com/vtapi/v2/domain/report'
        params = {'apikey':f'{config.virustotal_api}', 'domain': f'{domain}'}
        r = requests.get(url, params=params)
        data=r.json()["subdomains"]
        with open("result.txt", "a") as file:
            for i in range(0, len(data)):
                try:
                    file.writelines("%s\n" % data[i])
                    print(colored("[Virus Total]"+" "+data[i], "blue"))
                except Exception as e:
                    print("Check your api")
    except Exception as e:
        print("Cannot run source virus total")


def virus_domain_proxy(domain, proxy):
    try:
        proxies = {
            "http": f"http://{proxy}",
            "https": f"https://{proxy}"
        }
        url = 'https://www.virustotal.com/vtapi/v2/domain/report'
        params = {'apikey':f'{config.virustotal_api}', 'domain': f'{domain}'}
        r = requests.get(url, params=params, proxies=proxies)
        data=r.json()["subdomains"]
        with open("result.txt", "a") as file:
            for i in range(0, len(data)):
                try:
                    file.writelines("%s\n" % data[i])
                    print(colored("[Virus Total]"+" "+data[i], "blue"))
                except Exception as e:
                    print("Check your api")
    except Exception as e:
        print("Cannot run source virus total")
