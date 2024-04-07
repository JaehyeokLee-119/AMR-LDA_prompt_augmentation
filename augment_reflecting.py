# 각 옵션 칸에 option = option + augmented_option + augmented_context

import json 
import pandas as pd

def load_jsonl(file_path):
    return pd.read_json(file_path, lines=True)

fname = 'result/Trainable_ReClor_AMR-LDA_300.jsonl'

data = load_jsonl(fname)

# data['answers']의 각 원소[i]에다가 augmented_answers[i]와 augmented_context를 합쳐서 넣어주기ㅏ
def func(row):
    context_list = [row['augmented_context'] for i in range(len(row['answers']))]
    # row['answers']의 각 element에다가 augmented_answers와 augmented_context의 각 element를 더하기
    for i in range(len(row['answers'])):
        if row['answers'][i][-1] not in ['.', '!', '?']:
            row['answers'][i] += '.'
    return [f"{row['answers'][i]} {row['augmented_answers'][i]} {context_list[i]}" for i in range(len(row['answers']))]

for i in range(len(data)):
    data['answers'][i] = func(data.iloc[i])
    

data.to_json('Trainable_ReClor_AMR-LDA_300_augmented.jsonl', orient='records', lines=True)