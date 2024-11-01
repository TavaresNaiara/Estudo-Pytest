import pytest

@pytest.fixture
def sample_list():
   return [1,2,3,4,5]

def test_soma(sample_list):
  assert sum(sample_list) == 15

def test_tamaho(sample_list):
  assert len(sample_list) == 5


