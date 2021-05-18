import collections
class FreqStack(object):

    def __init__(self):
        self.freq = collections.Counter()
        self.group = collections.defaultdict(list)
        self.maxfreq = 0

    def push(self, x):
        freqtmp = self.freq[x] + 1
        self.freq[x] = freqtmp
        if freqtmp > self.maxfreq:
            self.maxfreq = freqtmp
        self.group[freqtmp].append(x)

    def pop(self):
        result = self.group[self.maxfreq].pop()
        self.freq[result] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        return result
        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()