import re
ret_greed= re.findall(r'(\d+)','a23b')

# ?: 代表非捕获形括号，仅起到分组的作用
ret_greed2 = re.findall(r"(?:[1-9]{1,3}\.){3}[1-9]{1,3}", "abd.fde 123.163.1.32dbd")

result = re.findall(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])', "abd.fde 123.163.1.32dbd")

print(ret_greed2)
print result