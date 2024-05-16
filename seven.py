import random  
  
# 生成一个1到10之间的随机整数  
random_number = random.randint(1, 10)  
  
# 定义一个变量来存储用户的猜测  
guess = None  
  
# 游戏循环，直到用户猜对为止  
while guess != random_number:  
    # 提示用户输入猜测  
    guess = int(input("请猜一个1到10之间的整数："))  
  
    # 检查用户的猜测  
    if guess < random_number:  
        print("猜小了！")  
    elif guess > random_number:  
        print("猜大了！")  
  
# 如果用户猜对了，显示恭喜信息  
print("恭喜你，猜对了！")
