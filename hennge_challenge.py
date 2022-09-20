import sys

def filter_and_square(num):
    num = int(num)
    if (num > 0):
        return num * num

def separate_testcases_and_calculate(input_list, count, testcase_amount, i, results_list):
    testcase_list = (input_list[i + 1]).split()
    i += 2
    count += 1
    results_list.append(sum(filter(None, map(filter_and_square, testcase_list))))
    if (count <= testcase_amount):
        separate_testcases_and_calculate(input_list, count, testcase_amount, i, results_list)


def main():
    input_list = sys.stdin.read().splitlines()
    testcase_amount = int(input_list[0])
    results_list = []
    count = 1
    i = 1
    separate_testcases_and_calculate(input_list, count, testcase_amount, i, results_list)
    print(*results_list, sep = "\n")


if __name__ == "__main__":
    main()