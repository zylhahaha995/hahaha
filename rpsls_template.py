#coding:gbk
"""
作者：曾亚蕾
日期：2020年11月24日
目标：完成RPSLS游戏
"""
import random
while True:
	first_list = ['石头','剪刀','布','蜥蜴','史波克']
	computer = random.choice(first_list)
	user = input("请输入石头，剪刀，布，蜥蜴，史波克,您的选择为:")
	while user not in first_list:
		user=input("Error: No Correct Name")
	print('--------')
	print('您的选择为:%s'%user)
	print('计算机的选择为:%s'%computer)
	if user == computer:
		print("平局")
	elif (user=="剪刀" and computer =="布") or (user == "布" and computer =="石头") or (user == "石头" and computer == "剪刀") or (user == "石头" and computer == "蜥蜴") or (user == "蜥蜴" and computer == "史波克") or (user == "史波克" and computer == "剪刀") or(user =="剪刀" and computer == "蜥蜴") or (user == "蜥蜴" and computer == "布") or (user == "布" and computer == "史波克") or (user == "史波克" and computer == "石头"):
		print("您赢了")
	else:
		print("电脑赢了")
