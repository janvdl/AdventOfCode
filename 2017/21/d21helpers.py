def calculateSplitCount(pattern: str) -> int:
    pattern_rows = len(pattern.split('/'))
    if pattern_rows % 2 == 0:
        return 2
    else:
        return 3