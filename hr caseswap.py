def swap_case(s):
    ans = ""
    for char in s:
        if isinstance(char, str):
            if char == char.upper():
                char = char.lower()
                ans += char
            elif char == char.lower():
                char = char.upper()
                ans += char
        else:
            ans += char
    return ans


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)