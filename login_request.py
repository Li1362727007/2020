import requests
def requests_login(url,data,token=None):
    header = {'X-Lemonban-Media-Type': 'lemonban.v2', 'Content-Type': 'application/json', 'Authorization': token}
    response=requests.post(url,data,headers=header)
    result=response.json()
    return result

url = "http://120.78.128.25:8766/futureloan/member/login"
payload = '{"mobile_phone": "18855123497","pwd": "lemon123456"}'
login_result=requests_login(url,payload)
print(login_result)