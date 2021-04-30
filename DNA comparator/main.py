import numpy as np

def GET_SCORE(n1, n2, penalty=-1, reward=1):

    if n1 == n2:
        return reward
    else:
        return penalty

def global_alignment(X, Y, penalty=-1, reward=1):

    score_matrix = np.ndarray((len(X) + 1, len(Y) + 1))

    for i in range(len(X) + 1):
        score_matrix[i, 0] = penalty * i

    for j in range(len(Y) + 1):
        score_matrix[0, j] = penalty * j

    for i in range(1, len(X) + 1):
        for j in range(1, len(Y) + 1):
            match = score_matrix[i - 1, j - 1] + \
                GET_SCORE(X[i - 1], Y[j - 1], penalty, reward)
            delete = score_matrix[i - 1, j] + penalty
            insert = score_matrix[i, j - 1] + penalty

            score_matrix[i, j] = max([match, delete, insert])

    i = len(X)
    j = len(Y)

    updated_dna1 = ""
    updated_dna2 = ""

    while i > 0 or j > 0:

        current_score = score_matrix[i, j]
        left_score = score_matrix[i - 1, j]

        if i > 0 and j > 0 and X[i - 1] == Y[j - 1]:
            updated_dna1 = X[i - 1] + updated_dna1
            updated_dna2 = Y[j - 1] + updated_dna2
            i = i - 1
            j = j - 1

        elif i > 0 and current_score == left_score + penalty:
            updated_dna1 = X[i - 1] + updated_dna1
            updated_dna2 = "|" + updated_dna2
            i = i - 1

        else:
            updated_dna1 = "|" + updated_dna1
            updated_dna2 = Y[j - 1] + updated_dna2
            j = j - 1

    return updated_dna1, updated_dna2

if __name__ == "__main__":
    X = str(input("enter your 1st dna sequence: "))
    Y = str(input("enter your 2nd dna sequence: "))
    dna_align = list(global_alignment(X, Y))
    for index, element in enumerate(dna_align[0]):
        print(f"{dna_align[0][index]}----{dna_align[1][index]}")
    j = 0
    score = 0
    flag = True
    while flag :
        score += GET_SCORE(dna_align[0][j],dna_align[1][j])
        if j>=(len(dna_align[0])-1):
            flag = False
        else:
            j+=1
    print(f"\nbest score of your sequence :\t{score}")
    