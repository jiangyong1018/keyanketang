import json

def zhenghe(json_path,save_path):
    # 读取JSON文件
    name_danmu = (((json_path.split('\\'))[-1].split('.'))[0]).split('_')[-1]
    with open(json_path,'r', encoding='utf-8') as file:
        data = json.load(file)
    # 按照seconds将评论内容保存
    result_dict = {}
    current_key = None

    for entry in data:
        seconds = entry["seconds"]
        comment = entry["d"]
        date = entry["date"]

        # 计算当前时间片的键值
        current_key = int(seconds / 90) * 90

        # 将评论内容保存到对应键值的字典中
        if current_key not in result_dict:
            result_dict[current_key] = {"seconds": current_key, "d": "", "date": date}
        result_dict[current_key]["d"] += comment.replace("\n", "") + " "
        # 增加评论数量
        if "comment_count" not in result_dict[current_key]:
            result_dict[current_key]["comment_count"] = 0
        result_dict[current_key]["comment_count"] += 1
    # 构造新的JSON数据
    output_data = list(result_dict.values())
    # 删除最后一组数据
    if output_data:
        output_data.pop()
    # 将结果保存到新的JSON文件
    with open(f"{save_path}\\danmu_min_{name_danmu}.json", 'w', encoding='utf-8') as output_file:
        json.dump(output_data, output_file, ensure_ascii=False, indent=2)

# zhenghe(r"D:\desk\video\录制-545068-20231031-215655-040-德云色  7点开播！\录制-545068-20231031-215655-040-德云色  7点开播！.json",r"D:\desk\video\录制-545068-20231031-215655-040-德云色  7点开播！")