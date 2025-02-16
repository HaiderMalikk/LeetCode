def mergeAlternately(self, word1: str, word2: str) -> str:
    curr = 0
    merged = ""
    while len(word1) != curr and len(word2) != curr:
        merged += word1[curr]
        merged += word2[curr]
        curr += 1
    if len(word1) == curr or len(word2) == curr:
        if len(word1) == curr and len(word2) != curr: 
            merged += word2[curr:]
        if len(word2) == curr and len(word1) != curr: 
            merged += word1[curr:]
    return merged
