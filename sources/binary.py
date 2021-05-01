import requests
from config import config
from termcolor import colored


def binary_domain(domain):
    try:
        headers={'X-Key': f"{config.binary_api}"}
        r=requests.get(f"https://api.binaryedge.io/v2/query/domains/subdomain/{domain}", headers=headers)
        data=r.json()["events"]
        with open("result.txt", "a") as file:
            for i in range(0, len(data)):
                try:
                    file.writelines("%s\n" % data[i])
                    print(colored("[Binary edge]"+" "+data[i]+" ", "blue"))
                except Exception as e:
                    pass
    except Exception as e:
        print("Cannot run source binary edge")



def binary_domain_proxy(domain, proxy):
    try:
        proxies = {
            "http": f"http://{proxy}",
            "https": f"https://{proxy}"
        }
        headers={'X-Key': f"{config.binary_api}"}
        r=requests.get(f"https://api.binaryedge.io/v2/query/domains/subdomain/{domain}", headers=headers, proxies=proxies)
        data=r.json()["events"]
        with open("result.txt", "a") as file:
            for i in range(0, len(data)):
                try:
                    file.writelines("%s\n" % data[i])
                    print(colored("[Binary edge]"+" "+data[i]+" ", "blue"))
                except Exception as e:
                    pass
    except Exception as e:
        print("Cannot run source binary edge")



