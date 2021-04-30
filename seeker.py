import argparse
from banner.banner import banner_design
from functions.function import *
import sys
banner=banner_design()

parser=argparse.ArgumentParser(description=banner, formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-d', '--domain', help='domain name for subdomain enumeration', type=str, required=True)
parser.add_argument('-p', '--proxy', help='proxy to be used for subdomain enumeration')
args=parser.parse_args()


if len(sys.argv)==3:
    shodan_domain(args.domain)
    binary_domain(args.domain)
    trails_domain(args.domain)
    chaos_domain(args.domain)
    recondev_domain(args.domain)
    spyse_domain(args.domain)
    virus_domain(args.domain)
    alienvault_domain(args.domain)
    anubis_domain(args.domain)
    certspotter_domain(args.domain)
    certsh_domain(args.domain)
    sonar_domain(args.domain)
    sublist3r_domain(args.domain)
    threatminer_domain(args.domain)
    threatcrowd_domain(args.domain)
elif len(sys.argv)==5:
    shodan_domain_proxy(args.domain, args.proxy)
    binary_domain_proxy(args.domain, args.proxy)
    trails_domain_proxy(args.domain, args.proxy)
    chaos_domain_proxy(args.domain, args.proxy)
    recondev_domain_proxy(args.domain, args.proxy)
    spyse_domain_proxy(args.domain, args.proxy)
    virus_domain_proxy(args.domain, args.proxy)
    alienvault_domain_proxy(args.domain, args.proxy)
    anubis_domain_proxy(args.domain, args.proxy)
    certspotter_domain_proxy(args.domain, args.proxy)
    certsh_domain_proxy(args.domain, args.proxy)
    sonar_domain_proxy(args.domain, args.proxy)
    sublist3r_domain_proxy(args.domain, args.proxy)
    threatminer_domain_proxy(args.domain, args.proxy)
    threatcrowd_domain_proxy(args.domain, args.proxy)