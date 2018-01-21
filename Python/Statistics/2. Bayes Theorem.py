# Cancer Example
# P(C) = P0
# P(Pos/C) = P1
# P(Neg/7C) = P2

# Give the Probability for test be Positive of Cancer P(C/Pos)


def f(P0, P1, P2):
    return P0 * P1 / (P0 * P1 + (1 - P0) * (1 - P2))


print(f(0.1, 0.9, 0.8))


# Give the Probability for test be Negative of Cancer P(C / Neg)


def nf(P0, P1, P2):
    return P0 * (1 - P1) / (P0 * (1 - P1) + (1 - P0) * P2)


print(nf(0.1, 0.9, 0.8))
