

# 这道题目相当于实现一个高精度除法
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)
        s = ""
        # 计算符号
        if numerator * denominator < 0:
            s += "-"
        # 取绝对值，计算整数部分
        integer_part = abs(numerator) // abs(denominator)
        s += str(integer_part)
        s += "."
        # 模拟除法，计算小数部分
        fraction_part = ""
        remainder_index_map = dict()
        # 余数
        remainder = abs(numerator) % abs(denominator)
        index = 0
        while remainder != 0 and remainder not in remainder_index_map:
            remainder_index_map[remainder] = index
            remainder *= 10
            fraction_part += str(remainder // abs(denominator))
            remainder = remainder % abs(denominator)
            index += 1
        if remainder != 0:
            insert_index = remainder_index_map.get(remainder)
            # 字符串的insert_index位置插入"("
            fraction_part_list = list(fraction_part)
            fraction_part_list.insert(insert_index, "(")
            fraction_part = "".join(fraction_part_list)
            fraction_part += ")"

        s += fraction_part
        return s





if __name__ == '__main__':
    print(Solution().fractionToDecimal(2, 1))