import pandas as pd

# 示例 1：基本用法
print("=== 示例 1：基本用法 ===")
data = {'颜色': ['红', '蓝', '绿', '红', '蓝']}
df = pd.DataFrame(data)
print("原始数据:")
print(df)

# 使用 get_dummies 进行独热编码
df_dummies = pd.get_dummies(df)
print("\n转换后的数据 (get_dummies):")
print(df_dummies)

# 示例 2：处理多个分类列并指定前缀
print("\n=== 示例 2：处理多个分类列并指定前缀 ===")
data2 = {
    '动物': ['猫', '狗', '猫', '鸟'],
    '大小': ['小', '大', '小', '中'],
    '数量': [1, 2, 1, 5]
}
df2 = pd.DataFrame(data2)
print("原始数据:")
print(df2)

# 指定 prefix 参数
df_dummies2 = pd.get_dummies(df2, columns=['动物', '大小'], prefix=['Type', 'Size'])
print("\n转换后的数据 (指定列和前缀):")
print(df_dummies2)

# 示例 3：Dummy Trap (虚拟变量陷阱) - drop_first=True
print("\n=== 示例 3：避免虚拟变量陷阱 (drop_first=True) ===")
# 如果有 N 个类别，其实只需要 N-1 个变量就能表示。
# 例如：如果不是红色也不是蓝色，那一定是绿色（假设只有三种颜色）。
df_dummies3 = pd.get_dummies(df, drop_first=True)
print("转换后的数据 (drop_first=True):")
print(df_dummies3)
