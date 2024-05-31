import random
f = open("/Users/xiaobai/Documents/python/num.txt","w")
# 执行次数
n = 20
#总计升级次数
sumcount = 0
#轮次
total = 1
while total <= n:
    #成功率
    p1 = 0.8
    #失败降级概率
    p2 = 0.5
    #失败保级概率
    p3 = 0.2
    #升级次数
    maxlevel = 5
    #初始等级 
    level = 0
    #锻造次数
    # 初始化计数器和等级为0
    count = 0
    # 循环直到等级达到最大值
    while level < maxlevel:
        # 每次循环，计数器加1
        count += 1
        # 生成0到1之间的随机数
        random_number = random.random()
        print(random_number)
        
        # 如果随机数小于等于p1，等级上升并更新概率值
        if(random_number <= p1):
            level +=1
            p1 -=0.05
            p2 +=0.02
            p3 +=0.03
            print("当前等级",level)
        
        # 若随机数在p1到p1+p2之间且等级小于等于2，等级保持不变
        #（表示在这个范围内不会掉级）
        elif(random_number <= p1 + p2 and level <= 2):
            level = level
            print("当前等级",level)
        
        # 若随机数在p1到p1+p2之间且等级大于2，等级下降并更新概率值
        elif(random_number <= p1 + p2 and level > 2):
            level -=1
            p1 +=0.05
            p2 -=0.02
            p3 -=0.03
            print("当前等级",level)
        
        # 其他情况，等级保持不变
        else:
            level = level
            print("当前等级",level)
#    print("第", total,"轮，锻造了", count,"次")
    f.write("第"+str(total) +"轮，锻造了:"+str(count)+"次"+"\n")

    total +=1
    sumcount = sumcount + count 
print("合计运行",total-1,"轮，合计升级了", sumcount,"次，平均每轮升级",sumcount/(total-1),"次。")
f.write("合计锻造了"+str(sumcount))
f.close()