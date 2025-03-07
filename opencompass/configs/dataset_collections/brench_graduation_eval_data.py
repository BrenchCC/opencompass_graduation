from mmengine.config import read_base

with read_base():
    from opencompass.configs.datasets.mmlu.mmlu_gen_4d595a import mmlu_datasets
    from opencompass.configs.datasets.gsm8k.gsm8k_gen_1d7fe4 import gsm8k_datasets
    from opencompass.configs.datasets.humaneval.humaneval_gen_8e312c import humaneval_datasets

datasets = sum((v for k, v in locals().items() if k.endswith('_datasets')), [])
