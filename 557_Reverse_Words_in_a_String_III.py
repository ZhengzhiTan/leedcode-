#Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
#Example 1:
#Input: s = "Let's take LeetCode contest"
#Output: "s'teL ekat edoCteeL tsetnoc"


def reverseWords(self, s: str) -> str:
        out = ''
        string = s.split(" ",s.count(" "))
        out = ' '.join(i[::-1] for i in string )
        return out
      
      
#recall lamada 

