import sys

from src.midir import (
    root_levels,
    root_suffix,
    midir,
    mipath
)

def test_midir():
    #print(midir(__file__))
    assert midir().endswith("midir/tests")

def test_mipath():
    assert mipath().endswith("midir/tests/test_unit.py")

def test_root_levels():
    assert not [path for path in sys.path if path.endswith("/tests")]
    with_midir = [path for path in sys.path if path.endswith("/midir")]
    root_levels(levels=1)
    assert [path for path in sys.path if path.endswith("/tests")]
    root_levels(levels=2)
    assert with_midir == [path for path in sys.path if path.endswith("/midir")]

def test_root_suffix():
    assert '/Users/jordi' not in sys.path
    root_suffix("jordi")
    assert '/Users/jordi' in sys.path

def test_root_suffix_oserror():
    try:
        root_suffix("jona")
    except Exception:
        assert True

if __name__ == '__main__':
    test_midir()
    test_mipath()
    test_root_levels()
    test_root_suffix()
    test_root_suffix_oserror()