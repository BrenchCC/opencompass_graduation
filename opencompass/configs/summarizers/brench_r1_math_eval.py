from mmengine.config import read_base

summarizer = dict(
    dataset_abbrs=[
        ['aime2024','accuracy'],
        ['math-500','accuracy']
    ],
    summary_groups=sum(
        [v for k, v in locals().items() if k.endswith('_summary_groups')], []),
)