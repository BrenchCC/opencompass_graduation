from mmengine.config import read_base

with read_base():
    from opencompass.configs.dataset_collections.brench_graduation_eval_data import datasets
    from opencompass.configs.models.brench_qwen_finetune.qwen2_instruct import models
    from opencompass.configs.summarizers.chat_OC15_multi_faceted import summarizer