import numpy as np

first_cnt = np.array([1.61, 1.42, 3.45, 9.19])
st_ms = np.array([1.61, 1.42, 3.45, 1.42, 1.61, 1.42, 3.45, 9.19, 1.65, 1.61, 10.67, 1.76, 1.27, 1.00, 1.00, 1.46, 1.54, 1.12, 5.65])

def found_index(self, first_cnt, st_ms):
    window_size = len(first_cnt)
    is_subset = False
    found_indices = []

    for i in range(len(st_ms) - window_size + 1):
        window = st_ms[i:i+window_size]
        if np.array_equal(window, first_cnt):
            is_subset = True
            found_indices = list(range(i, i+window_size))
            break

    print(found_indices)

