class Codec:
    hashmap = {}
    codeccount = -1
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        self.codeccount += 1
        self.hashmap[self.codeccount] = longUrl
        return 'http://tinyurl.com/' + str(self.codeccount)
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        codenumber = shortUrl.split('http://tinyurl.com/')[1]
        return self.hashmap[int(codenumber)]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))