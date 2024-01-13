from transformers import BertTokenizer, BertForSequenceClassification
import torch

def calculate_chinese_emotion_bert(text):
    # 使用 BERT 预训练模型和分词器
    # 指定本地路径
    local_model_path = r'D:\desk\bert-base-chinese'

    tokenizer = BertTokenizer.from_pretrained(local_model_path)
    model = BertForSequenceClassification.from_pretrained(local_model_path)

    # 截断文本以适应模型最大输入长度
    max_length = model.config.max_position_embeddings - 2  # 保留两个位置给特殊标记 [CLS] 和 [SEP]
    truncated_text = text[:max_length]
    # 分词并转换为模型输入格式
    inputs = tokenizer(truncated_text, return_tensors="pt", truncation=True, padding=True)

    # 获取模型输出
    outputs = model(**inputs)
    logits = outputs.logits

    # 计算情感概率
    probabilities = torch.softmax(logits, dim=1).tolist()[0]

    # 返回正面和负面概率
    positive_prob = probabilities[1]
    negative_prob = probabilities[0]

    return positive_prob, negative_prob

# # 长文本
# long_text = "那个地方失误了发条那时候发条唯一大到发条唯一大到我的意思后面就没大到过了因为你不管发条球藏的有多好你发条不可能站在我脸上开大礼应该不会有人玩个发条把球给自己然后团站阿闪球给自己阿闪阿闪经常吗当时团人玩不可能吧对吧我上个寺所去这旁光局啊那有个那有那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事那有什么事"
#
# # 计算情感概率
# result_bert = calculate_chinese_emotion_bert(long_text)
#
# # 打印结果
# print(f"正面概率: {result_bert[0]}, 负面概率: {result_bert[1]}")
