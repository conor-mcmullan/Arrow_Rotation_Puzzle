

def most_common_arrow(arrow_string):
    frequencies = [(arrow_char, arrow_string.count(arrow_char)) for arrow_char in set(arrow_string)]
    return max(frequencies, key=lambda x: x[1])[0]

def arrow_rotation(arrow_string):
    desired_arrow = most_common_arrow(arrow_string)
    print(f"Most Common Arrow:\t{desired_arrow}")
    desired_arrow_string = ""
    arrow_counter = 0
    for arrow in arrow_string:
        new_arrow, moves = rotate_and_count(arrow, desired_arrow)
        desired_arrow_string += new_arrow
        arrow_counter += moves
    print(f"Final Rotated String:\t{desired_arrow_string}")
    print(f"Total (90 Degree) Arrow Rotation:\t{arrow_counter}")


def rotate_and_count(arrow, desired_arrow):
    
    moves = 0
    #while arrow != desired_arrow:
    # tabbed in code not using the while 
    if arrow!=desired_arrow:
        if arrow in ["^", "v"]:
            arrow = desired_arrow
            if desired_arrow in ["<", ">"]:
                moves += 1
            else:
                # if v to ^ or v to ^ is the same so 2
                moves += 2

    if arrow!=desired_arrow:
        if arrow in ["<", ">"]:
            arrow = desired_arrow
            if desired_arrow in ["^", "v"]:
                moves += 1
            else:
                # if < to > or > to < is the same so 2
                moves += 2

    return arrow, moves


def minimum_arrows_to_rotate(arrow_string):
    # gets the most common arrow then counts the characters that are not that character for the answer
    desired_arrow = most_common_arrow(arrow_string)
    min_to_rotate = len([c for c in arrow_string if c != desired_arrow])
    print(f"Minimum Rotation:\t{min_to_rotate}")

if __name__ == "__main__":
    
    test_string_one = "^vv<v"
    print(f"\nTest String One:\t{test_string_one}")
    arrow_rotation(test_string_one)
    minimum_arrows_to_rotate(test_string_one)

    test_string_two = "v>>>vv"
    print(f"\nTest String Two:\t{test_string_two}")
    arrow_rotation(test_string_two)
    minimum_arrows_to_rotate(test_string_two)

    test_string_three = "<<<"
    print(f"\nTest String Three:\t{test_string_three}")
    arrow_rotation(test_string_three)
    minimum_arrows_to_rotate(test_string_three)
