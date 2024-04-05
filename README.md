# AMR-LDA_prompt_augmentation

## Requirements
1. make pretrained_models folder
2. download model_generate_t5wtense-v0_1_0 and model_parse_xfm_bart_large-v0_1_0 from https://github.com/bjascob/amrlib-models to ./pretrained_models 
<br> (wget https://github.com/bjascob/amrlib-models/releases/download/parse_xfm_bart_large-v0_1_0/model_parse_xfm_bart_large-v0_1_0.tar.gz)
<br> (wget https://github.com/bjascob/amrlib-models/releases/download/model_generate_t5wtense-v0_1_0/model_generate_t5wtense-v0_1_0.tar.gz)
2. unzip them

## Temp
코드 전체 구성

input: 데이터셋
- RULE 모든 문제들
- option 문제들

output: augmented 데이터셋
- RULE 모든 문제들
- option 문제들


0. 전체 데이터를 처리하는 함수
    각 row에 대해서 1번을 반복하고 

1. (process_whole) 원본 데이터를 row 단위로 입력받고 그 row를 전체 처리하는 함수
    -> context
    -> question
    -> option

    input: row
    output: processed row

    context와 각 option은 각각 (2) 함수로 들어가서 처리된다
    (question)은 처리되지 않음

2. (row_process) 각 text를 AMR-LDA로 augmentation 하는 함수
    input: TEXT
    output: Augmented TEXT

3. (text_augmentation) 전체 과정을 바탕으로 EC-finetuning의 format에 맞게 변경해서 바로 inference할 수 있게 만듦

4. (original_to_option) augmented original을 바탕으로 YES/NO 문제를 생성함
