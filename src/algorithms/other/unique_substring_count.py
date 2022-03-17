from src.data_structures.lcp_array import LCP


def unique_substring_count(value: str):
    str_len = len(value)
    lcp = LCP(value)
    num_substr = (str_len * (str_len + 1)) // 2
    duplicate_count = sum([lcp[i] for i in range(1, str_len, 1)])
    return num_substr - duplicate_count
