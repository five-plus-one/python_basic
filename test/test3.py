def convert_ones(num):
    """转换个位数（1-9）"""
    ones_words = ["", "one", "two", "three", "four", "five",
                  "six", "seven", "eight", "nine"]
    return ones_words[num]


def convert_teens(num):
    """转换10-19的数字"""
    teens_words = ["ten", "eleven", "twelve", "thirteen", "fourteen",
                   "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    return teens_words[num - 10]


def convert_tens(num):
    """转换十位数（20-90）"""
    tens_words = ["", "", "twenty", "thirty", "forty", "fifty",
                  "sixty", "seventy", "eighty", "ninety"]
    return tens_words[num]


def convert_two_digits(num):
    """转换两位数（1-99）"""
    if num < 10:
        return convert_ones(num)
    elif num < 20:
        return convert_teens(num)
    else:
        tens = num // 10
        ones = num % 10
        if ones == 0:
            return convert_tens(tens)
        else:
            return f"{convert_tens(tens)} {convert_ones(ones)}"


def convert_three_digits(num):
    """转换三位数（100-999）"""
    hundreds = num // 100
    remainder = num % 100

    if remainder == 0:
        return f"{convert_ones(hundreds)} hundred"
    else:
        return f"{convert_ones(hundreds)} hundred and {convert_two_digits(remainder)}"


def number_to_words(num):
    """将1-999的数字转换为英文单词"""
    if num == 0:
        return "zero"
    elif num < 100:
        return convert_two_digits(num)
    else:
        return convert_three_digits(num)


def validate_input(user_input):
    """验证用户输入是否有效"""
    if user_input.lower() == "exit":
        return "exit"

    try:
        num = int(user_input)
        if 1 <= num <= 999:
            return num
        else:
            return None
    except ValueError:
        return None


"""主程序，处理用户输入和输出"""
print("数字转英文单词转换器")
print("输入1-999之间的整数，或输入'exit'退出程序")
print("-" * 40)

while True:
    user_input = input("请输入一个数字 (1-999): ").strip()

    # 验证输入
    result = validate_input(user_input)

    if result == "exit":
        print("程序已退出。")
        break
    elif result is None:
        print("错误：请输入1-999之间的有效整数！")
        continue
    else:
        # 转换并输出结果
        english_words = number_to_words(result)
        print(f"{result} 的英文表示是: {english_words}")

    print("-" * 40)
