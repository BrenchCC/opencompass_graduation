from mmengine.config import read_base

with read_base():
    from opencompass.configs.dataset_collections.brench_eval_r1_math import datasets
    from opencompass.configs.models.brench_qwen_finetune.qwen2_r1_distilled_v1 import models
    from opencompass.configs.summarizers.chat_OC15_multi_faceted import summarizer