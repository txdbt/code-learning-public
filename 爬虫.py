import requests

url="https://api.bilibili.com/x/kv-frontend/namespace/data?appKey=333.1333&nscode=0&versionId=1737633097297"

wz={"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42',
    "referer": 'https://www.bilibili.com/video/BV1kYD5Y5EJ9/?spm_id_from=333.1387.homepage.video_card.click&vd_source=459844ddc21a6c43bf7f244c68da35be'}

res = requests.get(url,headers = wz)


open("2233.mp4","wb").write(res.content)

print(res.status_code)









