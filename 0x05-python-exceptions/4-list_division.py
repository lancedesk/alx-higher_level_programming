#!/usr/bin/python3

# Check if is valid type -> is_valid_type
def i_v_t(value):
    return isinstance(value, (int, float))


def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            # Try to divide elements from the lists
            quotient = my_list_1[i] / my_list_2[i]
        except IndexError:
            # Handle out of range error
            print("out of range")
            quotient = 0
        except (ZeroDivisionError, TypeError):
            # Handle division by 0 or wrong type error
            if i_v_t(my_list_1[i]) and i_v_t(my_list_2[i]):
                print("division by 0")
            else:
                print("wrong type")
            quotient = 0
        finally:
            # Append the quotient to the result list
            result.append(quotient)
    return (result)
