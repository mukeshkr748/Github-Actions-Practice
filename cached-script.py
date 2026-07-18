import requests
import numpy as np
import sys

print("📦 Testing with cached dependencies...")

# Test 1: requests
try:
    response = requests.get("https://httpbin.org/status/200")
    assert response.status_code == 200
    print("✅ requests test passed")
except:
    print("❌ requests test failed")
    sys.exit(1)

# Test 2: numpy
try:
    arr = np.array([1, 2, 3, 4, 5])
    assert arr.mean() == 3.0
    print("✅ numpy test passed")
except:
    print("❌ numpy test failed")
    sys.exit(1)

print("🎉 All cached tests passed!")
sys.exit(0)
