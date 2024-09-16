from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/randomize')
def randomize():
    array = random.sample(range(1, 101), 20)  # Generate 20 random numbers
    return jsonify(array)

@app.route('/bubble_sort/<array>')
def bubble_sort(array):
    arr = list(map(int, array.split(',')))
    n = len(arr)
    steps = []  # To store the steps for visualization
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            steps.append(arr.copy())  # Store the current state of the array
    return jsonify(steps)

@app.route('/selection_sort/<array>')
def selection_sort(array):
    arr = list(map(int, array.split(',')))
    n = len(arr)
    steps = []  # To store the steps for visualization
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        steps.append(arr.copy())  # Store the current state of the array
    return jsonify(steps)

@app.route('/insertion_sort/<array>')
def insertion_sort(array):
    arr = list(map(int, array.split(',')))
    n = len(arr)
    steps = []  # To store the steps for visualization
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        steps.append(arr.copy())  # Store the current state of the array
    return jsonify(steps)

@app.route('/merge_sort/<array>')
def merge_sort(array):
    arr = list(map(int, array.split(',')))
    steps = []  # To store the steps for visualization

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = sort(arr[:mid])
        right = sort(arr[mid:])
        merged = merge(left, right)
        steps.append(merged)  # Store the current state of the array
        return merged

    sort(arr)
    return jsonify(steps)
'''
@app.route('/quick_sort/<array>')
def quick_sort(array):
    arr = list(map(int, array.split(',')))
    steps = []  # To store the steps for visualization

    def sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        steps.append(arr.copy())  # Store the current state of the array
        return sort(left) + middle + sort(right)

    sort(arr)
    return jsonify(steps)  '''

@app.route('/quick_sort/<array>')
def quick_sort(array):
    arr = list(map(int, array.split(',')))
    steps = []  # To store the steps for visualization

    def sort(arr):
        if len(arr) <= 1:
            steps.append(arr.copy())  # Capture the final state
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        # Capture the current state of the array
        steps.append(left + middle + right)
        
        return sort(left) + middle + sort(right)

    sort(arr)
    steps.append(arr.copy())  # Capture the final sorted state
    print(f"Steps captured: {steps}")  # Log the captured steps
    return jsonify(steps)



@app.route('/heap_sort/<array>')
def heap_sort(array):
    arr = list(map(int, array.split(',')))
    steps = []  # To store the steps for visualization

    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            steps.append(arr.copy())  # Store the current state of the array
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        steps.append(arr.copy())  # Store the current state of the array
        heapify(arr, i, 0)

    return jsonify(steps)

if __name__ == '__main__':
    app.run(debug=True)
