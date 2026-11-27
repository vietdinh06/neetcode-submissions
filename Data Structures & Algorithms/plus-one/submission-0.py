class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0

        digits[len(digits)-1] += 1

        for digit in range(len(digits) - 1, -1, -1):
            new_dig = digits[digit] + carry
            print(str(digits[digit]) + ":" + str(new_dig))

            if new_dig == 10:
                new_dig = 0
                carry = 1
            else:
                carry = 0

            digits[digit] = new_dig

        if carry:
            digits.insert(0, 1)

        return digits

    # [1, 2, 3, 4] always add the last digit

    # but, if the digit is 0, we will have to go to the next (-1) digit

    # since we're only adding 1, the only time we have to do a carry is if the current digit is 9, and even then we are only doing a carry of 1 for the next digits that are 9.

    # so, lets loop through the digits backwards. if the number is 9, set that digit to 0, and we will add the carry of 1 to the next digit. otherise, we will have the carry simply be 0 and it will go through the entire list as if no caryr happened.
    # there is the case at the end where we will have to add a new digit if the last digit was a 9. so jsut check if a digit exists