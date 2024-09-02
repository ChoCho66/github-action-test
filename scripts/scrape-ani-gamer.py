import requests_html
# import json

url = "https://ani.gamer.com.tw/"
session = requests_html.HTMLSession()
response = session.get(url)

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