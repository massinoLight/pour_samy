import configparser
import requests

config = configparser.ConfigParser()
config.read('config.ini')

proxy_ip = config.get('proxy', 'ip')
proxy_port = config.get('proxy', 'port')
proxy_username = config.get('proxy', 'username')
proxy_password = config.get('proxy', 'password')

proxies = {
  'http': f'http://{proxy_username}:{proxy_password}@{proxy_ip}:{proxy_port}',
  'https': f'http://{proxy_username}:{proxy_password}@{proxy_ip}:{proxy_port}'
}

url = 'https://www.ta_page_web_de_chez_safran/le_lien_de_ton_xlsx'
response = requests.get(url, proxies=proxies)

print(response.content)

with open('ton_merveilleu_fichier.xlsx', 'wb') as file:
    file.write(response.content)
