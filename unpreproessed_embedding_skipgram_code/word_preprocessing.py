import argparse
import logging
import os
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
    replaced_file = open('data/'+'preprocessed.txt', "w", encoding="utf8")
    with open('data/'+ input_file, 'r', encoding="utf8") as source_f:
        for line in tqdm_notebook(source_f):
            line = p1.sub(r' ', line)
            line = p2.sub(r' ', line)
            line = p3.sub(r' ', line)
            line = p4.sub(r' ', line)
            line = p5.sub(r' ', line)
            line = p6.sub(r' ', line)

            replaced_file.write(line)

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