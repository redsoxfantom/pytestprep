from pytestprep.testparser import parse_test_bank
import sys

testfile = sys.argv[1]
print("Parsing %s..." % testfile)
parse_test_bank(testfile)

