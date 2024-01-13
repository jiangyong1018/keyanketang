import subprocess
import os


def convert_flv_to_audio(input_file, output_directory, segment_length=90):
    # 创建输出目录
    os.makedirs(output_directory, exist_ok=True)

    # 获取视频时长
    duration_command = ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', input_file]
    duration = float(subprocess.check_output(duration_command).decode('utf-8').strip())

    # 计算段数
    num_segments = int(duration / segment_length)

    # 获取源文件名称（不包括扩展名）
    base_name = os.path.splitext(os.path.basename(input_file))[0]

    # 使用FFmpeg将FLV视频转换为音频
    for i in range(num_segments):
        start_time = i * segment_length
        end_time = (i + 1) * segment_length
        time_str = f"{start_time:02d}_{end_time:02d}"  # 格式化时间信息

        output_file = os.path.join(output_directory, f"{base_name}_{time_str}.wav")

        ffmpeg_command = [
            'ffmpeg',
            '-i', input_file,
            '-ss', str(start_time),
            '-t', str(segment_length),
            '-acodec', 'pcm_s16le',
            '-ar', '44100',
            '-ac', '2',
            output_file
        ]

        subprocess.run(ffmpeg_command)
'''# 设置输入FLV视频文件路径
input_video_file = r"E:\bilibilivideo\21690102-丐伦菌\录制-21690102-20230913-202206-069-金牌导师上线！.flv"

# 设置输出目录
output_directory = r"D:\desk\aa"

# 调用函数进行视频转音频并切分
convert_flv_to_audio(input_video_file, output_directory)
'''