class Codec:

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        """
        shortUrl=''
        for i in longUrl:
            if i == '/':
                shortUrl=shortUrl+','
            else:
                shortUrl=shortUrl+i
        self.shortUrl=shortUrl

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        """
        longUrl=''
        for i in self.shortUrl:
            if i == ',':
                longUrl=longUrl+'/'
            else:
                longUrl=longUrl+i
        self.longUrl=longUrl
        return longUrl

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))