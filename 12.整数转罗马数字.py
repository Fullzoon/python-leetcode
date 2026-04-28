'''
罗马数字是通过添加从最高到最低的小数位值的转换而形成的。将小数位值转换为罗马数字有以下规则：

如果该值不是以 4 或 9 开头，请选择可以从输入中减去的最大值的符号，将该符号附加到结果，减去其值，然后将其余部分转换为罗马数字。
如果该值以 4 或 9 开头，使用 减法形式，表示从以下符号中减去一个符号，例如 4 是 5 (V) 减 1 (I): IV ，9 是 10 (X) 减 1 (I)：IX。仅使用以下减法形式：4 (IV)，9 (IX)，40 (XL)，90 (XC)，400 (CD) 和 900 (CM)。
只有 10 的次方（I, X, C, M）最多可以连续附加 3 次以代表 10 的倍数。你不能多次附加 5 (V)，50 (L) 或 500 (D)。如果需要将符号附加4次，请使用 减法形式。
给定一个整数，将其转换为罗马数字。
'''


def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    roman_str = ''

    count1 = int(num / 1000)
    for i in range(count1):
        roman_str += 'M'
    num = num % 1000
    if num >= 900:
        num -= 900
        roman_str += 'CM'
    elif num >= 500:
        num -= 500
        roman_str += 'D'
    elif num >= 400:
        num -= 400
        roman_str += 'CD'

    count2 = int(num / 100)
    for i in range(count2):
        roman_str += 'C'
    num = num % 100
    if num >= 90:
        num -= 90
        roman_str += 'XC'
    elif num >= 50:
        num -= 50
        roman_str += 'L'
    elif num >= 40:
        num -= 40
        roman_str += 'XL'

    count3 = int(num / 10)
    for i in range(count3):
        roman_str += 'X'
    num = num % 10
    if num >= 9:
        num -= 9
        roman_str += 'IX'
    elif num >= 5:
        num -= 5
        roman_str += 'V'
    elif num >= 4:
        num -= 4
        roman_str += 'IV'

    for i in range(num):
        roman_str += 'I'

    return roman_str

num1 = 3749     # MMMDCCXLIX
num2 = 1994     # MCMXCIV

print(intToRoman(num2))
