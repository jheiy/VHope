"""
FROM EREN:
Original NRC Emotion lexicon: http://sentiment.nrc.ca/lexicons-for-research/
Supporting research: https://www.researchgate.net/publication/331256216_Using_sentiment_analysis_to_detect_affect_in_children's_and_adolescents'_poetry

ADDITIONAL FOR MHBOT:
Perma Lexicon: http://www.wwbp.org/lexica.html
Supporting research: http://wwbp.org/papers/2016_predicting_wellbeing.pdf
"""

#ORIG FILE CAN BE SEEN IN: http://sentiment.nrc.ca/lexicons-for-research/

import csv

def write_data(tabs):
    print("writing")
    with open('nrc_perma_lexicon.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(tabs)
    csvFile.close()

def read_data():
    path = 'C:\\Users\\Acer\\Documents\\GitHub\\MHBot\\EDEN\\NRC_emotion\\NRC-Emotion-Lexicon-Senselevel-v0.92.txt'
    days_file = open(path, 'r')
    contents = days_file.read()

    splitted = contents.split('\n')

    print("splitted: ")
    print(contents)

    del splitted[-1]

    Y = []
    for X in splitted:
        parsed = X.split('--')
        Y.append(parsed)

    tabs = []
    for X in Y:
        curr = []
        curr.append(X[0])

        curr_result_tabs = X[1].split('\t')

        curr.append(curr_result_tabs[1])
        curr.append(int(curr_result_tabs[2]))

        curr_result_comma = curr_result_tabs[0].split(', ')

        for i in curr_result_comma:
            curr.append(i)

        tabs.append(curr)

    return tabs

def format_data(retrieved_data):
    new_format = []
    new_format.append(['term', 'fear', 'anger', 'anticip', 'trust', 'surprise', 'positive', 'negative', 'sadness', 'disgust', 'joy', 'synonym_1', 'synonym_2', 'synonym_3'])
    curr_row = []
    curr_row.append(retrieved_data[0][0])
    for i in range(len(retrieved_data)):
        if i%10 == 0 and not i==0:
            for j in range (3, len(retrieved_data[i-1])):
                curr_row.append(retrieved_data[i-1][j])

            new_format.append(curr_row)
            curr_row = []
            curr_row.append(retrieved_data[i][0])
        curr_row.append(retrieved_data[i][2])

    return new_format


def read_perma(term, word_count):
    with  open('C:\\Users\\Acer\\Documents\\GitHub\\MHBot\\MHBot\\NRC_Perma_Lexicon\\permaV3_dd.csv', 'r', encoding='utf-8') as perma_file:
        perma_reader = csv.reader(perma_file)
        perma_term_got = []
        for perma_row in perma_file:
            # list_perma = perma_row.split(',')
            # print("Perma " + perma_row)
            x = perma_row.split(",")
            if (x[0].lower().strip() != "term"):
                if len(term) == 14:
                    if(x[0].lower().strip() == str(term[0]).lower().strip()):
                    # print("NRC: " + term[0] + " PERMA: " + x[0] + " CATEGORY: " + x[1] + " ID: " + str(word_count))
                    # perma_term_got = []
                        perma_term_got.append([word_count, term[0], x[0], x[1], x[2]])
                    elif (x[0].lower().strip() == str(term[11]).lower().strip()):  #Synonym 1
                        # if(x[0].lower().strip() == str(term[11]).lower().strip()):
                        # print("NRC: " + term[0] + " PERMA: " + x[0] + " CATEGORY: " + x[1] + " ID: " + str(word_count))
                        perma_term_got.append([word_count, term[0], x[0], x[1], x[2]])
                    elif (x[0].lower().strip() == str(term[12]).lower().strip()):  #Synonym 2
                        perma_term_got.append([word_count, term[0], x[0], x[1], x[2]]) 
                    elif (x[0].lower().strip() == str(term[13]).lower().strip()):  #Synonym 3
                        perma_term_got.append([word_count, term[0], x[0], x[1], x[2]])
                elif len(term) == 13:
                    if(x[0].lower().strip() == str(term[0]).lower().strip()):
                    # print("NRC: " + term[0] + " PERMA: " + x[0] + " CATEGORY: " + x[1] + " ID: " + str(word_count))
                    # perma_term_got = []
                        perma_term_got.append([word_count, term[0], x[0], x[1], x[2]])
                    elif (x[0].lower().strip() == str(term[11]).lower().strip()):  #Synonym 1
                        # if(x[0].lower().strip() == str(term[11]).lower().strip()):
                        # print("NRC: " + term[0] + " PERMA: " + x[0] + " CATEGORY: " + x[1] + " ID: " + str(word_count))
                        perma_term_got.append([word_count, term[0], x[0], x[1], x[2]])
                    elif (x[0].lower().strip() == str(term[12]).lower().strip()):  #Synonym 2
                        perma_term_got.append([word_count, term[0], x[0], x[1], x[2]])
                elif len(term) == 12:
                    if(x[0].lower().strip() == str(term[0]).lower().strip()):
                    # print("NRC: " + term[0] + " PERMA: " + x[0] + " CATEGORY: " + x[1] + " ID: " + str(word_count))
                    # perma_term_got = []
                        perma_term_got.append([word_count, term[0], x[0], x[1], x[2]])
                    elif (x[0].lower().strip() == str(term[11]).lower().strip()):  #Synonym 1
                        # if(x[0].lower().strip() == str(term[11]).lower().strip()):
                        # print("NRC: " + term[0] + " PERMA: " + x[0] + " CATEGORY: " + x[1] + " ID: " + str(word_count))
                        perma_term_got.append([word_count, term[0], x[0], x[1], x[2]])
        return perma_term_got

import csv
def read_csv():
    with open('C:\\Users\\Acer\\Documents\\GitHub\\MHBot\\MHBot\\NRC_Perma_Lexicon\\nrc_emotion_lexicon.csv', 'r') as nrc_file:
        nrc_reader = csv.reader(nrc_file)
        word_count = 1
        list_all_words = []
        for nrc_row in nrc_reader:
            perma_row = read_perma(nrc_row, word_count)
            word_count = word_count + 1;
            # print(perma_row[0])
            # print("fish")
            if perma_row != None and word_count!=2:
                for term_ish in perma_row:
                    list_all_words.append(term_ish)
        return list_all_words;

def write_nrc_perma():
    new_format_perma = []
    new_format_perma.append(['emotion_id', 'nrc_term', 'perma_term', 'perma_category', 'perma_score'])
    final_list = read_csv();
    for term in final_list:
        new_format_perma.append(term)
    return new_format_perma;



print("start")
perma_final = write_nrc_perma()
write_data(perma_final)
print("done")
