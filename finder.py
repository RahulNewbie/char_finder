from collections import Counter

# Global Variable Section
WORD = "rahul"
STRING_LIST = ['rahlu', 'rhula', 'asd', 'gesdlk', 'das', 'hular']


class Finder:
    # Constructor
    def __init__(self, string_list):
        """
        initializing instance list.
        """
        self.str_list = string_list

    def find(self, word):
        """
        Find the matching string from the string list
        """
        matching_list = []
        # First it iterates in string list and extract
        # every string from the List.
        # Then it checks the following
        # 1. If the length of the provided string is same with the
        # string from the string list
        # 2. if all the characters of the provided string is present
        # in the string from the string list
        # If both condition made, then append that into resulting list
        # which will be the output
        for item in self.str_list:
            if (len(word) is len(item)) and\
                    (len(word) is sum((Counter(word) &
                                       Counter(item)).values())):
                matching_list.append(item)

        # To remove any redundant entry, first resulting list
        # converted into a set and then again converted into a list to
        # to return the resulting list
        return list(set(matching_list))


if __name__ == '__main__':
    finder_obj = Finder(STRING_LIST)
    match = finder_obj.find(WORD)
    print(match)
