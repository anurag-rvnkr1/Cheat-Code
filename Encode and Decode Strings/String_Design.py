'''
271. Encode and Decode Strings

Design an algorithm to encode a list of strings into a single string.
The encoded string can then be decoded back to the original list of strings.

Implement the Codec class:

    - encode(strs): Encodes a list of strings into a single string.
    - decode(s): Decodes a single string back into the original list of strings.

Note:
    The encoded string should be decodable without ambiguity.
    The strings may contain any possible characters, including '#', digits,
    spaces, and special symbols.

Example 1:
    Input:
        strs = ["lint","code","love","you"]

    Output:
        ["lint","code","love","you"]

Example 2:
    Input:
        strs = ["we","say",":","yes"]

    Output:
        ["we","say",":","yes"]

Constraints:
    0 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] may contain any valid ASCII character.
'''

# String Design


class Codec:

    def encode(self, strs):
        """
        Encodes a list of strings to a single string.
        Format: <length>#<string>
        """
        encoded = ""

        for string in strs:
            encoded += str(len(string)) + "#" + string

        return encoded

    def decode(self, s):
        """
        Decodes a single string to a list of strings.
        """
        decoded = []
        index = 0

        while index < len(s):
            separator = index

            # Find '#'
            while s[separator] != "#":
                separator += 1

            length = int(s[index:separator])

            start = separator + 1
            end = start + length

            decoded.append(s[start:end])
            index = end

        return decoded


# Example usage
codec = Codec()

# Example 1
strs1 = ["lint", "code", "love", "you"]
encoded1 = codec.encode(strs1)

print(encoded1)
# Output: "4#lint4#code4#love3#you"

print(codec.decode(encoded1))
# Output: ['lint', 'code', 'love', 'you']

# Example 2
strs2 = ["we", "say", ":", "yes"]
encoded2 = codec.encode(strs2)

print(encoded2)
# Output: "2#we3#say1#:3#yes"

print(codec.decode(encoded2))
# Output: ['we', 'say', ':', 'yes']

# Example 3
strs3 = ["", "abc", "", "hello world"]
encoded3 = codec.encode(strs3)

print(encoded3)
# Output: "0#3#abc0#11#hello world"

print(codec.decode(encoded3))
# Output: ['', 'abc', '', 'hello world']

# Example 4
strs4 = ["123", "#$%", "Python", "DSA"]
encoded4 = codec.encode(strs4)

print(codec.decode(encoded4))
# Output: ['123', '#$%', 'Python', 'DSA']
