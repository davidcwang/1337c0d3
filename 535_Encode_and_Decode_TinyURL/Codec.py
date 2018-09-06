"""
Problem: 535. Encode and Decode TinyURL
Url: https://leetcode.com/problems/encode-and-decode-tinyurl/description/
Author: David Wang
Date: 12/26/2017
"""

import string

class Codec:
    """
    Convert Url to shortened url (TinyUrl)

    Encode normal url to smaller url
    Decode TinyUrl to original url
    """

    BASE_URL = 'http://tinyurl.com/'
    encode_map = {}
    decode_map = {}
    next_id_list = [0] * 6
    alphabet = string.digits + string.ascii_letters
    index_map = {i: a for i, a in enumerate(alphabet)}

    def __update_next(self):
        for i in range(len(self.next_id_list) - 1, -1, -1):
            symbol = self.index_map[self.next_id_list[i]]
            if symbol != 'Z':
                self.next_id_list[i] += 1
                for j in range(i+1, len(self.next_id_list)):
                    self.next_id_list[j] = 0
                return
    
    def encode(self, long_url):
        """
        Encode a long url to a tiny url

        Args:
            long_url: The orignal url
        Returns:
            A tiny url
        """
        id_list = [self.index_map[x] for x in self.next_id_list]
        id_string = ''.join(id_list)
        self.encode_map[long_url] = id_string
        self.decode_map[id_string] = long_url
        self.__update_next()
        return self.BASE_URL + id_string

    def decode(self, short_url):
        """
        Decode the tiny url to the original url

        Args:
            short_url: The tiny url
        Returns:
            The orignal url
        """
        id_string = short_url.split('/')[-1]
        return self.decode_map[id_string]

