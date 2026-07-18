#!/usr/bin/env python3
import sys

def test_addition():
    assert 2 + 2 == 4, "Addition test failed"
    print("✅ Addition test passed")

def test_subtraction():
    assert 5 - 3 == 2, "Subtraction test failed"
    print("✅ Subtraction test passed")

def test_string():
    assert "hello".upper() == "HELLO", "String test failed"
    print("✅ String test passed")

if __name__ == "__main__":
    print("🧪 Running tests...")
    test_addition()
    test_subtraction()
    test_string()
    print("🎉 All tests passed!")
    sys.exit(0)  # Success
