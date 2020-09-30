import requests
import sys

def request(url):
    try:
        return requests.get("http://"+ url)
    except:
        pass

target_url = sys.argv[1]
file_path = sys.argv[2]

with open(file_path) as f:
          for line in f:
              word = line.strip()
              new_url = word + "." + target_url
              response = request(new_url)
              if response:
                  print("[+] Discovered subdomain --> " + new_url)