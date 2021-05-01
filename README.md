SEEKER - Seeker is an vertical subdomain enumeration tool which collect subdomain from different sources. 

Sources include :        

1 - Alien Vault
                       
2 - Anubis

3 - Binary edge

4 - Certspotter

5 - Chaos

6 - Crtsh

7 - ReconDev

8 - Security Trails

9 - Shodan

10 - Sonar

11 - Spyse

12 - Sublist3r

13 - Threatcrowd

14 - Threatminer

15 - VirusTotal

Installation :
 
             git clone https://github.com/operationfalcon/Seeker.git

             cd seeker

             pip install -r requirements.txt

Usage :
  
             python3 seeker.py -d <domain name>

             python3 seeker.py -d <domain name> -p <proxy>
             
Output :

             python3 seeker.py -d <domain name>
             
             Output will be saved in current working directory as result.txt
             
             python3 seeker.py -d <domain name> -p <proxy>
             
             Output will again be saved in current working directory as result.txt
             
API KEYS:

  [Alien Vault](https://otx.alienvault.com/)
