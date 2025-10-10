class PrecisionFloat: #AMAL
    def __init__(self, value):
        if isinstance(value, str) and '.' in value:
            # Convert decimal string to fraction
            parts = value.split('.')
            integer_part = int(parts[0]) if parts[0] else 0
            decimal_part = parts[1]
            self.numerator = integer_part * (10 ** len(decimal_part)) + int(decimal_part)
            self.denominator = 10 ** len(decimal_part)
        elif isinstance(value, float):
            # Convert float to fraction by finding decimal representation
            str_val = f"{value:.15f}".rstrip('0')
            if '.' in str_val:
                self.__init__(str_val)
            else:
                self.numerator = int(value)
                self.denominator = 1
        else:
            self.numerator = int(value)
            self.denominator = 1
        self._simplify()
    
    def _gcd(self, a, b): #AMAL
        while b: a, b = b, a % b
        return a
    
    def _simplify(self): #aMAL
        gcd = self._gcd(abs(self.numerator), abs(self.denominator))
        self.numerator //= gcd
        self.denominator //= gcd
        if self.denominator < 0:
            self.numerator, self.denominator = -self.numerator, -self.denominator
    
    def __str__(self): #Hani
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator / self.denominator:.15g}"
    
    def add(self, other): #Hani
        if not isinstance(other, PrecisionFloat):
            other = PrecisionFloat(other)
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        result = PrecisionFloat(0)
        result.numerator, result.denominator = num, den
        result._simplify()
        return result
    
    def subtract(self, other): #srijana
        if not isinstance(other, PrecisionFloat):
            other = PrecisionFloat(other)
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        result = PrecisionFloat(0)
        result.numerator, result.denominator = num, den
        result._simplify()
        return result
    
    def multiply(self, other): #Hani
        if not isinstance(other, PrecisionFloat):
            other = PrecisionFloat(other)
        result = PrecisionFloat(0)
        result.numerator = self.numerator * other.numerator
        result.denominator = self.denominator * other.denominator
        result._simplify()
        return result
    
    def divide(self, other): #srijana
        if not isinstance(other, PrecisionFloat):
            other = PrecisionFloat(other)
        if other.numerator == 0:
            raise ZeroDivisionError("Division by zero")
        result = PrecisionFloat(0)
        result.numerator = self.numerator * other.denominator
        result.denominator = self.denominator * other.numerator
        result._simplify()
        return result

    def __lt__(self, other): #aAMAl
        if not isinstance(other, PrecisionFloat):
            other = PrecisionFloat(other)
        return self.numerator * other.denominator < other.numerator * self.denominator
    
    def __le__(self, other): #aAMaL
        return self.__lt__(other) or self.__eq__(other)
    
    def __eq__(self, other):
        if not isinstance(other, PrecisionFloat):
            other = PrecisionFloat(other)
        return self.numerator * other.denominator == other.numerator * self.denominator
    
    def __gt__(self, other):
        return not self.__le__(other)


# Sorting Algorithms 
def bubble_sort(arr):#aMAL 
    """Bubble sort implementation for PrecisionFloat"""
    n = len(arr)
    arr_copy = arr[:]
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
    return arr_copy


def merge_sort(arr): #Hani
    """Merge sort implementation for PrecisionFloat"""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Merge the sorted halves
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


# Performance Testing
if __name__ == "__main__":
    import time
    import random
    import matplotlib.pyplot as plt
    
    print("Sorting Algorithm Performance with PrecisionFloat")
    print("=" * 60)
    
    sizes = [10, 50, 100, 300, 500, 700, 1000]
    bubble_times = []
    merge_times = []
    
    for size in sizes:
        # Generate random PrecisionFloat list
        test_list = [PrecisionFloat(random.uniform(0, 100)) for _ in range(size)]
        
        # Test Bubble Sort
        start = time.time()
        bubble_sorted = bubble_sort(test_list)
        bubble_time = time.time() - start
        bubble_times.append(bubble_time)
        
        # Test Merge Sort
        start = time.time()
        merge_sorted = merge_sort(test_list)
        merge_time = time.time() - start
        merge_times.append(merge_time)
        
        print(f"Size {size:4d}: Bubble={bubble_time:.6f}s, Merge={merge_time:.6f}s")
    
    # Plot performance comparison #AMAL
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, bubble_times, marker='o', linewidth=2, markersize=8, label='Bubble Sort O(nÂ²)')
    plt.plot(sizes, merge_times, marker='s', linewidth=2, markersize=8, label='Merge Sort O(n log n)')
    plt.xlabel('List Size (n)', fontsize=12)
    plt.ylabel('Time (seconds)', fontsize=12)
    plt.title('Sorting Algorithm Performance Comparison\nwith PrecisionFloat Type (Log Scale)', fontsize=14, fontweight='bold')
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3, which='both')
    plt.tight_layout()
    plt.show()
    
    # Verify correctness with small example #srijana
    print("\n" + "=" * 60)
    print("Correctness Test:")
    test = [PrecisionFloat("3.5"), PrecisionFloat("1.2"), PrecisionFloat("2.8"), 
            PrecisionFloat("0.5"), PrecisionFloat("4.1")]
    print(f"Original: {[str(x) for x in test]}")
    print(f"Bubble:   {[str(x) for x in bubble_sort(test)]}")
    print(f"Merge:    {[str(x) for x in merge_sort(test)]}")
