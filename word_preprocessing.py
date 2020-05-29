import argparse
import logging
import os

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from tqdm._tqdm_notebook import tqdm_notebook
import re



def get_args():
    parser = argparse.ArgumentParser(description='words preprocessing')
    parser.add_argument('--text', type=str, help='输入原始文本')
    return parser.parse_args()

def replace_func(input_file):
    p1 = re.compile(r'-\{.*?(zh-hans|zh-cn):([^;]*?)(;.*?)?\}-')
    p2 = re.compile(r'[(][: @ . , ？！\s][)]')
    p3 = re.compile(r'[「『]')
    p4 = re.compile(r'[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）0-9 , : ; \-\ \[\ \]\ ]')
    p5 = re.compile('<.*?>')
    p6 = re.compile('–')
    sentence = ""
    numstopwords = 0
    replaced_file = open('data/'+'preprocessed.txt', "w", encoding="utf8")
    with open('data/'+ input_file, 'r', encoding="utf8") as source_f:
        print('data/'+ input_file + " reading")
        for line in tqdm_notebook(source_f):
            line = p1.sub(r' ', line)
            line = p2.sub(r' ', line)
            line = p3.sub(r' ', line)
            line = p4.sub(r' ', line)
            line = p5.sub(r' ', line)
            line = p6.sub(r' ', line)
            line = line.lower()
            sentence += line
        sentence_list = sentence.split(' ')
        print('data/' + input_file + " to list")
        for word in sentence_list:
            word = WordNetLemmatizer().lemmatize(word)
            if not word in stopwords.words('english'):
                replaced_file.write(word + " ")
            else:
                numstopwords += 1
                if numstopwords % 100 == 0:
                    print("number of stopwords",numstopwords)
        replaced_file.close()




def main():
    args = get_args()

    if not args.text == '':
        replace_func(args.text)
        print('has been processed !')
    else:
        logging.info('Unknown this text %s, should be "text"', args.text)
        return

if __name__ == '__main__':
    os.makedirs('data/', exist_ok=True)
    main()