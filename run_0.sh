CUDA_VISIBLE_DEVICES=0 python process_whole.py \
    --model_path "/hdd/hjl8708/workspace/AMR-LDA//AMR-LDA_prompt_augmentation/pretrained_models" \
    --data_path "/hdd/hjl8708/workspace/AMR-LDA/AMR-LDA_prompt_augmentation/data/RULE/Trainable_ReClor_900.jsonl" \
    --result_data_path "/hdd/hjl8708/workspace/AMR-LDA/AMR-LDA_prompt_augmentation/result/Trainable_ReClor_900-AMR_LDA.jsonl"

CUDA_VISIBLE_DEVICES=0 python process_whole.py \
    --model_path "/hdd/hjl8708/workspace/AMR-LDA//AMR-LDA_prompt_augmentation/pretrained_models" \
    --data_path "/hdd/hjl8708/workspace/AMR-LDA/AMR-LDA_prompt_augmentation/data/RULE/Trainable_ReClor_1800.jsonl" \
    --result_data_path "/hdd/hjl8708/workspace/AMR-LDA/AMR-LDA_prompt_augmentation/result/Trainable_ReClor_1800-AMR_LDA.jsonl"

# CUDA_VISIBLE_DEVICES=1 python process_whole.py \
#     --model_path "/hdd/hjl8708/workspace/AMR-LDA//AMR-LDA_prompt_augmentation/pretrained_models" \
#     --data_path "/hdd/hjl8708/workspace/AMR-LDA/AMR-LDA_prompt_augmentation/data/RULE/Trainable_ReClor_2700.jsonl" \
#     --result_data_path "/hdd/hjl8708/workspace/AMR-LDA/AMR-LDA_prompt_augmentation/result/Trainable_ReClor_2700-AMR_LDA.jsonl"

# CUDA_VISIBLE_DEVICES=1 python process_whole.py \
#     --model_path "/hdd/hjl8708/workspace/AMR-LDA//AMR-LDA_prompt_augmentation/pretrained_models" \
#     --data_path "/hdd/hjl8708/workspace/AMR-LDA/AMR-LDA_prompt_augmentation/data/RULE/Trainable_ReClor_3695.jsonl" \
#     --result_data_path "/hdd/hjl8708/workspace/AMR-LDA/AMR-LDA_prompt_augmentation/result/Trainable_ReClor_3695-AMR_LDA.jsonl"