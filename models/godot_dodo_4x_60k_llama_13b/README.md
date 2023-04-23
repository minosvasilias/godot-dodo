# godot_dodo_4x_60k_llama_13b

This model is a finetune of `llama-13b` using the [godot_dodo_4x_60k](../../data/godot_dodo_4x_60k/) dataset.

## Weights

Weights are available on Huggingface: [godot_dodo_4x_60k_llama_13b](https://huggingface.co/minosu/godot_dodo_4x_60k_llama_13b)

## Training

Below is the exact command that was used to finetune this model.

Please note that we use the `yahma/llama-13b-hf` LLaMA weights instead of the more frequently referenced `decapoda-research/llama-13b-hf` ones. This is due to the latter being incompatible with the current release of the `transformers` library.

Feel free to use your own LLaMA weights instead of relying on huggingface-hosted ones. You can find further info regarding the process for that in the [stanford_alpaca](https://github.com/tatsu-lab/stanford_alpaca) repository.

If you are using less than 8 GPUs, change `nproc_per_node` to the number of GPUs used.

```bash
torchrun --nproc_per_node=8 --master_port=2023 finetune/train.py \
    --model_name_or_path "yahma/llama-13b-hf" \
    --data_path ./data/godot_dodo_4x_60k_data.json \
    --bf16 True \
    --output_dir godot_dodo_4x_60k_llama_13b \
    --num_train_epochs 3 \
    --per_device_train_batch_size 2 \
    --per_device_eval_batch_size 2 \
    --gradient_accumulation_steps 8 \
    --evaluation_strategy "no" \
    --save_strategy "steps" \
    --save_steps 500 \
    --save_total_limit 1 \
    --learning_rate 1e-5 \
    --weight_decay 0. \
    --warmup_ratio 0.03 \
    --lr_scheduler_type "cosine" \
    --logging_steps 1 \
    --fsdp "full_shard auto_wrap" \
    --fsdp_transformer_layer_cls_to_wrap 'LlamaDecoderLayer' \
    --tf32 True
```
