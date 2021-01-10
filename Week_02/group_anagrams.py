class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 字典，键是排序后字符串，值是原字符串的列表
        word_dict = {}
        for word in strs:
            # 对每个字符串排序，作为键
            key = "".join(sorted(word))
            # 把原字符串添加到列表中
            if key in word_dict.keys():
                word_dict[key].append(word)
            else:
                word_dict[key] = [word, ]
        # 返回原字符串列表
        return list(word_dict.values())
