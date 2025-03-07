from mmengine.config import read_base

with read_base():
    #from opencompass.configs.datasets.math.math_500_gen import math_datasets
    from opencompass.configs.datasets.aime2024.aime2024_gen_6e39a4 import aime2024_datasets

datasets = sum((v for k, v in locals().items() if k.endswith('_datasets')), [])
