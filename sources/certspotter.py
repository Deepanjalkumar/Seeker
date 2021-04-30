import requests
from termcolor import colored, cprint
from config.config import certspotter_api
def certspotter_domain(domain):
    try:
        headers={'Authorization': 'Bearer %s' % certspotter_api }
        r=requests.get(f"https://api.certspotter.com/v1/issuances?domain={domain}&include_subdomains=true&expand=dns_names", headers=headers)
        data=r.json()
        with open("result.txt", "a") as file:
            for i in range(0, len(data)):
                try:
                    for j in range(0, len(data[i]["dns_names"])):
                        try:
                            file.writelines("%s\n" % data[i]["dns_names"][j])
                            print(colored("[Certspotter]"+" "+data[i]["dns_names"][j], "blue"))
                        except Exception as e:
                            print("Not found")
                except Exception as e:
                    print("out of api request")
    except Exception as e:
        print("Cannot run source certspotter")

def certspotter_domain_proxy(domain, proxy):
    try:
        proxies = {
            "http": f"http://{proxy}",
            "https": f"https://{proxy}"
        }
        headers={'Authorization': 'Bearer %s' % certspotter_api }
        r=requests.get(f"https://api.certspotter.com/v1/issuances?domain={domain}&include_subdomains=true&expand=dns_names", headers=headers, proxies=proxies)
        data=r.json()
        with open("result.txt", "a") as file:
            for i in range(0, len(data)):
                try:
                    for j in range(0, len(data[i]["dns_names"])):
                        try:
                            file.writelines("%s\n" % data[i]["dns_names"][j])
                            print(colored("[Certspotter]"+" "+data[i]["dns_names"][j], "blue"))
                        except Exception as e:
                            print("Not found")
                except Exception as e:
                    print("out of api request")
    except Exception as e:
        print("Cannot run source certspotter")
