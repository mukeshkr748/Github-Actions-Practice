#!/usr/bin/env python3
import sys

print("🧪 Running tests...")

# Test 1
if 2 + 2 == 4:
    print("✅ Addition test passed")
else:
    print("❌ Addition test failed")
    sys.exit(1)

# Test 2
if "hello".upper() == "HELLO":
    print("✅ String test passed")
else:
    print("❌ String test failed")
    sys.exit(1)

print("🎉 All tests passed!")
sys.exit(0)
