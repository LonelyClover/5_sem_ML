import numpy as np


def sum_non_neg_diag(X: np.ndarray) -> int:
    sqare_size = min(X.shape)
    Diag = X[np.arange(sqare_size), np.arange(sqare_size)]
    Diag_nonneg = Diag[Diag >= 0]
    
    if Diag_nonneg.size == 0:
        return -1

    return Diag_nonneg.sum()


def are_multisets_equal(x: np.ndarray, y: np.ndarray) -> bool:
    if x.size != y.size:
        return False

    return all(np.sort(x) == np.sort(y))


def max_prod_mod_3(x: np.ndarray) -> int:
    if x.size <= 1:
        return -1
        
    products = (x[1:] * x[:x.size-1])
    valid_products = products[products % 3 == 0]

    if valid_products.size == 0:
        return -1

    return valid_products.max()


def convert_image(image: np.ndarray, weights: np.ndarray) -> np.ndarray:
    weighted_image = np.multiply(image, weights)
    result_image = np.add.reduce(weighted_image, 2)
    return result_image


def rle_to_vec(x: np.ndarray) -> np.ndarray:
    #result = np.array([])
    #np.apply_along_axis(lambda pair: result = append(result, np.full(pair[1], pair[0])), 1, x)
    #print(result)
    pass

def rle_scalar(x: np.ndarray, y: np.ndarray) -> int:
    #print(x)
    #print(rle_to_vec(x))
    pass


def cosine_distance(X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    """
    Вычислить матрицу косинусных расстояний между объектами X и Y.
    В случае равенства хотя бы одно из двух векторов 0, косинусное расстояние считать равным 1.
    """
    pass
