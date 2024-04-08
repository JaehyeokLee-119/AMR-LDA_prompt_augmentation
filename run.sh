CUDA_VISIBLE_DEVICES=2 python process_whole.py \
    --model_path "/hdd/hjl8708/workspace/AMR-LDA//AMR-LDA_prompt_augmentation/pretrained_models" \
    --data_path "/hdd/hjl8708/workspace/AMR-LDA/AMR-LDA_prompt_augmentation/data/RULE/RULE_subq_all_1500.jsonl" \
    --result_data_path "/hdd/hjl8708/workspace/AMR-LDA/AMR-LDA_prompt_augmentation/result/RULE_subq_all-AMR_LDA-1500.jsonl

CUDA_VISIBLE_DEVICES=0 python process_whole.py \
    --model_path "/hdd/hjl8708/workspace/AMR-LDA//AMR-LDA_prompt_augmentation/pretrained_models" \
    --data_path "/hdd/hjl8708/workspace/AMR-LDA/AMR-LDA_prompt_augmentation/data/RULE/RULE_subq_all_3003.jsonl" \
    --result_data_path "/hdd/hjl8708/workspace/AMR-LDA/AMR-LDA_prompt_augmentation/result/RULE_subq_all-AMR_LDA-3003.jsonl