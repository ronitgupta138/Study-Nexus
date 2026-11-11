# Unit test asserting LRU frame eviction order

def test_lru_eviction():
    capacity = 3
    frames = ["P1", "P2", "P3"]
    frames.remove("P1")
    frames.append("P1")
    victim = frames.pop(0)
    assert victim == "P2"
