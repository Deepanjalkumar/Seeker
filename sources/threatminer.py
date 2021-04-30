import requests
from termcolor import colored, cprint

def threatminer_domain(domain):
    try:
        r=requests.get(f"https://api.threatminer.org/v2/domain.php?q={domain}&rt=5")
        data=r.json()["results"]
        with open("result.txt", "a") as file:
            for i in range(0, len(data)):
                try:
                    file.writelines("%s\n" % data[i])
                    print(colored("[Threatminer]"+" "+data[i], "blue"))
                except Exception as e:
                    print("Out of api request")
    except Exception as e:
        print("Cannot run source threatminer")

def threatminer_domain_proxy(domain, proxy):
    try:
        proxies = {
            "http": f"http://{proxy}",
            "https": f"https://{proxy}"
        }
        r=requests.get(f"https://api.threatminer.org/v2/domain.php?q={domain}&rt=5", proxies=proxies)
        data=r.json()["results"]
        with open("result.txt", "a") as file:
            for i in range(0, len(data)):
                try:
                    file.writelines("%s\n" % data[i])
                    print(colored("[Threatminer]"+" "+data[i], "blue"))
                except Exception as e:
                    print("Out of api request")
    except Exception as e:
        print("Cannot run source threatminer")
