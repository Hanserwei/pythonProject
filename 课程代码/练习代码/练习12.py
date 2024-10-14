# 某公司发工资，一共有10000元，给20个员工发工资，员工的编号从1到20,依次领取工资，
# 但是要随机给绩效分(1-10)，绩效分低于5分则不发工资，钱发完了也就不发了。
import random

all_money = 10000
count = 0 

for x in range(1, 21):
    num = random.randint(1, 10)
    if num < 5:
        print(f"第{x}位员工，绩效分{num}，不发工资，下一位！")
        continue
    else:
        if all_money < 1000:
            print("钱发完了，拜拜！")
            break
        all_money -= 1000
        print(f"第{x}位，绩效分{num}, 发工资1000。")
        count += 1

print(count)
print(all_money)

# 为避免余额为负数，在发工资前需要检查一下工资够不够发下个员工的工资。