import pandas as pd
import statistics

class PERMA:

    def __init__(self) -> None:
        pass

    def getLexMinMax(cat):
        PERMA_lex = pd.read_csv('FTER/permaV3_dd.csv')
        # print(PERMA_lex)

        PERMA_cat = list()
        PERMA_scores = list()

        for index, row in PERMA_lex.iterrows():
            if row['category'] == cat:
                PERMA_cat.append(row)
                PERMA_scores.append(row['weight'])

        lexMin = 0
        lexMax = 0

        for i in PERMA_cat:
            if i['weight'] < lexMin:
                lexMin = i['weight']

        for i in PERMA_cat:
            if i['weight'] > lexMax:
                lexMax = i['weight']

        print(lexMin)
        print(lexMax)

        # Mean
        mean = statistics.mean(PERMA_scores)
        print("Mean: ", mean)

        # STD
        std = statistics.stdev(PERMA_scores)
        print("STD: ", std)



    if __name__ == "__main__":
        # output min & max per category
        cats = ['POS_P', 'POS_E', 'POS_R', 'POS_M', 'POS_A', 'NEG_P', 'NEG_E', 'NEG_R', 'NEG_M', 'NEG_A']
        for i in cats:
            print(i)
            getLexMinMax(i)