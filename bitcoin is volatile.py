import requests
import winsound

r = requests.get('https://api.coindesk.com/v1/bpi/currentprice/CNY.json')

ans = r.json()['bpi']['USD']['rate']
print(ans)

if ans < '99500':
    winsound.PlaySound("You Suffer (Napalm Death).wav", winsound.SND_FILENAME)
    print("it ran")


