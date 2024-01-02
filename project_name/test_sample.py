from project_name.sample import sample_logic


def test_if_expected_integer_is_returned() -> None:
    """
    Sample test
    """
    assert sample_logic() == 0
    assert sample_logic(x=None) == 0
    assert sample_logic(x=1) == 1
