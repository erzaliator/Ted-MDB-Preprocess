import pandas as pd
import os

def get_conn(raw, line, rel_type):
    if rel_type=='Implicit': return line[7]
    return get_split_text(raw, line, index=1)
        
def get_split_text(raw, line, index):
    arg_text=line[index]
    try: 
        x,y = arg_text.split('..')
        x,y = int(x), int(y)
        return raw[x:y]
    except:
        return None #first raw file only one rejected line for conn_text

def save_ted_file(file_name, lang):
    ann = open('./Ted-MDB-Annotations/'+lang+'/ann/01/'+file_name+'.txt')
    raw = open('./Ted-MDB-Annotations/'+lang+'/raw/01/'+file_name+'.txt').read()
    csv = './Ted-MDB-csv/'+lang+'/'+file_name+'.csv'

    output_row = {"rel_type": ['rel_type'], "rel_sense": ['rel_sense'], "conn_text": ['conn_text'], "arg1_text": ['arg1_text'], "arg2_text": ['arg2_text']}
    pd.DataFrame(output_row).to_csv(csv, mode='w', sep="\t", index=False, header=False)

    for line in ann:
        line=line.split('|')
        rel_type = line[0]
        rel_sense = line[8]
        conn_text = get_conn(raw, line, rel_type)
        arg1_text = get_split_text(raw, line, index=14)
        arg2_text = get_split_text(raw, line, index=20)

        if rel_type=='NoRel' or rel_type=='EntRel':
            continue
            
        elif rel_type=='Explicit' or rel_type=='AltLex':
            if conn_text is None:
                continue
                
        elif rel_type=='Implicit':
            pass
        output_row = {"rel_type": [rel_type], "rel_sense": [rel_sense], "conn_text": [conn_text], "arg1_text": [arg1_text], "arg2_text": [arg2_text]}
        pd.DataFrame(output_row).to_csv(csv, mode='a', sep="\t", index=False, header=False)
        
        
langs = ['English', 'Polish', 'Turkish', 'German', 'Lithuanian', 'Portuguese', 'Russian']
for lang in langs:
    print(lang)
    if lang=='English':
        for file_name in ['talk_1927_en', 'talk_1978_en', 'talk_2150_en_intra', 'talk_1971_en', 'talk_2009_en', 'talk_1976_en', 'talk_2150_en_inter']:
            save_ted_file(file_name, lang)
    elif lang=='Polish':
        for file_name in ['talk_1927_pl', 'talk_1978_pl', 'talk_2150_pl_intra', 'talk_1971_pl', 'talk_2009_pl', 'talk_1976_pl', 'talk_2150_pl_inter']:
            save_ted_file(file_name, lang)
    elif lang=='Turkish':
        for file_name in ['talk_1927_tr', 'talk_1978_tr', 'talk_2150_tr_intra', 'talk_1971_tr', 'talk_2009_tr', 'talk_2150_tr', 'talk_1976_tr', 'talk_2150_tr_inter']:
            save_ted_file(file_name, lang)
    elif lang=='German':
        for file_name in ['talk_1927_de', 'talk_1978_de', 'talk_2150_de_intra', 'talk_1971_de', 'talk_2009_de', 'talk_1976_de', 'talk_2150_de_inter']:
            save_ted_file(file_name, lang)
    elif lang=='Lithuanian':
        for file_name in ['talk_1927_lt', 'talk_1978_lt', 'talk_2150_lt_intra', 'talk_1971_lt', 'talk_2009_lt', 'talk_1976_lt', 'talk_2150_lt_inter']:
            save_ted_file(file_name, lang)
    elif lang=='Portuguese':
        for file_name in ['talk_1927_pt_tok', 'talk_1978_pt_tok', 'talk_2150_pt_tok_intra', 'talk_1971_pt_tok', 'talk_2009_pt_tok', 'talk_1976_pt_tok', 'talk_2150_pt_tok_inter']:
            save_ted_file(file_name, lang)
    elif lang=='Russian':
        for file_name in ['talk_1927_ru', 'talk_1978_ru', 'talk_2150_ru_intra', 'talk_1971_ru', 'talk_2009_ru', 'talk_1976_ru', 'talk_2150_ru_inter']:
            save_ted_file(file_name, lang)
