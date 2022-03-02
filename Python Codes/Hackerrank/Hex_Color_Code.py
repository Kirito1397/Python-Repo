import re
line = int(input())
output = []
for lines in range(line):
    hex = str(input())
    print(hex)
    # pattern = re.compile(r"(#[0-9a-fA-F]{3,6})")
    temp = re.findall(r"(?<=.)#{1}[0-9A-Fa-f]{3,6}",hex)
    if bool(temp):
        # print(temp)
        output.extend(temp)
for x in range(len(output)):
    print(output[x])

    # [#[0-9a-fA-F]{6}]?|#[0-9a-fA-F]{3}[^\n]

