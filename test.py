import unittest
import finder

# Global Variable Section
WORD = "bad"
STRING_LIST = ['abd', 'dab', 'fre', 'glk', 'lkm']
LARGE_STRING_LIST = ['abd', 'saw', 'sasfwfss',
                     'wewewee', 'ffgt', 'wscf', 'outt',
                     'traa', 'frew', 'lkjh', 'cdeea','pdw',
                     'ntrs',  'dab', 'itr', 'qllq', 'ceuzr',
                     'icswa', 'ztsr']
POS_RESULT = ['abd', 'dab']
NEG_RESULT = []


# Utility function to compare the data in two list
# and determine if the lists are same according to the
# content or not
def compare_list(list_a, list_b):
    """
    Function to check if the two lists are
    identical according to the data or not.
    Order of the data is not considered here
    @param: two lists
    @return: True: if the two lists are same
             False: If the two lists are not same
    """
    if set(list_a) == set(list_b):
        return True
    else:
        return False


class TestFinderMethods(unittest.TestCase):

    def test_positive(self):
        finder_obj = finder.Finder(STRING_LIST)
        self.assertEqual(True, compare_list(finder_obj.find(WORD),
                                            POS_RESULT),
                         "Test case Passed")

    def test_negative(self):
        finder_obj = finder.Finder(STRING_LIST)
        self.assertEqual(False, compare_list(finder_obj.find(WORD),
                                             NEG_RESULT),
                         "Negative test case passed")

    def test_large_dataset(self):
        finder_obj = finder.Finder(LARGE_STRING_LIST)
        self.assertEqual(True, compare_list(finder_obj.find(WORD),
                                            POS_RESULT),
                         "Test case for large dataset Passed")


if __name__ == '__main__':
    unittest.main()
