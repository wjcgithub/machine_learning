# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

这是一个机器学习学习笔记项目，使用 Jupyter Notebook 实践和演示各种机器学习算法。主要围绕用户生命周期价值（LTV）预测场景展开。

## 常用命令

```bash
# 启动 Jupyter Lab
jupyter lab

# 启动 Jupyter Notebook
jupyter notebook
```

## 项目结构

### 核心 Notebook 文件

| 文件 | 主题 |
|------|------|
| `supervised_learning.ipynb` | 监督学习基础：线性回归、决策树、随机森林预测 LTV |
| `防止过拟合-LTV-Lasso和Ridge回归.ipynb` | 正则化防止过拟合 |
| `防止过拟合-LTV-决策树的剪枝.ipynb` | 决策树剪枝防止过拟合 |
| `LTV-拆分K折交叉验证.ipynb` | K 折交叉验证 |
| `LTV-网络搜索参数调优.ipynb` | 网格搜索超参数调优 |
| `no_supervised_learning_rfm.ipynb` | 无监督学习：RFM 聚类 |
| `怎么用特征工程提高模型效率.ipynb` | 特征工程：选择、变换、构建 |
| `loudou.ipynb` | 漏斗分析 |

### 数据文件

- `orders.csv` - 订单数据（用于 LTV 预测）
- `data.csv` - 通用数据集

### 辅助工具

- `font.py` - 设置 Matplotlib/Seaborn 中文字体（跨平台兼容）

## 依赖库

```
pandas
numpy
matplotlib
seaborn
scikit-learn
```

## 机器学习工作流

项目遵循标准的机器学习流程：

1. **数据导入与清洗** - 处理日期格式、删除重复值
2. **特征工程** - RFM 特征构建（R=最近消费、F=消费频率、M=消费金额）
3. **数据集拆分** - train_test_split（70% 训练 / 15% 验证 / 15% 测试）
4. **特征缩放** - StandardScaler 或 MinMaxScaler
5. **模型训练** - 线性回归、Lasso、Ridge、决策树、随机森林等
6. **模型评估** - R² 分数、MAE 等

## 常用代码模式

```python
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 数据集拆分
from sklearn.model_selection import train_test_split
X_train, X_rem, y_train, y_rem = train_test_split(X, y, train_size=0.7, random_state=36)
X_valid, X_test, y_valid, y_test = train_test_split(X_rem, y_rem, test_size=0.5, random_state=36)

# RFM 特征构建
df_R_value = df_sales.groupby('用户码').消费日期.max().reset_index()
df_R_value['R值'] = (df_R_value['最近购买日期'].max() - df_R_value['最近购买日期']).dt.days
```
