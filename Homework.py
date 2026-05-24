def reverse_bits(n):
    result = 0
    for i in range(32):
        result <<= 1
        result |= (n & 1)
        n >>= 1
    return result

num = 43261596
reversed_num = reverse_bits(num)

print(f"Original Number: {num}")
print(f"Newly Formed Number: {reversed_num}")