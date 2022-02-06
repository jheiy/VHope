import random

for x in range(5):
    positive_scores = random.randint(0,9)
    negative_scores = random.randint(0,9)

    print("POS: " + str(positive_scores) + " NEG: " + str(negative_scores))

    if positive_scores >= 7 or negative_scores <= 1.9:
        print("SPECTRUM: EXCELLING")
    elif positive_scores >= 6 or negative_scores <= 2:
        print("SPECTRUM: THRIVING")
    elif positive_scores >= 4.5 or negative_scores <= 3:
        print("SPECTRUM: SURVIVING")
    elif positive_scores >= 3 or negative_scores <= 4:
        print("SPECTRUM: STRUGGLING")
    elif positive_scores < 3 or negative_scores > 5:
        print("SPECTRUM: IN CRISIS")