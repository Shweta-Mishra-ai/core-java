package com.corejava.array;

import java.util.Scanner;

/**
 * Inspects prime numbers in a user-defined array.
 */
public class ArrayLen {
    public static boolean isPrime(int val) {
        if (val <= 1) return false;
        for (int i = 2; i <= Math.sqrt(val); i++) {
            if (val % i == 0) return false;
        }
        return true;
    }

    public static void main(String[] ar) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter array size : ");
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            if (n <= 0) {
                System.out.println("Size must be positive.");
                sc.close();
                return;
            }
            int[] a = new int[n];
            System.out.println("Enter array elements : ");
            for (int i = 0; i < n; i++) {
                if (sc.hasNextInt()) {
                    a[i] = sc.nextInt();
                }
            }
            System.out.println("Prime numbers in the array : ");
            for (int val : a) {
                if (isPrime(val)) {
                    System.out.println(val);
                }
            }
        } else {
            System.out.println("Invalid input.");
        }
        sc.close();
    }
}
