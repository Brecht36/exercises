import pytest
from parentheses import matching_parentheses


@pytest.mark.parametrize('string', [
    ("((((((()))))))"),
    ("(n(n(n(n(n(n(n(n(n(n(n)))))))))))"),
    ("nnn(xxx()x)x()"),
    (")()(")
])
def test_matching_parentheses(string):
    assert matching_parentheses(string), f"{string} has matching parantheses."
    
@pytest.mark.parametrize('string', [
    ("((((((())))))"),
    ("(n(n(n(n(n(n(n(n(n(n(n))))))))))"),
    ("nnn(xxx)x)x()"),
    ("))(")
])

def test_no_matching_parentheses(string):
    assert not matching_parentheses(string), f"{string} has no matching parantheses!"
