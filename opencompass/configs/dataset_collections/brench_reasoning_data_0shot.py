from mmengine.config import read_base

with read_base():
    from opencompass.configs.datasets.gsm8k.gsm8k_brench_0shot_v1 import gsm8k_datasets
    from opencompass.configs.datasets.math.math_brench_0shot import math_datasets
    from opencompass.configs.datasets.humaneval.humaneval_brench_v1 import humaneval_datasets

datasets = sum((v for k, v in locals().items() if k.endswith('_datasets')), [])
