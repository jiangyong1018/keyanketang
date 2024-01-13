import os
import shutil
import xmlTOjson
import videoTOvoicepart
import voiceTOtxt
import danmuzhenghe
def get_name(path):
    lis=[]
    path_file = path.replace('.flv','')
    lis.append(path_file)
    lis.append(path)
    lis.append(path_file+".xml")
    lis.append(path_file+ r"\\" +((path.split('\\'))[-1].split('.'))[0] + ".json")
    return lis
def new_files(path):
    if not os.path.exists(path):
        os.makedirs(path)




if __name__ == "__main__":
    flv_folder = r"D:\desk\23503814-王者剑圣甲壳虫"  # 指定包含FLV文件的文件夹路径

    for flv_file in os.listdir(flv_folder):
        if flv_file.lower().endswith('.flv'):
            lis_path = get_name(os.path.join(flv_folder, flv_file))
            # lis_path = get_name(r"F:\9048914-古月酱cc\录制-9048914-20231024-201925-403-今天电一宗师看看有无狼人杀.flv")
            files_path = lis_path[0]
            video_path = lis_path[1]
            xml_path = lis_path[2]
            new_files(files_path)
            json_path = lis_path[3]
            # 弹幕处理
            xmlTOjson.translate_xml_jsom(xml_path, files_path)
            danmuzhenghe.zhenghe(json_path, files_path)
            # 视频处理
            video_path_out = files_path+"\\video"  # 存放视频缓存
            # 视频切分为音频
            videoTOvoicepart.convert_flv_to_audio(video_path, video_path_out)
            # 音频转写
            for root, dirs, files in os.walk(video_path_out):
                for file in files:
                    if file.lower().endswith('.wav'):
                        voiceTOtxt.voice_txt(os.path.join(root, file), files_path)
            # 删除video文件夹及其内容
            shutil.rmtree(video_path_out)