
import os 
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
import json 
import fire
import sentence_to_sentence as sts
from tqdm import tqdm
import re
import logging

def split_text_into_sentences_with_punctuation(text):
    # 정규 표현식을 사용하여 마침표, 물음표, 느낌표로 끝나는 문장을 찾아 분리
    # 결과에 구두점을 포함시킴
    sentences = re.findall(r'[^.!?]+[.!?]', text)
    sentences = [s.strip() for s in sentences]
    return sentences

def augment(text):
    # text를 sentence 별로 파싱
    # sentence 별로 SentenceManipulator.manipulate() 실행
    
    sentences = split_text_into_sentences_with_punctuation(text)    
    
    ''' 
    text = "In rheumatoid arthritis, the body' s immune system misfunctions by attacking healthy cells in the joints causing the release of a hormone that in turn causes pain and swelling. This hormone is normally activated only in reaction to injury or infection. A new arthritis medication will contain a protein that inhibits the functioning of the hormone that causes pain and swelling in the joints."
    
    sentences = [
        "In rheumatoid arthritis, the body' s immune system misfunctions by attacking healthy cells in the joints causing the release of a hormone that in turn causes pain and swelling",
        ' This hormone is normally activated only in reaction to injury or infection',
        ' A new arthritis medication will contain a protein that inhibits the functioning of the hormone that causes pain and swelling in the joints'
    ]    
    '''
    
    augmented_sentences = []
    for sentence in sentences:
        augmented_sentence, counts = SentenceManipulator.manipulate(sentence)
        augmented_sentences.append(augmented_sentence)
    
    result_text = ''
    for augmented_sentence in augmented_sentences:
        result_text += ' '.join(augmented_sentence)
    
    return result_text, counts

def process_row(row):
    id_string = row['id_string']
    data_name = row['data_name']
    context = row['context']
    question = row['question']
    answers = row['answers']
    label = row['label']
    others = row['others']
    
    # context, answers 처리하게 보내기
    augmented_context = augment(context)
    augmented_answers = [augment(q) for q in answers]
    
    augment_text_context = augmented_context[0]
    augment_type_context = augmented_context[1]
    augment_text_answers = [augmented_answer[0] for augmented_answer in augmented_answers]
    augment_type_answers = [augmented_answer[1] for augmented_answer in augmented_answers]
    
    if others is None:
        others = {}
        
    others['augment_type_context'] = augment_type_context
    others['augment_type_answers'] = augment_type_answers
    others['augment_type_label'] = ['double_negation', 'contraposition', 'commutative', 'implication']
    
    new_row = {
        "id_string": id_string,
        "data_name": data_name,
        "context": context,
        "question": question,
        "answers": answers,
        "augmented_context": augment_text_context,
        "augmented_answers": augment_text_answers,
        "label": label,
        "others": others,
    }
    return new_row
    
def process_whole(
    data_name = "RULE_mainq",
    data_path = f"/hdd/hjl8708/workspace/AMR-LDA/AMR-LDA_prompt_augmentation/data/RULE/RULE_mainq.jsonl",
    result_data_path = f"/hdd/hjl8708/workspace/AMR-LDA/AMR-LDA_prompt_augmentation/result/RULE_mainq_AMR-LDA.jsonl",
    augmentation = "AMR-LDA",
):
    # logger warning 무시
    logging.getLogger().setLevel(logging.ERROR)
    
    new_data = []
    global SentenceManipulator
    SentenceManipulator = sts.SentenceManipulator()
        # sentence -> manipulate() -> sentence list
    
    with open(data_path, "r") as f:
        data = f.readlines()
    
    for line in tqdm(data):
        row = json.loads(line)
        new_row = process_row(row)
        new_data.append(new_row)
    
    # jsonl로 저장
    with open(result_data_path, "w") as f:
        for new_row in new_data:
            f.write(json.dumps(new_row) + '\n')

if __name__ == '__main__':
    # conda activate amrlda
    fire.Fire(process_whole)

