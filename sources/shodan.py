import requests
from config import config
from termcolor import colored

def shodan_domain(domain):
    try:
        r=requests.get(f"https://api.shodan.io/dns/domain/{domain}?key={config.shodan_api}")
        data=r.json()["subdomains"]
        with open("result.txt", "w") as file:
            for i in range(0, len(data)):
                try:
                    file.writelines("%s%s%s\n" % (data[i], ".", f"{domain}") )
                    print(colored("[Shodan]"+" "+data[i]+"."+f"{domain}"+" ", "blue"))
                except Exception as e:
                    print("Check your api")
    except Exception as e:
        print("Cannot run source shodan")


def shodan_domain_proxy(domain,proxy):
    try:
        proxies={
            "http": f"http://{proxy}",
            "https": f"https://{proxy}"
        }
        r=requests.get(f"https://api.shodan.io/dns/domain/{domain}?key={config.shodan_api}", proxies=proxies)
        data=r.json()["subdomains"]
        with open("result.txt", "w") as file:
            for i in range(0, len(data)):
                try:
                    file.writelines("%s%s%s\n" % (data[i], ".", f"{domain}"))
                    print(colored("[Shodan]"+" "+data[i]+"."+f"{domain}"+" ", "blue"))
                except Exception as e:
                    print("Check your api")
    except Exception as e:
        print("Cannot run source shodan")
