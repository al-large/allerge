from random import shuffle
import re
import os

for filename in os.listdir(os.getcwd()):
    if filename.endswith(".txt"):
        
        name = ["희연", "동훈", "원주"] # 참여자 목록
        probs = [] # 문제 이름 목록
        f = open(filename,'rt', encoding='UTF8')
        nums = 0 # 문제 총 개수
        flag = False
        
        while True and not flag:
            line = f.readline()
            if not line:
                break

            if line == "---------------------\n":
                flag = True
                break

            if re.compile('http').match(line) or line == '\n':
                continue
            probs.append(line)
            nums += 1

        if flag:
            f.close()
            continue

            
        #print(probs)
        #print(names)
        names = []

        # 문제마다 사람 배정
        for _ in range(nums//len(name) + (1 if nums%len(name) else 0)):
            names += name

        # 7문제, 3명이면 2명은 더미 문제에 배정하기 위함.
        for _ in range(nums%len(name)):
            probs.append(".")
        
        shuffle(names)
        f.close()

        if nums:
            f = open(filename,'at', encoding='UTF8')
            f.write('\n\n---------------------\n')
            print("\t< ",filename, "> :")
            for i in range(nums):
                names[i] +=": "
                names[i] +=probs[i]
                print(names[i][:-1])
                f.write(names[i])

            f.close()
