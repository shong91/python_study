import requests

res = requests.get("http://google.com")
# res = requests.get("http://nadocoding.tistory.com")
res.raise_for_status()
print('웹 스크래핑을 진행합니다. ')

# if res.status_code == requests.codes.ok: 
#     print('응답코드 200, 정상')
# else:
#     print('문제 발생. [에러코드: ', res.status_code, ']')

print(len(res.text))

with open('mygoogle.html', 'w', encoding="utf8") as f:
    f.write(res.text)