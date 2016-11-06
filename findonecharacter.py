class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_list=list(s)
        t_list=list(t)
        s_list=sorted(s_list)
        t_list=sorted(t_list)
        result=""
        for i in range(len(s_list)):
            if s_list[i]!=t_list[i]:
                result=t_list[i]
                return result
        result=t_list[-1]
        return result