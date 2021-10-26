import os


path = "C:/Users/михаил/PycharmProjects/1824_GB_Python_1/Mikhail_Toropchin_dz_7/my_project"

result_dict = {}
count = {100:0, 1000:0, 10000:0, 100000:0}
less_than = {100:[], 1000:[], 10000:[], 100000:[]}


for root, dirs, files in os.walk(path):
    for item in os.scandir(root):
        if item.stat().st_size < 100 and os.path.isfile(os.path.join(root, item)):
            count[100] += 1
            p, n = os.path.splitext(os.path.join(root, item))
            less_than[100].append(n[1:])
        elif 100 < item.stat().st_size < 1000 and os.path.isfile(os.path.join(root, item)):
            count[1000] += 1
            p, n = os.path.splitext(os.path.join(root, item))
            less_than[1000].append(n[1:])
        elif 1000 < item.stat().st_size < 10000 and os.path.isfile(os.path.join(root, item)):
            count[10000] += 1
            p, n = os.path.splitext(os.path.join(root, item))
            less_than[10000].append(n[1:])
        elif 10000 < item.stat().st_size < 100000 and os.path.isfile(os.path.join(root, item)):
            count[100000] += 1
            p, n = os.path.splitext(os.path.join(root, item))
            less_than[100000].append(n[1:])
n = 100
while n <= 100000:
    result_dict.setdefault(n, (count[n], less_than[n]))
    n *= 10

with open("my_project_summary.json", "w", encoding="utf-8") as f:
    f.write(str(result_dict))
