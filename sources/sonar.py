import requests
from termcolor import colored, cprint
def sonar_domain(domain):
    try:
        r=requests.get(f"https://sonar.omnisint.io/subdomains/{domain}?page=")
        data=r.json()
        with open("result.txt", "a") as file:
            for i in range(0, len(data)):
                try:
                    file.writelines("%s\n" % data[i])
                    print(colored("[Project Sonar]"+" "+data[i], "blue"))
                except Exception as e:
                    pass
    except Exception as e:
        print("Cannot run source Project Sonar")



def sonar_domain_proxy(domain, proxy):
    try:
        proxies = {
            "http": f"http://{proxy}",
            "https": f"https://{proxy}"
        }
        r=requests.get(f"https://sonar.omnisint.io/subdomains/{domain}?page=", proxies=proxies)
        data=r.json()
        with open("result.txt", "a") as file:
            for i in range(0, len(data)):
                try:
                    file.writelines("%s\n" % data[i])
                    print(colored("[Project Sonar]"+" "+data[i], "blue"))
                except Exception as e:
                    pass
    except Exception as e:
        print("Cannot run source Project Sonar")
