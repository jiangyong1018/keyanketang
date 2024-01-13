import xml.etree.ElementTree as ET
import pandas as pd
import json
from datetime import datetime, timedelta
from dateutil import parser
from datetime import timezone, timedelta
'''
本代码完成任务为将xml弹幕文件转换为json文件，且包含弹幕发送时间-秒数
danmu_all_全部数据
danmu_just弹幕相关数据user args d
danmu_time增加了时间和日期
'''
def add_seconds_with_timezone(base_datetime, seconds, timezone_offset):
    fixed_datetime = base_datetime + timedelta(seconds=seconds) - timedelta(hours=timezone_offset)
    return fixed_datetime
def translate_xml_jsom(xml_path,save_path):
    # 读取文件名
    xml_name = ((xml_path.split('\\'))[-1].split('.'))[0]
    # print(xml_name)
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # 将XML根元素转换为字典
    xml_data = element_to_dict(root)

    # 将字典转换为JSON
    # 此文件包含所有信息  f"{xml_name}_danmu_all.json"
    json_data = json.dumps(xml_data, ensure_ascii=False, indent=2)
    with open(f"{save_path}\\danmu_all_{xml_name}.json", 'w', encoding='utf-8') as f:
        f.write(json_data)
    # 打印JSON数据

    # 读取JSON文件
    json_file = f"{save_path}\\danmu_all_{xml_name}.json"
    with open(json_file, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    # 打印录制时间
    print(json_data["BililiveRecorderRecordInfo"]["start_time"])
    time_start = json_data["BililiveRecorderRecordInfo"]["start_time"]
    timezone_str = time_start[-6:]
    original_str = time_start[:-6]
    datetime_obj = parser.parse(original_str) + timedelta(hours=int(timezone_str[1:3]), minutes=int(timezone_str[4:]))
    # time_start_1= time_start[:26]  # 截取前三位数字
    # time_start_1 = time_start[:23] + str(round(float(time_start[23:29]), 3)) + time_start[29:]  # 四舍五入
    # datetime_obj = datetime.fromisoformat(datetime_obj)
    d_list = json_data['d']

    # 创建一个新的 JSON 文件并将提取到的内容保存到其中
    # 此文件仅包含弹幕部分的全部信息
    output_file = f'{save_path}\\danmu_just_{xml_name}.json'  # 新JSON文件路径
    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(d_list, outfile, ensure_ascii=False, indent=2)

    df = pd.read_json(f'{save_path}\\danmu_just_{xml_name}.json')
    # 录制开始时间

    df['seconds'] = df['p'].str.split(',').str[0].astype(float)
    df['date'] = df['seconds'].apply(lambda x: add_seconds_with_timezone(datetime_obj, x, int(timezone_str[1:3])))
    # df['date'] = time_start + df['seconds'].apply(lambda x: timedelta(seconds=x))
    # print(df)
    df.to_json(f'{save_path}\\{xml_name}.json', orient='records', force_ascii=False, indent=2)

def add_seconds(base_datetime, seconds):
    fixed_datetime = base_datetime + timedelta(seconds=seconds)
    return fixed_datetime

# 定义一个函数来将XML元素转换为字典
def element_to_dict(element):
    result = {}
    if element.attrib:
        result.update(element.attrib)
    for child in element:
        child_data = element_to_dict(child)
        if child.tag in result:
            if isinstance(result[child.tag], list):
                result[child.tag].append(child_data)
            else:
                result[child.tag] = [result[child.tag], child_data]
        else:
            result[child.tag] = child_data
    if element.text:
        result[element.tag] = element.text
    return result


if __name__ == "__main__":
    xml_file = r'D:\desk\course\keyanketang\homework\test\test3.xml'  # 替换为您的XML文件路径
    translate_xml_jsom(xml_file,r"D:\desk\course\keyanketang\homework\test")
