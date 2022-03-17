class SuffixArray:
    def __init__(self, value: str):
        suffixes = [value[i:] for i in range(len(value))]
        sorted_suffixes = sorted(suffixes)
        arg_suffix = [suffixes.index(suffix) for suffix in sorted_suffixes]
        self.suffix_array = arg_suffix
        self.value = value
