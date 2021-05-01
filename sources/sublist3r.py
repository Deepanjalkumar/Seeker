import requests
from termcolor import colored, cprint
def sublist3r_domain(domain):
    try:
        r=requests.get(f"https://api.sublist3r.com/search.php?domain={domain}")
        data=r.json()
        with open("result.txt", "a") as file:
            for i in range(0, len(data)):
                try:
                    file.writelines("%s\n" % data[i])
                    print(colored("[Sublist3r]"+" "+data[i], "blue"))
                except Exception as e:
                    print("Out of request wait for some time")
    except Exception as e:
        print("Cannot run source sublist3r")


def sublist3r_domain_proxy(domain, proxy):
    try:
        proxies = {
            "http": f"http://{proxy}",
            "https": f"https://{proxy}"
        }
        r=requests.get(f"https://api.sublist3r.com/search.php?domain={domain}", proxies=proxies)
        data=r.json()
        with open("result.txt", "a") as file:
            for i in range(0, len(data)):
                try:
                    file.writelines("%s\n" % data[i])
                    print(colored("[Sublist3r]"+" "+data[i], "blue"))
                except Exception as e:
                    print("Out of request wait for some time")
    except Exception as e:
        print("Cannot run source sublist3r")
