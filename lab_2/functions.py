from typing import List


def sum_non_neg_diag(X: List[List[int]]) -> int:
    n = 0
    flag = False

    for i, row in enumerate(X):
        for j, value in enumerate(row):
            if i == j and value >= 0:
                n += value
                flag = True

    if (not flag):
        return -1
    return n


def are_multisets_equal(x: List[int], y: List[int]) -> bool:
    x.sort()
    y.sort()
    return x == y


def max_prod_mod_3(x: List[int]) -> int:
    if len(x) <= 1:
        return -1

    m = x[0] * x[1]
    flag = False

    for i in range(len(x) - 1):
        if (x[i] % 3 == 0 or x[i+1] % 3 == 0) and x[i] * x[i+1] >= m:
            m = x[i] * x[i+1]
            flag = True
    
    if (not flag):
        return -1

    return m


def convert_image(image: List[List[List[float]]], weights: List[float]) -> List[List[float]]:
    result = []

    for height, image_slice in enumerate(image):
        result.append([])
        for width, values in enumerate(image_slice):
            result[height].append(0)
            for value, weight in zip(values, weights):
                result[height][width] += value * weight

    return result


def rle_to_vec(rle: List[List[int]]) -> List[int]:
    result = []

    for pair in rle:
        for i in range(pair[1]):
            result.append(pair[0])

    return result


def product(u: List[float], v: List[float]) -> float:
    result = 0;

    if len(u) != len(v):
        return -1 

    for u_i, v_i in zip(u, v):
        result += u_i * v_i

    return result


def rle_scalar(x: List[List[int]], y:  List[List[int]]) -> int:
    x = rle_to_vec(x)
    y = rle_to_vec(y)
    return product(x, y)


def metric(X: List[float]) -> float:
    result = 0;

    for x_i in X:
        result += x_i ** 2

    return result ** 0.5


def cos(u: List[float], v: List[float]) -> float:
    result = 0;

    u_m = metric(u)
    v_m = metric(v)
    p = product(u, v)

    if u_m == 0 or v_m == 0:
        return 1

    return p / (u_m * v_m)


def cosine_distance(X: List[List[float]], Y: List[List[float]]) -> List[List[float]]:
    result = []

    for i, x in enumerate(X):
        result.append([])
        for y in Y:
            result[i].append(cos(x, y))

    return result
