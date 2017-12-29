# coding=utf-8
"""
设计手的射了n靶后，得到的总分是m，收集所有分数组合的可能性
"""

def shooting_target(m, n, score_range):
    print("m {}, n {}, score_range {}".format(m, n, score_range))
    combinations = []

    if m == 0:
        return [[]]
    if m > 0 and n == 0:
        return None
    if m < 0:
        return None

    for score in range(score_range, 0, -1):
        num_score = 1

        while num_score <= n and num_score * score <= m:
            fix_set = [score] * num_score
            other_shooting_results = shooting_target(m - num_score * score, n - num_score, score-1)
            num_score += 1
            # trim
            if other_shooting_results is None:
                continue
            for sub_combination in other_shooting_results:
                combinations.append(fix_set + sub_combination)
            # print("as score {} with Num {}".format(score, num_score))
            # print("combinations {}".format(combinations))

    return combinations


if __name__ == '__main__':
    print(shooting_target(35, 5, 10))