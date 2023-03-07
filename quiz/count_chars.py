from typing import Tuple


def count_chars(strings: str) -> Tuple[str, int]:
    strings = strings.lower()
    d = {}
    for char in strings:
        if not char.isspace():
            d[char] = d.get(char, 0) + 1
    max_key = max(d, key=d.get)
    return max_key, d[max_key]


if __name__ == '__main__':
    l = 'This is a pen. This is an apple. Apple pen.'
    print(count_chars(l))
