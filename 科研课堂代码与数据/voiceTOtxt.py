import os
import whisper
import json


def voice_txt(video_path, output_dir):
    # 获取视频文件的名称（不包括扩展名）
    video_name = os.path.splitext(os.path.basename(video_path))[0]

    # 构造txt文件路径
    output_txt_path = os.path.join(output_dir, f"{video_name}_transcription.txt")

    model = whisper.load_model("base")
    result = model.transcribe(video_path)

    # 获取结果文本
    transcribed_text = result["text"]

    # # 将结果保存到txt文件
    # with open(output_txt_path, 'w', encoding='utf-8') as txt_file:
    #     txt_file.write(transcribed_text)

    # 读取原始JSON文件
    video_name_0 = (video_name.split('_'))[0]
    source_file_path = f'{output_dir}\\danmu_min_{video_name_0}.json'

    with open(source_file_path, 'r', encoding='utf-8') as source_file:
        records = json.load(source_file)

    # 遍历每个记录，添加新元素"s"（仅对"seconds"等于0的记录）
    for record in records:
        if record["seconds"] == int((video_name.split('_'))[1]):
            record["s"] = transcribed_text  # 这里可以根据需要修改

    # 更新JSON数据到原始文件
    with open(source_file_path, 'w', encoding='utf-8') as source_file:
        json.dump(records, source_file, ensure_ascii=False, indent=2)

    print("更新后的JSON数据已保存到文件:", source_file_path)
'''# 示例用法
input_video_path = r"D:\desk\aa\your_video.flv"
output_directory = r"D:\desk\aa"
voice_txt(input_video_path, output_directory)
'''