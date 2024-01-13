import jieba


def extract_keywords(anchor_text):
    # 中文分词
    anchor_words = list(jieba.cut(anchor_text))

    # 返回所有分词作为关键词
    return set(anchor_words)


def calculate_interaction_score(anchor_keywords, barrage_text):
    # 中文分词
    barrage_words = list(jieba.cut(barrage_text))

    # 弹幕中出现的主播话关键词数量
    common_keywords = len(set(anchor_keywords).intersection(set(barrage_words)))

    # 计算互动度得分（关键词出现次数）
    interaction_score = common_keywords / len(anchor_keywords)

    return interaction_score



def jiaohu(s, d):
    # 提取关键词
    anchor_keywords = extract_keywords(s)
    # 计算互动度得分
    score = calculate_interaction_score(anchor_keywords, d)
    return score

# # 示例：将主播的话进行分词，并计算互动度得分
# anchor_text = "男枪确实有操作太六了笑死你粉丝也防我也绷不住了[dog]武器破防了哈哈哈哈我说过都回来全部一开全是活呀[吃瓜]了？？？？？？？大胆"
# barrage_text = "男枪确实有操作太六了笑死你粉丝也防我也绷不住了[dog]武器破防了哈哈哈哈我说过都回来全部一开全是活呀[吃瓜]了？？？？？？？大胆"
#
# # 提取关键词
# anchor_keywords = extract_keywords(anchor_text)
#
# # 计算互动度得分
# score = calculate_interaction_score(anchor_keywords, barrage_text)
# print("关键词：", anchor_keywords)
# print("互动度评分：", score)
#

