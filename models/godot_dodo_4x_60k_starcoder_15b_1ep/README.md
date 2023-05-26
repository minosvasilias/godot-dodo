# godot_dodo_4x_60k_starcoder_15b_1ep

This model is a finetune of `starcoder` using the [godot_dodo_4x_60k](../../data/godot_dodo_4x_60k/) dataset.

## Weights

Weights are available on Huggingface: [godot_dodo_4x_60k_starcoder_15b_1ep](https://huggingface.co/minosu/godot_dodo_4x_60k_starcoder_15b_1ep)

## Training

Below is the exact command that was used to finetune this model on an `8xA10080GB` GPU instance.
The checkpoint stored after 400 iterations was used for above weights.

If you are using less than 8 GPUs, change `nproc_per_node` to the number of GPUs used.

```bash
torchrun --nproc_per_node=8 --master_port=2023 finetune/train.py \
    --model_name_or_path "bigcode/starcoder" \
    --data_path ./data/godot_dodo_4x_60k/godot_dodo_4x_60k_data.json \
    --bf16 True \
    --output_dir godot_dodo_4x_60k_starcoder_15b \
    --num_train_epochs 3 \
    --per_device_train_batch_size 2 \
    --per_device_eval_batch_size 2 \
    --gradient_accumulation_steps 8 \
    --evaluation_strategy "no" \
    --save_strategy "steps" \
    --save_steps 200 \
    --learning_rate 2e-5 \
    --weight_decay 0. \
    --warmup_ratio 0.03 \
    --lr_scheduler_type "cosine" \
    --logging_steps 1 \
    --fsdp "full_shard auto_wrap" \
    --fsdp_transformer_layer_cls_to_wrap 'GPTBigCodeBlock' \
    --tf32 True
```
