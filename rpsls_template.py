#coding:gbk
"""
���ߣ�������
���ڣ�2020��11��24��
Ŀ�꣺���RPSLS��Ϸ
"""
import random
while True:
	first_list = ['ʯͷ','����','��','����','ʷ����']
	computer = random.choice(first_list)
	user = input("������ʯͷ���������������棬ʷ����,����ѡ��Ϊ:")
	while user not in first_list:
		user=input("Error: No Correct Name")
	print('--------')
	print('����ѡ��Ϊ:%s'%user)
	print('�������ѡ��Ϊ:%s'%computer)
	if user == computer:
		print("ƽ��")
	elif (user=="����" and computer =="��") or (user == "��" and computer =="ʯͷ") or (user == "ʯͷ" and computer == "����") or (user == "ʯͷ" and computer == "����") or (user == "����" and computer == "ʷ����") or (user == "ʷ����" and computer == "����") or(user =="����" and computer == "����") or (user == "����" and computer == "��") or (user == "��" and computer == "ʷ����") or (user == "ʷ����" and computer == "ʯͷ"):
		print("��Ӯ��")
	else:
		print("����Ӯ��")
