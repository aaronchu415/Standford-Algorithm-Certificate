def karatsubaMultiplication(x, y):

    if x < 10 or y < 10:
        return x * y

    # check whether n is even. If odd, set n lower by 1
    largest_n = max(len(str(x)), len(str(y)))

    if largest_n % 2 != 0:
        largest_n -= 1

    n_over_2 = int(largest_n / 2)

    a, b = divmod(x, 10**n_over_2)
    c, d = divmod(y, 10**n_over_2)

    a_and_b = a + b
    c_and_d = c + d

    ac = karatsubaMultiplication(a, c)
    bd = karatsubaMultiplication(b, d)
    product_a_b_c_d = karatsubaMultiplication(a_and_b, c_and_d) - ac - bd

    return ((ac*(10**largest_n)) + bd + ((product_a_b_c_d)*(10**n_over_2)))


def gradeSchoolMultiplication(n1, n2):
    n1, n2 = pad(n1, n2)

    o = []

    for j in range(len(n2)-1, -1, -1):
        carry_over = 0
        row = []
        for i in range(len(n1)-1, -1, -1):
            p = int(n2[j]) * int(n1[i]) + carry_over

            if p >= 10:
                carry_over = p // 10
                p = p % 10
            else:
                carry_over = 0
            row.append(p)
        if carry_over > 0:
            row.append(carry_over)
        row.reverse()

        # padd with zeros based on the position of n2
        for x in range(len(n2)-1-j):
            row.append(0)
        o.append(row)

    return sum([int(''.join([str(n) for n in nums])) for nums in o])


def pad(n1, n2):
    return n1.zfill(len(n2)), n2.zfill(len(n1))


print(gradeSchoolMultiplication(
    '3141592653589793238462643383279502884197169399375105820974944592', '2718281828459045235360287471352662497757247093699959574966967627'))

print(karatsubaMultiplication(3141592653589793238462643383279502884197169399375105820974944592,
                              2718281828459045235360287471352662497757247093699959574966967627))
