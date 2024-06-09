import argparse
import json


def generate_diff(first_file, second_file):
    result = f'\n'
    dict1 = json.load(open(first_file))
    dict2 = json.load(open(second_file))
    sum_dict = {**dict1, **dict2}
    sum_sorted_dict = dict(sorted(sum_dict.items()))
    for i in sum_sorted_dict:
        if i in dict1 and i in dict2 and dict1[i] == sum_sorted_dict[i]:
            result += f'  {i}: {sum_sorted_dict[i]}\n'
        if i in dict1 and i not in dict2:
            result += f'- {i}: {sum_sorted_dict[i]}\n'
        if i in dict1 and i in dict2 and dict1[i] != sum_sorted_dict[i]:
            result += f'- {i}: {dict1[i]}\n+ {i}: {sum_sorted_dict[i]}\n'
        if i in dict2 and i not in dict1:
            result += f'+ {i}: {sum_sorted_dict[i]}\n'
    print(result)
    return result


def main():
    parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    generate_diff(args.first_file, args.second_file)
    return



if __name__ == "__main__":
    main()
