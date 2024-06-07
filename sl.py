import random
import datetime
import time
import os

#总奖励
sumrewards = 0
countnum = 20000
countwin = 0
numbers = []
# 定义图标
icons = ['桃子', '西瓜', '苹果', '香蕉', '梨子', '樱桃', '黄瓜', '橙子', '柠檬', '包菜', '双7', '金钟', '锄头', '麻将', '扑克']

# 定义每个格子中每个图标的权重
grid_probs = [
    [0.1, 0.08, 0.07, 0.06, 0.05, 0.04, 0.04, 0.03, 0.03, 0.02, 0.02, 0.02, 0.01, 0.01, 0.01],  # 格子1
    [0.15, 0.07, 0.09, 0.04, 0.06, 0.03, 0.03, 0.02, 0.02, 0.02, 0.01, 0.01, 0.01, 0.01, 0.01],  # 格子2
    [0.1, 0.08, 0.07, 0.06, 0.05, 0.04, 0.04, 0.03, 0.03, 0.02, 0.02, 0.02, 0.01, 0.01, 0.01],  # 格子3
    [0.15, 0.07, 0.09, 0.04, 0.06, 0.03, 0.03, 0.02, 0.02, 0.02, 0.01, 0.01, 0.01, 0.01, 0.01],  # 格子4
    #[0.1, 0.08, 0.07, 0.06, 0.05, 0.04, 0.04, 0.03, 0.03, 0.02, 0.02, 0.02, 0.01, 0.01, 0.01],  # 格子5
    [1, 2, 3, 0.06, 0.05, 0.04, 0.04, 0.03, 0.03, 0.02, 0.02, 0.02, 0.01, 0.01, 0.01],  # 格子5
    # ... 为其他格子添加权重分布
]

# 生成5个格子的图标
def generate_grid():
    return [random.choices(icons, weights=prob_dist, k=1)[0] for prob_dist in grid_probs]

# 检查连续图标并给予奖励
def check_reward(grid):
    rewards = 0
    icon_groups = {
        icons[0]: {1: 0, 2: 12, 3: 13, 4: 14, 5: 15},
        icons[1]: {1: 0,2: 22, 3: 23, 4: 24, 5: 25},
        icons[2]: {1: 0,2: 32, 3: 33, 4: 34, 5: 35},
        icons[3]: {1: 0,2: 42, 3: 43, 4: 44, 5: 45},
        icons[4]: {1: 0,2: 52, 3: 53, 4: 54, 5: 55},
        icons[5]: {1: 0,2: 62, 3: 63, 4: 64, 5: 65},
        icons[6]: {1: 0,2: 72, 3: 73, 4: 74, 5: 75},
        icons[7]: {1: 0,2: 82, 3: 83, 4: 84, 5: 85},
        icons[8]: {1: 0,2: 92, 3: 93, 4: 94, 5: 95},
        icons[9]: {1: 0,2: 102, 3: 103, 4: 104, 5: 105},
        icons[10]: {1: 0,2: 112, 3: 113, 4: 114, 5: 115},
        icons[11]: {1: 0,2: 122, 3: 123, 4: 124, 5: 125},
        icons[12]: {1: 0,2: 132, 3: 133, 4: 134, 5: 135},
        icons[13]: {1: 0,2: 142, 3: 143, 4: 144, 5: 145},
        icons[14]: {1: 0,2: 152, 3: 153, 4: 154, 5: 155} 
    }

    current_streak = 1 
    last_icon = grid[0]
    first_streak_icon = None
    first_streak_length = 0

   
    if grid[0] != grid[1]:
        current_streak = 1
    elif grid[1] != grid[2]:
        current_streak = 2
    elif grid[2] != grid[3]:
        current_streak =3
    elif grid[3] != grid[4]:
        current_streak =4
    else:
        current_streak=5    
    
    rewards = icon_groups[grid[0]][current_streak]


    if rewards > 0:
       # print(f"总奖励：{rewards} 分！")
        return rewards  # 确保返回非零值，表示有奖励
        
    else:
        # print("没有连续图标，无奖励。")
        return 0  # 明确返回0，表示无奖励
    print("游戏结束")




# 主程序
results = []

for i in range(countnum):
    grid = generate_grid()
    #current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:")   #时间格式
    current_time = int(round(time.time() * 1000000))  #毫秒千分位
    result_text = f"游戏 {i+1}: 时间：{current_time}"
    result_text += f"生成的格子： {', '.join(grid)}"
    rewards = check_reward(grid)  
    sumrewards += rewards
    
    
    
    if rewards:
        result_text += f",获得奖励：{rewards} 分！\n"
        countwin += 1
        numbers.append(rewards)
    else:
        result_text += ",没有连续图标，无奖励。\n"  
    
    
    #result_text += "游戏结束\n"
    
    # 向结果列表中添加一个新的结果文本
    results.append(result_text)

#统计每个奖励出现的次数
def count_occurrences(numbers):
    # 初始化一个空字典来存储每个数值及其出现的次数
    counts = {}
    
    # 遍历数值列表
    for number in numbers:
        # 如果数值已经在字典中，则增加其计数
        if number in counts:
            counts[number] += 1
        # 如果数值不在字典中，则添加到字典并设置计数为1
        else:
            counts[number] = 1
    
    return counts


result_text += f"游戏进行了{countnum}次，最终总奖励：{sumrewards} 分！\n"
result_text += f"总中奖次数：{countwin} 次！中奖率为{countwin/ countnum},平均奖励为{sumrewards/countnum}\n"
result_text += f"每个奖励出现的次数：{count_occurrences(numbers)} 次！"
results.append(result_text)
# 将所有结果写入一个文件
file_name = f"game_results_{datetime.datetime.now()}.txt"
#文件名如果为时间
file_path = os.path.join('/Users/xiaobai/Documents/pythontest/', file_name)

try:
    with open(file_path, 'w', encoding='utf-8') as file:
#   a代表跟着后面写的模式
#   with open(file_path, 'a', encoding='utf-8') as file:
        file.write(''.join(results))
except IOError as e:
    print(f"文件操作失败: {e}")

