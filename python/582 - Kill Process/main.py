import collections
class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        pidmapppid = collections.defaultdict(list)
        for index, parts in enumerate(pid):
            pidmapppid[ppid[index]].append(parts)
        stack=[]
        finalstack=[]
        stack.append(kill)
        while stack:
            tmptarget = stack[-1]
            finalstack.append(tmptarget)
            stack.pop()
            if pidmapppid[tmptarget]:
                stack = stack + pidmapppid[tmptarget]
                pidmapppid[tmptarget]=[]
        return finalstack     
        
        