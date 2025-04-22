#!/usr/bin/python

import os
from moviepy.editor import VideoFileClip
import argparse

def extract_mp3(video_path, output_path=None, bitrate='128k'):
    """
    从视频文件中提取MP3音频
    
    参数:
    video_path (str): 输入视频文件路径
    output_path (str): 输出音频文件路径（可选）
    bitrate (str): 输出音频比特率（默认128k）
    
    返回:
    str: 成功时返回输出文件路径，失败返回None
    """
    try:
        # 检查输入文件是否存在
        if not os.path.exists(video_path):
            raise FileNotFoundError(f"视频文件未找到: {video_path}")

        # 设置默认输出路径
        if output_path is None:
            base_name = os.path.splitext(video_path)[0]
            output_path = f"{base_name}.mp3"

        # 读取视频文件并提取音频
        with VideoFileClip(video_path) as video:
            audio = video.audio
            audio.write_audiofile(
                output_path,
                codec='mp3',
                bitrate=bitrate,
                logger='bar'  # 显示进度条
            )
            audio.close()

        print(f"\n成功导出MP3文件: {output_path}")
        return output_path

    except Exception as e:
        print(f"\n错误发生: {str(e)}")
        return None

if __name__ == "__main__":
    # 设置命令行参数
    parser = argparse.ArgumentParser(description='从视频文件中提取MP3音频')
    parser.add_argument('input', help='输入视频文件路径')
    parser.add_argument('-o', '--output', help='输出MP3文件路径（可选）')
    parser.add_argument('-b', '--bitrate', default='128k',
                        help='音频比特率（如 128k, 192k, 256k）')
    
    args = parser.parse_args()

    # 执行转换
    result = extract_mp3(
        args.input,
        args.output,
        args.bitrate
    )

    if not result:
        exit(1)
