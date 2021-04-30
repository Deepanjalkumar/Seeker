import requests
from termcolor import colored, cprint
def alienvault_domain(domain):
    try:
        r=requests.get(f"https://otx.alienvault.com/api/v1/indicators/domain/{domain}/passive_dns")
        data=r.json()["passive_dns"]
        with open("result.txt", "a") as file:
            for i in range(0, len(data)):
                try:
                    file.writelines("%s\n" % data[i]["hostname"])
                    print(colored("[Alien Vault]"+" "+data[i]["hostname"], "blue"))
                except Exception as e:
                    print("Out of api request")
    except Exception as e:
        print("Cannot run source alien vault")




def alienvault_domain_proxy(domain, proxy):
    try:
        proxies = {
            "http": f"http://{proxy}",
            "https": f"https://{proxy}"
        }
        r=requests.get(f"https://otx.alienvault.com/api/v1/indicators/domain/{domain}/passive_dns", proxies=proxies)
        data=r.json()["passive_dns"]
        with open("result.txt", "a") as file:
            for i in range(0, len(data)):
                try:
                    file.writelines("%s\n" % data[i]["hostname"])
                    print(colored("[Alien Vault]"+" "+data[i]["hostname"], "blue"))
                except Exception as e:
                    print("Out of api request")
    except Exception as e:
        print("Cannot run source alien vault")