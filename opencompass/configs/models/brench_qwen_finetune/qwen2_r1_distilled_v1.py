from opencompass.models import OpenAISDK

api_meta_template = dict(
    round=[
        dict(role='HUMAN', api_role='HUMAN'),
        dict(role='BOT', api_role='BOT', generate=True),
    ],
    reserved_roles=[dict(role='SYSTEM', api_role='SYSTEM')],
)

models = [
    dict(
        abbr='qwen2_r1_distilled_v1',
        type=OpenAISDK,
        key='EMPTY', # API key
        openai_api_base='http://0.0.0.0:8081/v1', # 服务地址
        path='qwen2_r1_distilled_v1', # 请求服务时的 model name
        tokenizer_path='/Users/bytedance/BrenchProjects/Graduation_Evaluation/opencompass/tokenizers_saves/qwen2', # 请求服务时的 tokenizer name 或 path, 为None时使用默认tokenizer gpt-4
        rpm_verbose=True, # 是否打印请求速率
        meta_template=api_meta_template, # 服务请求模板
        query_per_second=10, # 服务请求速率
        max_out_len=8192, # 最大输出长度
        max_seq_len=8192, # 最大输入长度
        temperature=0.7, # 生成温度
        batch_size=8, # 批处理大小
        retry=3, # 重试次数
    )
]