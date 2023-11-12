#include <iostream>
#include <cmath>

int minPRAM(int arr[], int len) {
    int k = log2(len);
    for (int i = 0; i < k; i++) {
        for ( int j = 0; j < len; j += pow(2, i + 1)) {
            //The return type of the pow() function in the cmath library is a double.
            if ( arr[j] > arr[static_cast<int>(j + pow(2, i))] ) {
                int temp = arr[j];
                arr[j] = arr[static_cast<int>(j + pow(2, i))];
                arr[static_cast<int>(j + pow(2, i))] = temp;
            }
        }
    }
    return arr[0];
}

int log2(int x) {
    int result = 0;
    while (x > 1) {
        if (x % 2 != 0) {
            // throw std::invalid_argument("Input is not a power of 2");
        }
        x /= 2;
        result++;
    }
    return result;
}

int main() {
    int arr[] = {3, 6, 2, 8, 9, 2, 5, 4, 7};
    int len = sizeof(arr) / sizeof(arr[0]);
    int result = minPRAM(arr, len);
    std::cout << result << std::endl;
    return 0;
}
