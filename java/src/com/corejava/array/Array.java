package com.corejava.array;

import java.util.Scanner;

/**
 * Computes sum and average of input array elements.
 */
public class Array {
    public static void main(String[] ar) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter array size : ");
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            if (n <= 0) {
                System.out.println("Array size must be greater than zero.");
                sc.close();
                return;
            }
            int[] a = new int[n];
            int sum = 0;
            System.out.println("enter array elements : ");
            for (int i = 0; i < n; i++) {
                if (sc.hasNextInt()) {
                    a[i] = sc.nextInt();
                    sum += a[i];
                }
            }
            double avg = (double) sum / n;
            System.out.println("total is=" + sum);
            System.out.println("average is=" + avg);
        } else {
            System.out.println("Invalid input.");
        }
        sc.close();
    }
}
