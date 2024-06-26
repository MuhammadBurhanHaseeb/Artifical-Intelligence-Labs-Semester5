matchScore = 1
misMatchScore = -1
gapPenalty = -2

def editDistance(s1, s2):
    n = len(s1)
    m = len(s2)
    
    # Initialize the memoization matrix
    memo = [[0] * (m + 1) for _ in range(n + 1)]

    # Initialize the memoization matrix for traceback
    traceback = [[None] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0:
                memo[i][j] = j * gapPenalty
            elif j == 0:
                memo[i][j] = i * gapPenalty
            else:
                match = memo[i - 1][j - 1] + (matchScore if s1[i - 1] == s2[j - 1] else misMatchScore)
                gapS1 = memo[i][j - 1] + gapPenalty
                gapS2 = memo[i - 1][j] + gapPenalty
                maxScore = max(match, gapS1, gapS2)
                memo[i][j] = maxScore

                # Record the traceback direction
                if maxScore == match:
                    traceback[i][j] = 'diagonal'
                elif maxScore == gapS1:
                    traceback[i][j] = 'left'
                else:
                    traceback[i][j] = 'up'

    # Backtrack to find the aligned sequences
    alignedS1 = []
    alignedS2 = []
    i, j = n, m
    while i > 0 or j > 0:
        if traceback[i][j] == 'diagonal':
            alignedS1.append(s1[i - 1])
            alignedS2.append(s2[j - 1])
            i -= 1
            j -= 1
        elif traceback[i][j] == 'left':
            alignedS1.append('-')
            alignedS2.append(s2[j - 1])
            j -= 1
        else:
            alignedS1.append(s1[i - 1])
            alignedS2.append('-')
            i -= 1

    alignedS1 = ''.join(reversed(alignedS1))
    alignedS2 = ''.join(reversed(alignedS2))

    return memo[n][m], alignedS1, alignedS2

sequence1 = "AAGC"
sequence2 = "AGT"
alignmentScore, aligned_seq1, aligned_seq2 = editDistance(sequence1, sequence2)
print("Alignment Score:", alignmentScore)
print("Aligned Sequence 1:", aligned_seq1)
print("Aligned Sequence 2:", aligned_seq2)
