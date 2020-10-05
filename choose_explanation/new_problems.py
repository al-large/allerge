import os
import datetime

days = ['월', '화', '수', '목', '금', '토', '일']
parent = os.path.dirname(os.getcwd())
target = parent + "\\PillowCroco"
files = os.listdir(target) + os.listdir(target + "\\DONE")
y = datetime.datetime.today().year

for filename in os.listdir(os.getcwd()):
    # 작성 안된애 찾기
    if not filename.endswith(".txt"):
        continue
    m, d = filename[:2], filename[2:4]
    check = True
    for f in files:
        if f.startswith(f'{y}-{m}-{d}'):
            check = False

    if not check:
        continue

    # 문제 수집
    probs = []
    f = open(filename, 'rt', encoding='utf-8')
    while True:
        line = f.readline().splitlines()
        if not line:
            break

        # name, prob
        probs.append((line[0], f.readline().splitlines()[0]))

    # 문제 기록
    day = days[datetime.datetime(int(y), int(m), int(d)).weekday()]
    f = open(target + f"\\{y}-{m}-{d}.md", 'wt', encoding='utf-8')
    f.write(f"""
## {y}/{int(m)}/{int(d)}/{day}, 자유주제
자기 하고 싶은 문제 2개씩


```python
# 시간 단위는 분
if 도착시간 > 시작시간 :
    벌금 += math.ceiling((도착시간-시작시간) / 5) * 500

# 'problems' is a list of problems
# 'hosts' is a list of all host who participate in the group study.
# each 'problem' has a 'host' who picks it.

for p in problems:
    for h in hosts:
        if not p.accepted and not p.explained :
            h.벌금 += 2000

        if not p.accepted and p.host is h:
            h.벌금 += 2000
```


""")
    for name, prob in probs:
        f.write(f"- [ ] {name}\n {prob}\n")
    f.write("""

---


""")

    for name, prob in probs:
        f.write(f"""### {name}
{prob}

```c++
```

---
""")

    f.close()
