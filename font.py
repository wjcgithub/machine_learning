import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import platform

def set_chinese_font_for_seaborn():
    """
    为 Seaborn 设置中文字体
    """
    system = platform.system()
    
    if system == 'Windows':
        # Windows 字体
        font_list = ['SimHei', 'Microsoft YaHei', 'FangSong', 'KaiTi']
    elif system == 'Darwin':  # macOS
        # macOS 字体
        font_list = ['Arial Unicode MS', 'PingFang SC', 'Heiti SC', 'Hiragino Sans GB']
    else:  # Linux
        # Linux 字体
        font_list = ['DejaVu Sans', 'WenQuanYi Zen Hei', 'Noto Sans CJK']
    
    # 尝试设置字体
    for font in font_list:
        try:
            plt.rcParams['font.sans-serif'] = [font]
            matplotlib.rcParams['font.sans-serif'] = [font]
            # 测试字体是否可用
            temp_fig, temp_ax = plt.subplots()
            temp_ax.set_xlabel('测试中文')
            plt.close(temp_fig)
            print(f"✓ 已设置 Seaborn 字体为: {font}")
            break
        except:
            continue
    
    # 必须设置这一项
    plt.rcParams['axes.unicode_minus'] = False
    matplotlib.rcParams['axes.unicode_minus'] = False
    
    # Seaborn 样式设置（可选）
    sns.set_style("whitegrid")
    sns.set_context("notebook", font_scale=1.2)
