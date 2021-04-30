import requests
from config import config
from termcolor import colored


def recondev_domain(domain):
    try:
        headers={'Accept' : 'application/json'}
        r=requests.get(f"https://recon.dev/api/search?key={config.recondev_api}&domain={domain}", headers=headers)
        data=r.json()
        with open("result.txt", "a") as file:
            for i in range(0, len(data)):
                try:
                    for j in range(0, len(data[i]["rawDomains"])):
                        file.writelines("%s\n" % data[i]["rawDomains"][j])
                        print(colored("[Recon Dev]"+" "+data[i]["rawDomains"][j], "blue"))
                except Exception as e:
                    print("Out of api request")
    except Exception as e:
        print("Cannot run source recondev")



def recondev_domain_proxy(domain, proxy):
    try:
        proxies = {
            "http": f"http://{proxy}",
            "https": f"https://{proxy}"
        }
        headers={'Accept' : 'application/json'}
        r=requests.get(f"https://recon.dev/api/search?key={config.recondev_api}&domain={domain}", headers=headers, proxies=proxies)
        data=r.json()
        with open("result.txt", "a") as file:
            for i in range(0, len(data)):
                try:
                    for j in range(0, len(data[i]["rawDomains"])):
                        file.writelines("%s\n" % data[i]["rawDomains"][j])
                        print(colored("[Recon Dev]"+" "+data[i]["rawDomains"][j], "blue"))
                except Exception as e:
                    print("Out of api request")
    except Exception as e:
        print("Cannot run source recondev")