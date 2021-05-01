import requests
from config import config
from termcolor import colored

def chaos_domain(domain):
    try:
        headers={"Authorization" : f"{config.chaos_api}"}
        r=requests.get(f"https://dns.projectdiscovery.io/dns/{domain}/subdomains", headers=headers)
        data=r.json()["subdomains"]
        with open("result.txt", "a") as file:
            for i in range(0, len(data)):
                try:
                    file.writelines("%s%s%s\n" % (data[i], ".", f"{domain}"))
                    print(colored("[Chaos]"+" "+data[i]+"."+f"{domain}", "blue"))
                except Exception as e:
                    print("Check your token")
    except Exception as e:
        print("Cannot run source chaos")




def chaos_domain_proxy(domain, proxy):
    try:
        proxies = {
            "http": f"http://{proxy}",
            "https": f"https://{proxy}"
        }
        headers={"Authorization" : f"{config.chaos_api}"}
        r=requests.get(f"https://dns.projectdiscovery.io/dns/{domain}/subdomains", headers=headers, proxies=proxies)
        data=r.json()["subdomains"]
        with open("result.txt", "a") as file:
            for i in range(0, len(data)):
                try:
                    file.writelines("%s%s%s\n" % (data[i], ".", f"{domain}"))
                    print(colored("[Chaos]"+" "+data[i]+"."+f"{domain}", "blue"))
                except Exception as e:
                    print("Check your token")
    except Exception as e:
        print("Cannot run source chaos")
