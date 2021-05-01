import requests
from config import config
from termcolor import colored


def trails_domain(domain):
    try:
        url = f"https://api.securitytrails.com/v1/domain/{domain}/subdomains"
        querystring = {"children_only":"false"}
        headers = {"Accept": "application/json","APIKEY": f"{config.trails_api}"}
        r = requests.get(url, headers=headers, params=querystring)
        data = r.json()["subdomains"]
        with open("result.txt", "a") as file:
            for i in range(0, len(data)):
                try:
                    file.writelines("%s%s%s\n" % (data[i], ".", f"{domain}"))
                    print(colored("[Security Trails]"+" "+data[i]+"."+f"{domain}", "blue"))
                except Exception as e:
                    print("Out of api request")
    except Exception as e:
        print("Cannot run source security trails")



def trails_domain_proxy(domain, proxy):
    try:
        proxies = {
            "http": f"http://{proxy}",
            "https": f"https://{proxy}"
        }
        url = f"https://api.securitytrails.com/v1/domain/{domain}/subdomains"
        querystring = {"children_only":"false"}
        headers = {"Accept": "application/json","APIKEY": f"{config.trails_api}"}
        r = requests.get(url, headers=headers, params=querystring, proxies=proxies)
        data = r.json()["subdomains"]
        with open("result.txt", "a") as file:
            for i in range(0, len(data)):
                try:
                    file.writelines("%s\n" % data[i])
                    print(colored("[Security Trails]"+" "+data[i]+"."+f"{domain}", "blue"))
                except Exception as e:
                    print("Out of api request")
    except Exception as e:
        print("Cannot run source security trails")
