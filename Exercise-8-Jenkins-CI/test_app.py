from app import greet

def test_greet():
    assert greet() == "Hello from the Jenkins CI exercise!"

if __name__ == "__main__":
    test_greet()
    print("Test passed")
