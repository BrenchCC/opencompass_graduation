from mmengine.config import read_base

with read_base():
    from opencompass.configs.dataset_collections.brench_eval_r1_math import datasets
    from opencompass.configs.models.brench_qwen_finetune.qwen2dot5_instruct import models
    from opencompass.configs.summarizers.brench_r1_math_eval import summarizer