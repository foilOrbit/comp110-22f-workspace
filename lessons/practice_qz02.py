"""qz02 practice."""


def odd_and_even(list_1: list[int])->list[int]:
    """Returns elements that are odd and have even index."""
    i: int = 0
    list_2: list[int] = []
    while i<len(list_1):
        if list_1[i] % 2 != 0:
            list_2.append(list_1[i])
        i += 2
    return list_2


def vowels_and_threes(input_str: str) -> str:
    """Returns vowels or consonants at an index at a multiple of 3."""
    output_str = ""
    vowels: list[int] = ["a", "e", "i", "o", "u"]
    i: int = 0
    j: int = 0
    contains: bool = False
    while i < len(input_str):
        contains = False
        j: int = 0
        while j < len(vowels):
            if input_str[i] == vowels[j]:
                contains = True
            j += 1
        if contains == True and i % 3 != 0:
            # cannot append to str
            output_str += input_str[i]
        elif contains == False and i % 3 == 0:
            output_str += input_str[i]
        i += 1
    return output_str   


def average_grades(dict_1: dict[str, list[int]]) -> dict[str, float]:
    """Returns key with average of list as value."""
    dict_2: dict[str, float] = {}
    for key in dict_1:
        avg: int = 0
        for i in dict_1[key]:
            avg += i
        avg /= len(dict_1[key])
        dict_2[key] = avg
    return dict_2


def main() -> None:
    print(odd_and_even([2, 9, 4, 17, 9, 10, 15, 13, 14, 21]))
    print(vowels_and_threes("hello world"))
    print(average_grades({"Bill": [75, 94, 97], "Annie": [88, 93, 99]}))

if __name__ == "__main__":
    main()