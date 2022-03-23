# самое тупое решение:
class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        split_words = sentence.split(' ')

        for root in dictionary:
            for i in range(len(split_words)):
                if root in split_words[i]:
                    if root == split_words[i][:len(root)]:
                        split_words[i] = root

        return ' '.join(split_words)

sol = Solution()
print(sol.replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery"))

