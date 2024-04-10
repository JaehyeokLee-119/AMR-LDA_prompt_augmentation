# 각 옵션 칸에 option = option + augmented_option + augmented_context

import json 
import pandas as pd

def load_jsonl(file_path):
    return pd.read_json(file_path, lines=True)

dirname = 'result'
fname = 'RULE_subq_all-AMR_LDA'

data = load_jsonl(f'{dirname}/{fname}.jsonl')

# data['answers']의 각 원소[i]에다가 augmented_answers[i]와 augmented_context를 합쳐서 넣어주기ㅏ
def func(row):
    context_list = [row['augmented_context'] for i in range(len(row['answers']))]
    # row['answers']의 각 element에다가 augmented_answers와 augmented_context의 각 element를 더하기
    for i in range(len(row['answers'])):
        if row['answers'][i].strip()[-1] not in ['.', '!', '?']:
            row['answers'][i] = row['answers'][i].strip()
            row['answers'][i] += '.'
    
    # '  ' to ' '
    def remove_double_space(s):
        while '  ' in s:
            s = s.replace('  ', ' ')
        return s    
    
    return [remove_double_space(f"{row['answers'][i]} {row['augmented_answers'][i].strip()} {context_list[i].strip()}".strip()) for i in range(len(row['answers']))]

for i in range(len(data)):
    data['answers'][i] = func(data.iloc[i])
    

data.to_json(f'{dirname}/{fname}-reflected.jsonl', orient='records', lines=True)