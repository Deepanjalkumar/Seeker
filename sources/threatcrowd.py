import requests
from termcolor import colored, cprint

def threatcrowd_domain(domain):
    try:
        r=requests.get(f"https://www.threatcrowd.org/searchApi/v2/domain/report/?domain={domain}")
        data=r.json()["subdomains"]
        with open("result.txt", "a") as file:
            for i in range(0, len(data)):
                try:
                    file.writelines("%s\n" % data[i])
                    print(colored("[Threatcrowd]"+" "+data[i], "blue"))
                except Exception as e:
                    pass
    except Exception as e:
        print("Cannot run source threatcrowd")



def threatcrowd_domain_proxy(domain, proxy):
    try:
        proxies = {
            "http": f"http://{proxy}",
            "https": f"https://{proxy}"
        }
        r=requests.get(f"https://www.threatcrowd.org/searchApi/v2/domain/report/?domain={domain}", proxies=proxies)
        data=r.json()["subdomains"]
        with open("result.txt", "a") as file:
            for i in range(0, len(data)):
                try:
                    file.writelines("%s\n" % data[i])
                    print(colored("[Threatcrowd]"+" "+data[i], "blue"))
                except Exception as e:
                    pass
    except Exception as e:
        print("Cannot run source threatcrowd")
