# 初夏 2023/8/15 8:31 open files
# 您可以在
# `start_wechat()`
# 函数内部添加限制条件，以便在特定条件下才启动微信应用。以下是一个示例，演示如何在指定时间范围内启动微信应用：
#
# ```python
import subprocess
import datetime
import time
import tkinter as tk
from tkinter import messagebox


def is_within_time_range(start_time, end_time):
    current_time = datetime.datetime.now().time()
    return start_time <= current_time <= end_time


def start_wechat_within_time_range():
    if is_within_time_range(datetime.time(16, 0), datetime.time(18, 0)):
        wechat_path = r'C:\Program Files (x86)\Tencent\WeChat\WeChat.exe'

        try:
            subprocess.Popen(wechat_path)
            return True
        except Exception as e:
            return str(e)
    else:
        return 0


def generate_result_message(success):
    if success:
        return "生成成功！微信已启动。"
    else:
        return "生成失败。无法启动微信。"


def main():
    success = start_wechat_within_time_range()
    message = generate_result_message(success)

    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口

    messagebox.showinfo("生成结果", message)


if __name__ == "__main__":
    main()


# 在这个示例中，`is_within_time_range()`
# 函数用于检查当前时间是否在指定的时间范围内。如果是，`start_wechat_within_time_range()`
# 函数会尝试启动微信应用。如果不在时间范围内，将会返回一个相应的提示。您可以根据自己的需求添加其他限制条件，例如网络状态、设备状态等。