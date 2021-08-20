# Python script demonstrating the base62 encoding algorithm for url shortening


class UrlShortener:
    id = 100  # suppose there are already 100 ids
    url_dict = {}  # to store original url : shortened id

    def shorten_url(self, input_url):
        # if input_url already exist
        if input_url in self.url_dict:
            id = self.url_dict[input_url]
            shorten_url = self.encode(self.id)

        else:
            self.url_dict[input_url] = self.id
            shorten_url = self.encode(self.id)
            self.id += 1

        return "short_url/" + shorten_url

    # func to perform base62 encoding
    def encode(self, id):
        # base-62 characters
        characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        base = len(characters)
        ret = []
        while id > 0:
            val = id % base
            ret.append(characters[val])
            id = id // base
        return "".join(ret[::-1]) # returning reverse str of list elements


# Driver-code
url_shortener = UrlShortener()
url = "https://www.linkedin.com/in/gaurav-pore-70a6501b0/"

print(url_shortner.shorten_url(url))
