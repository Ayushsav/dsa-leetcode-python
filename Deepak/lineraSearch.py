def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage
if __name__ == "__main__":
    arr = [10, 23, 45, 70, 11, 15]
    target = 70
    result = linear_search(arr, target)
    
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in the array")