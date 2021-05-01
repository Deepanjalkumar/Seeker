import requests
from termcolor import colored, cprint

def certsh_domain(domain):
    try:
        r=requests.get(f"https://crt.sh/?q={domain}&output=json")
        data=r.json()
        with open("result.txt", "a") as file:
            for i in range(0, len(data)):
                try:
                    file.writelines("%s\n" % data[i]["common_name"])
                    print(colored("[Certsh]"+" "+data[i]["common_name"], "blue"))
                except Exception as e:
                    print("Check your api")
    except Exception as e:
        print("Cannot run source certsh")



def certsh_domain_proxy(domain, proxy):
    try:
        proxies = {
            "http": f"http://{proxy}",
            "https": f"https://{proxy}"
        }
        r=requests.get(f"https://crt.sh/?q={domain}&output=json", proxies=proxies)
        data=r.json()
        with open("result.txt", "a") as file:
            for i in range(0, len(data)):
                try:
                    file.writelines("%s\n" % data[i]["common_name"])
                    print(colored("[Certsh]"+" "+data[i]["common_name"], "blue"))
                except Exception as e:
                    print("Check your api")
    except Exception as e:
        print("Cannot run source certsh")
