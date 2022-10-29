from sample_package import sample


def test_sample():
    result = sample.hello()
    assert result == 4
