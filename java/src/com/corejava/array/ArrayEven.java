package com.corejava.array;

/**
 * Filters even and odd numbers from an array, computing their counts and values.
 */
public class ArrayEven {
    public static void main(String[] ar) {
        int[] a = {13, 7, 6, 91, 67};
        int evenCount = 0;
        int oddCount = 0;
        for (int val : a) {
            if (val % 2 == 0) {
                System.out.println("Even element: " + val);
                evenCount++;
            } else {
                System.out.println("Odd element: " + val);
                oddCount++;
            }
        }
        System.out.println("Total even count: " + evenCount);
        System.out.println("Total odd count: " + oddCount);
    }
}
