import requests
from termcolor import colored, cprint
from config.config import spyse_api
def spyse_domain(domain):
    try:
        url = "https://api.spyse.com/v3/data/domain/subdomain"
        querystring = {"domain":f"{domain}","limit":"100"}
        headers = {"Accept": "application/json", "Authorization": "Bearer %s" % spyse_api}
        r = requests.request("GET", url, headers=headers, params=querystring)
        data=r.json()["data"]["items"]
        with open("result.txt", "a") as file:
            for i in range(0, len(data)):
                try:
                    file.writelines("%s\n" % data[i]["name"])
                    print(colored("[Spyse]"+" "+data[i]['name'], "blue"))
                except Exception as e:
                    print("Check your api")
    except Exception as e:
        print("Cannot run source spyse")



def spyse_domain_proxy(domain, proxy):
    try:
        proxies = {
            "http": f"http://{proxy}",
            "https": f"https://{proxy}"
        }
        url = "https://api.spyse.com/v3/data/domain/subdomain"
        querystring = {"domain":f"{domain}","limit":"100"}
        headers = {"Accept": "application/json", "Authorization": "Bearer %s" % spyse_api}
        r = requests.request("GET", url, headers=headers, params=querystring, proxies=proxies)
        data=r.json()["data"]["items"]
        with open("result.txt", "a") as file:
            for i in range(0, len(data)):
                try:
                    file.writelines("%s\n" % data[i]["name"])
                    print(colored("[Spyse]"+" "+data[i]['name'], "blue"))
                except Exception as e:
                    print("Check your api")
    except Exception as e:
        print("Cannot run source spyse")
