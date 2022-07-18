from scipy import spatial
import numpy as np
from numpy.linalg import norm


if __name__ == '__main__':
    """
    Compute cosine similarity between 2 vectors.
    NOTE!!! The cosine similarity measure is invariant with respect to vector stretching and compression
    """
    a = np.array([1, -1, 1]) * 100
    b = np.array([1, 0, -2]) * 50

    # 1-st way to calculate cosine similarity
    # Note that spatial.distance.cosine computes the distance, and not the similarity.
    # So, you must subtract the value from 1 to get the similarity.
    cos_similarity = 1 - spatial.distance.cosine(a, b)
    print(f'1-st way to calculate cos_similarity: {cos_similarity}')

    # 2-nd way to calculate cosine similarity
    cos_similarity = (a @ b) / (norm(a) * norm(b))
    print(f'2-nd way to calculate cos_similarity: {cos_similarity}')



