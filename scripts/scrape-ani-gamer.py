import requests_html
# import json

url = "https://ani.gamer.com.tw/"
session = requests_html.HTMLSession()

# 设置自定义 User-Agent 头部
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
response = session.get(url, headers=headers)

# 检查请求是否成功
if response.status_code == 200:
    # 初始化一个列表来存储数据
    data_list = []
    # 爬取数据并存储到列表中
    for i in range(6):
        name = response.html.find('.anime-name-block')[i].find('p')[1].text
        description = response.html.find('.anime-name-block')[i].find('p')[2].text
        
        # 将每一项数据存储到字典中
        data_dict = {
            'name': name,
            'description': description
        }
        
        # 将字典添加到列表中
        data_list.append(data_dict)
        
    print(data_list)

    # # 将列表数据写入 JSON 文件
    # with open('anime_data.json', 'w') as f:
    #     json.dump(data_list, f, ensure_ascii=False, indent=4)
else:
    print(f"请求失败，状态码：{response.status_code}")