
import json
import csv
import motion_get
import jiaohu
import os

# 指定包含JSON文件的文件夹路径
json_folder_path = r'D:\desk\video\over'
# 获取文件夹内所有JSON文件的文件名
json_files = [f for f in os.listdir(json_folder_path) if f.endswith('.json')]

# 处理每个JSON文件
for json_file in json_files:
    # 读取包含JSON数据的文件
    # 构建JSON文件的完整路径
    json_file_path = os.path.join(json_folder_path, json_file)
    #with open(r'D:\desk\clear_data\danmu_min_录制-9048914-20231024-201925-403-今天电一宗师看看有无狼人杀.json', 'r', encoding='utf-8') as file:
    with open(json_file_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    for entry in json_data:
        entry['hudongdu'] = jiaohu.jiaohu(entry['s'], entry['d'])

        processed_values = motion_get.calculate_chinese_emotion_bert(entry['d'])
        entry['d_pos'] = processed_values[0]  # 保存列表第一个元素
        entry['d_neg'] = processed_values[1]  # 保存列表第二个元素

        processed_values = motion_get.calculate_chinese_emotion_bert(entry['s'])
        entry['s_pos'] = processed_values[0]  # 保存列表第一个元素
        entry['s_neg'] = processed_values[1]  # 保存列表第二个元素

    # 计算comment_count的总和
    total_comment_count = sum(entry["comment_count"] for entry in json_data)


    print(f"处理文件 {json_file}，comment_count总和: {total_comment_count},alljson{len(json_data)}")

    # 保存处理后的结果到CSV文件
    csv_file_path = 'test_all.csv'
    with open(csv_file_path, 'a', encoding='utf-8', newline='') as csv_file:
        # 指定需要保存的字段
        fieldnames = ['d_pos', 'd_neg', 's_pos', 's_neg', 'hudongdu', 'comment_count']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # 写入CSV文件的表头
        # csv_writer.writeheader()

        # 写入每条数据
        for entry in json_data:
            # 创建一个新字典，只包含需要保存的字段
            row_to_write = {
                'd_pos': entry['d_pos'],
                'd_neg': entry['d_neg'],
                's_pos': entry['s_pos'],
                's_neg': entry['s_neg'],
                'hudongdu': entry['hudongdu'],
                'comment_count': entry['comment_count']


            }
            csv_writer.writerow(row_to_write)
    # 打印结果
    print(f"处理文件 {json_file}，comment_count总和: {total_comment_count}")
print("处理后的结果已保存到", csv_file_path)
