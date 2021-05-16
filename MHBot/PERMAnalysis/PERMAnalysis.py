import csv, enchant, nltk
from Unigram import unigram
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from numpy import array
import numpy as np
from scipy.stats import skew
# nltk.download('punkt')

sample_text = "I always loved watching movies with my friends and family then one day we got into a party and celebrated my brothers birthday and it was the happiest day of my life"

senti_dict = { 'POS_P' : {'min': 0, 'max': 0, 'score': 0, 'ctr': 0, 'score_list': []},
               'POS_E' : {'min': 0, 'max': 0, 'score': 0, 'ctr': 0, 'score_list': []},
               'POS_R' : {'min': 0, 'max': 0, 'score': 0, 'ctr': 0, 'score_list': []},
               'POS_M' : {'min': 0, 'max': 0, 'score': 0, 'ctr': 0, 'score_list': []},
               'POS_A' : {'min': 0, 'max': 0, 'score': 0, 'ctr': 0, 'score_list': []},
               'NEG_P' : {'min': 0, 'max': 0, 'score': 0, 'ctr': 0, 'score_list': []},
               'NEG_E' : {'min': 0, 'max': 0, 'score': 0, 'ctr': 0, 'score_list': []},
               'NEG_R' : {'min': 0, 'max': 0, 'score': 0, 'ctr': 0, 'score_list': []},
               'NEG_M' : {'min': 0, 'max': 0, 'score': 0, 'ctr': 0, 'score_list': []},
               'NEG_A' : {'min': 0, 'max': 0, 'score': 0, 'ctr': 0, 'score_list': []}}

POS_P = []

class PERMAnalysis: 
    def __init__(self):
        self.p = 0.0
        self.e = 0.0
        self.r = 0.0
        self.m = 0.0
        self.a = 0.0
    
    def readLex(self, input_text):
        global senti_dict
        global POS_P
        global sample_text
        
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
                    # if row[1] == 'POS_P':
                    #     # POS_P.append(float(row[2]))
                    #     pos_p += 1
                    # elif row[1] == 'POS_E':
                    #     pos_e += 1
                    # elif row[1] == 'POS_R':
                    #     pos_r += 1
                    # elif row[1] == 'POS_M':
                    #     pos_m += 1
                    # elif row[1] == 'POS_A':
                    #     pos_a += 1
                    # elif row[1] == 'NEG_P':
                    #     neg_p += 1
                    # elif row[1] == 'NEG_E':
                    #     neg_e += 1
                    # elif row[1] == 'NEG_R':
                    #     neg_r += 1
                    # elif row[1] == 'NEG_M':
                    #     neg_m += 1
                    # elif row[1] == 'NEG_A':
                    #     neg_a += 1
    
        for row in nrc_reader:
            if row[4] != '-' and row[4] != 'perma_score':
                unigrams.append(unigram(row))
                senti_dict[row[3]]['score_list'].append(float(row[4]))
                
        # print(pos_p)
        # print(pos_e)
        # print(pos_r)
        # print(pos_m)
        # print(pos_a)
        # print(neg_p)
        # print(neg_e)
        # print(neg_r)
        # print(neg_m)
        # print(neg_a)
        # print(unigrams.__len__())
                
            
        
        
        words = word_tokenize(sample_text)
        # print(words)
        for term in unigrams:
            for token in words:
                if token == term.text:
                    senti_dict[term.label]['score'] += float(term.score)
                    senti_dict[term.label]['ctr'] += 1
            
        
        # print(senti_dict['NEG_A']['score'] / senti_dict['NEG_A']['ctr'])           
        # print(((senti_dict['NEG_A']['score'] / senti_dict['NEG_A']['ctr']) - senti_dict['NEG_A']['min'] * 100) / (senti_dict['NEG_A']['max'] - senti_dict['NEG_A']['min']))
        
        
        
        
        
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
            print(key)
            print(senti_dict[key]['score'] / senti_dict[key]['ctr'])     
            print((((senti_dict[key]['score'] / senti_dict[key]['ctr'])   - senti_dict[key]['min']) * 100) / (senti_dict[key]['max'] - senti_dict[key]['min']))
            
        
        
if __name__ == "__main__":
    PERMAnalysis().readLex()
    for key in senti_dict:
        gn=array(senti_dict[key]['score_list'])
        plt.hist(gn.astype('float'))
        plt.show()
    