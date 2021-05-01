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

             cd Seeker

             pip3 install -r requirements.txt

Usage :
             
             python3 seeker.py -h 
  
             python3 seeker.py -d <domain name>

             python3 seeker.py -d <domain name> -p <proxy>
             
Output :

             python3 seeker.py -d <domain name>
             
             Output will be saved in current working directory as result.txt
             
             python3 seeker.py -d <domain name> -p <proxy>
             
             Output will again be saved in current working directory as result.txt
             
API KEYS:

  [Alien Vault](https://otx.alienvault.com/)

  [Shodan](https://www.shodan.io/)
  
  [Binary Edge](https://www.binaryedge.io/)
  
  [Chaos](https://chaos.projectdiscovery.io/#/)
  
  [Security Trails](https://securitytrails.com/)
  
  [Recon Dev](https://recon.dev/)
  
  [Virus Total](https://www.virustotal.com/gui/)
  
  [Censys](https://censys.io/)
  
  [Certspotter](https://sslmate.com/certspotter/api/)
  
  [Spyse](https://spyse.com/)
  
  Troubleshooting:
  
                   Cannot run source - This means that no api key was given in config.py file inside config directory
                   
                   Out of request wait for sometime - This might mean that source is getting too much request
                   
                   Check your api- This might mean that your api is out of request count, can't use the same api key anymore
