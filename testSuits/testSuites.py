import itertools

from nose.loader import TestLoader
from nose import run
from nose.suite import LazySuite

paths = ("E:\\pythonpractice\\apiautomation\\scripts")

def run_my_tests():
    all_tests = ()
    #for path in paths:
    all_tests = itertools.chain(all_tests, TestLoader().loadTestsFromDir(paths))
    suite = LazySuite(all_tests)
    run(suite=suite)

if __name__ == '__main__':
    run_my_tests()