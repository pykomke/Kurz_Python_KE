import nose.tools as nt
from IPython.utils.dir2 import dir2


class Base(object):
    x = 1
    z = 23


def test_base():
    res = dir2(Base())
    assert ('x' in res)
    assert ('z' in res)
    assert ('y' not in res)
    assert ('__class__' in res)
    nt.assert_equal(res.count('x'), 1)
    nt.assert_equal(res.count('__class__'), 1)

def test_SubClass():

    class SubClass(Base):
        y = 2

    res = dir2(SubClass())
    assert ('y' in res)
    nt.assert_equal(res.count('y'), 1)
    nt.assert_equal(res.count('x'), 1)


def test_SubClass_with_trait_names_method():

    class SubClass(Base):
        y = 2
        def trait_names(self):
            return ['t', 'umbrella']

    res = dir2(SubClass())
    assert('trait_names' in res)
    assert('umbrella' in res)
    nt.assert_equal(res[-6:], ['t', 'trait_names','umbrella', 'x','y','z'])
    nt.assert_equal(res.count('t'), 1)


def test_SubClass_with_trait_names_attr():
    # usecase: trait_names is used in a class describing psychological classification

    class SubClass(Base):
        y = 2
        trait_names = 44

    res = dir2(SubClass())
    assert('trait_names' in res)
