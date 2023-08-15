import os
import openai
import uuid
import requests
from PIL import Image
from io import BytesIO

openai.api_key = "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"


# 图片生成参数
prompts = ["一只可爱柴犬", "一位比基尼美女", "一幅夜空的星空"]

# 指定保存文件夹路径
save_folder = "E:\\APInewproject"

# 创建保存文件夹（如果不存在）
os.makedirs(save_folder, exist_ok=True)

# 循环生成并保存图片
for index, prompt in enumerate(prompts):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']

    # 发送GET请求获取图像数据
    response = requests.get(image_url)
    image_data = response.content

    # 使用Pillow库打开图像数据
    image = Image.open(BytesIO(image_data))

    # 生成唯一的文件名
    unique_filename = str(uuid.uuid4())
    file_name = f"{unique_filename}.jpg"

    # 规范化文件名
    file_name = file_name.encode('utf-8').decode('latin-1')

    # 拼接保存文件的完整路径
    save_path = os.path.join(save_folder, file_name)

    # 以追加模式保存图像到指定文件夹中
    with open(save_path, "ab") as file:
        file.write(image_data)
