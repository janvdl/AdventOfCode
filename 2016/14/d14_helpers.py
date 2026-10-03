import hashlib

def md5(prefix, i) -> str:
    """
    generates a single md5 hash based on prefix string and number
    """
    return hashlib.md5((prefix + str(i)).encode()).hexdigest()

def md5_basic(s) -> str:
    """
    generates a single md5 hash from a given string input
    """
    return hashlib.md5((s).encode()).hexdigest()

def generate_next_hash(hashes, prefix, i, n = 1, partB = False):
    """
    generates the next n hashes starting at index i provided it does not already exist
    """
    for j in range(n):
        if (i + j) not in hashes:
            hashes[i + j] = md5(prefix, i + j)

            if partB:
                for x in range(2016):
                    hashes[i + j] = md5_basic(hashes[i + j])

def repeats(s, l):
    """
    checks for the first repeat of l-characters in string s
    """
    i = 0
    while i <= len(s) - l:
        sub = s[i:i+l]
        num = [ord(c) for c in sub]
        if max(num) == min(num):
            # all values are the same
            return True, sub[0]
        i += 1

    return False, ""

def repeat3(s):
    """
    checks for the first 3-char repeat in string s
    """
    return repeats(s, 3)