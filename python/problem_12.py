class Solution:
    def intToRoman(self, num: int) -> str:
        n = 0
        num_roman = ''

        while num > 0:
            n += 1
            num, tmp = num // 10, num % 10
            
            # Ones digit
            if n == 1:
                if tmp == 0:
                    continue
                elif tmp <= 3:
                    num_roman += 'I' * tmp
                elif tmp == 4:
                    num_roman = 'IV'
                elif tmp <= 8:
                    num_roman = 'V' + 'I' * (tmp-5)
                else:
                    num_roman = 'IX'
            
            # Ten digit
            elif n == 2:
                if tmp == 0:
                    continue
                elif tmp <= 3:
                    num_roman = 'X' * tmp + num_roman
                elif tmp == 4:
                    num_roman = 'XL' + num_roman
                elif tmp <= 8:
                    num_roman = 'L' + 'X' * (tmp-5) + num_roman
                else:
                    num_roman = 'XC' + num_roman

            # Hundreds digit
            elif n == 3:
                if tmp == 0:
                    continue
                elif tmp <= 3:
                    num_roman = 'C' * tmp + num_roman
                elif tmp == 4:
                    num_roman = 'CD' + num_roman
                elif tmp <= 8:
                    num_roman = 'D' + 'C' * (tmp - 5) + num_roman
                else:
                    num_roman = 'CM' + num_roman

            elif n == 4:
                num_roman = 'M' * tmp + num_roman

            # For debugging
            # print('roman: {}\tnum: {}\ttmp: {}\tn: {}'.format(num_roman,num,tmp,n))

        return num_roman