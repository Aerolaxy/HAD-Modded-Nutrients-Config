import os
import json


directory_path = './mods'

def traversal_json_in_folder(folder_path) -> list:
    """ 遍历目录中的所有目录, 输出 json_list """
    json_list = []
    for root, dirs, files in os.walk(folder_path):
        # 遍历当前文件夹下的所有文件
        for file_name in files:
            if file_name.endswith('.json'):
                file_path = os.path.join(root, file_name)
                # 打开并读取JSON文件
                with open(file_path, 'r', encoding='utf-8') as file:
                    try:
                        # 解析JSON数据
                        json_data = json.load(file)
                        json_list.append(json_data)

                    except json.JSONDecodeError as e:
                        print(f"解析JSON文件 '{file_name}' 时出错: {e}")
    return json_list 
    

def json_list_usage(input_json_list) -> list:
    """ 处理json_list, 输出 list """

    output_list = []
    for item in input_json_list:
        item = dict(item)
        if "values" in item.keys():
            try:
                if "id" in item["values"][0].keys():
                    output_list.append(item["values"][0]["id"])
            except Exception as e:
                output_list.append(item["values"])

    return output_list


json_list = traversal_json_in_folder(directory_path)
list_out = json_list_usage(json_list)
with open('example.txt', 'w') as f:
    for i in list_out:
        f.write(str(i)+"\r\n")
