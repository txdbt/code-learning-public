import requests

# 要爬取的 URL
url = 'https://www.bilibili.com/video/BV1BpwgeREEM/?spm_id_from=333.337.search-card.all.click&vd_source=459844ddc21a6c43bf7f244c68da35be'

# 设置请求头，去除多余空格
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42',
    'Referer': 'https://www.bilibili.com/'
}

try:
    # 发送请求
    res = requests.get(url, headers=headers)
    
    # 检查响应状态码
    if res.status_code == 200:
        print("请求成功")
        print(res.text)
    else:
        print(f"请求失败，状态码: {res.status_code}")
except requests.exceptions.RequestException as e:
    print(f"请求发生错误: {e}")