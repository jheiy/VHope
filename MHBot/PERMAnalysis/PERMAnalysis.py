import csv, enchant, nltk
from MHBot.PERMAnalysis.Unigram import unigram
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from numpy import array
import numpy as np
from scipy.stats import skew
from src import Logger, EVENT_ACTION
# nltk.download('punkt')

sample_text = "I always loved watching movies with my friends and family then one day we got into a party and celebrated my brothers birthday and it was the happiest day of my life"

POS_P = []
pos_labels = {}

class PERMAnalysis: 
    def __init__(self):
        self.senti_dict = { 'POS_P' : {'min': 0, 'max': 0, 'score': 0, 'ctr': 0, 'score_list': []},
               'POS_E' : {'min': 0, 'max': 0, 'score': 0, 'ctr': 0, 'score_list': []},
               'POS_R' : {'min': 0, 'max': 0, 'score': 0, 'ctr': 0, 'score_list': []},
               'POS_M' : {'min': 0, 'max': 0, 'score': 0, 'ctr': 0, 'score_list': []},
               'POS_A' : {'min': 0, 'max': 0, 'score': 0, 'ctr': 0, 'score_list': []},
               'NEG_P' : {'min': 0, 'max': 0, 'score': 0, 'ctr': 0, 'score_list': []},
               'NEG_E' : {'min': 0, 'max': 0, 'score': 0, 'ctr': 0, 'score_list': []},
               'NEG_R' : {'min': 0, 'max': 0, 'score': 0, 'ctr': 0, 'score_list': []},
               'NEG_M' : {'min': 0, 'max': 0, 'score': 0, 'ctr': 0, 'score_list': []},
               'NEG_A' : {'min': 0, 'max': 0, 'score': 0, 'ctr': 0, 'score_list': []}}
    
    def readLex(self, input_text):
        senti_dict = self.senti_dict
        global POS_P
        global sample_text
        global pos_labels
        
        sample_text = input_text
        
        bad_chars = [';', ':', '!', '*', '.', ',']
        d = enchant.Dict("en_US")
        lex = open("permaV3_dd.csv", 'rt', encoding='utf-8')
        nrc_lex = open("nrc_perma_lexicon.csv", 'rt', encoding='utf-8')
        reader = csv.reader(lex)
        nrc_reader = csv.reader(nrc_lex)
        pos_p = pos_e = pos_r = pos_m = pos_a = neg_p = neg_e = neg_r = neg_m = neg_a = 0
        unigrams = []
        
        for row in reader:
            # row[0] = ''.join((filter(lambda i: i not in bad_chars, row[0]))).strip()
            if row[0] and row[1] != 'category':
                if d.check(row[0]):
                    # wr.writerow(row)
                    # print(row)
                    unigrams.append(unigram(row))
                    senti_dict[row[1]]['score_list'].append(float(row[2]))

        for row in nrc_reader:
            if row[4] != '-' and row[4] != 'perma_score' and row[1] != '':
                unigrams.append(unigram(row))
                senti_dict[row[3]]['score_list'].append(float(row[4]))
        
        words = word_tokenize(sample_text)
        # print(words)
        for term in unigrams:
            for token in words:
                if token == term.text:
                    senti_dict[term.label]['score'] += float(term.score)
                    senti_dict[term.label]['ctr'] += 1
            
        positive_scores = 0
        negative_scores = 0
        
        for key in senti_dict:
            temp_arr = array(senti_dict[key]['score_list'])
            std = np.std(temp_arr)
            mean = np.mean(temp_arr)
            distance_from_mean = abs(temp_arr - mean)
            max_deviations = 1.25
            not_outlier = distance_from_mean < max_deviations * std
            senti_dict[key]['score_list'] = temp_arr[not_outlier]
            
            senti_dict[key]['min'] = min(senti_dict[key]['score_list'])
            senti_dict[key]['max'] = max(senti_dict[key]['score_list'])
            # print(senti_dict[key]['min'])
            # print(senti_dict[key]['max'])
            average_score = 0
            percentage_score = 0
            if senti_dict[key]['ctr'] != 0:
                average_score = senti_dict[key]['score'] / senti_dict[key]['ctr']
                percentage_score = ((average_score - senti_dict[key]['min']) * 10) / (senti_dict[key]['max'] - senti_dict[key]['min'])
            # print(key)
            # print(senti_dict[key]['score'] / senti_dict[key]['ctr'])     
            # print((((senti_dict[key]['score'] / senti_dict[key]['ctr'])   - senti_dict[key]['min']) * 100) / (senti_dict[key]['max'] - senti_dict[key]['min']))
            if 'POS' in key:
                pos_labels[key] = percentage_score
                positive_scores = percentage_score + positive_scores
            elif 'NEG' in key:
                negative_scores = percentage_score + negative_scores
        positive_scores = positive_scores / 5
        negative_scores = negative_scores / 5
        
        Logger.log_perma_values_input(input_text)
        Logger.log_perma_scores("Positive Scores: " + str(positive_scores) + " & " + "Negative Scores: " + str(negative_scores))
        if positive_scores >= 8 or negative_scores <= 3:
            Logger.log_perma_scores("SPECTRUM: OPTIMAL")
            return 'green'
        elif positive_scores >= 5 or negative_scores <= 6.5:
            Logger.log_perma_scores("SPECTRUM: EMERGING")
            return 'orange'
        elif positive_scores < 5 or negative_scores > 6.5:
            Logger.log_perma_scores("SPECTRUM: AT RISK")
            return 'red'
    
    def get_lowest_score(self):
        return min(pos_labels, key=pos_labels.get)
    
    def isComplete(self):
        senti_dict = self.senti_dict
        flag = True
        
        for key in senti_dict:
            if senti_dict[key]['score'] == 0:
                flag = False
        print("BOWCHIKAWAWABOOM")

        Logger.log_perma_values_input(sample_text)
        Logger.log_perma_scores("CHECK IS PERMA COMPLETE: " + str(flag))
        Logger.log_perma_scores('POS_P: ' + str(self.senti_dict['POS_P']['score']))
        Logger.log_perma_scores('POS_E: ' + str(self.senti_dict['POS_E']['score']))
        Logger.log_perma_scores('POS_R: ' + str(self.senti_dict['POS_R']['score']))
        Logger.log_perma_scores('POS_M: ' + str(self.senti_dict['POS_M']['score']))
        Logger.log_perma_scores('POS_A: ' + str(self.senti_dict['POS_A']['score']))
        Logger.log_perma_scores('NEG_P: ' + str(self.senti_dict['NEG_P']['score']))
        Logger.log_perma_scores('NEG_E: ' + str(self.senti_dict['NEG_E']['score']))
        Logger.log_perma_scores('NEG_R: ' + str(self.senti_dict['NEG_R']['score']))
        Logger.log_perma_scores('NEG_M: ' + str(self.senti_dict['NEG_M']['score']))
        Logger.log_perma_scores('NEG_A: ' + str(self.senti_dict['NEG_A']['score']))


        return flag
        
    def reset(self):
        
        self.senti_dict = { 'POS_P' : {'min': 0, 'max': 0, 'score': 0, 'ctr': 0, 'score_list': []},
               'POS_E' : {'min': 0, 'max': 0, 'score': 0, 'ctr': 0, 'score_list': []},
               'POS_R' : {'min': 0, 'max': 0, 'score': 0, 'ctr': 0, 'score_list': []},
               'POS_M' : {'min': 0, 'max': 0, 'score': 0, 'ctr': 0, 'score_list': []},
               'POS_A' : {'min': 0, 'max': 0, 'score': 0, 'ctr': 0, 'score_list': []},
               'NEG_P' : {'min': 0, 'max': 0, 'score': 0, 'ctr': 0, 'score_list': []},
               'NEG_E' : {'min': 0, 'max': 0, 'score': 0, 'ctr': 0, 'score_list': []},
               'NEG_R' : {'min': 0, 'max': 0, 'score': 0, 'ctr': 0, 'score_list': []},
               'NEG_M' : {'min': 0, 'max': 0, 'score': 0, 'ctr': 0, 'score_list': []},
               'NEG_A' : {'min': 0, 'max': 0, 'score': 0, 'ctr': 0, 'score_list': []}}

        
        
# if __name__ == "__main__":
#     PERMAnalysis().readLex()
#     for key in senti_dict:
#         gn=array(senti_dict[key]['score_list'])
#         plt.hist(gn.astype('float'))
#         plt.show()
    