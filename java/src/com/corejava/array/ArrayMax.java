package com.corejava.array;

import java.util.Scanner;

/**
 * Finds the largest and smallest numbers along with their positions in an array.
 */
public class ArrayMax {
    public static void main(String[] ar) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter array size : ");
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            if (n <= 0) {
                System.out.println("Array size must be positive.");
                sc.close();
                return;
            }
            int[] a = new int[n];
            System.out.println("enter array elements : ");
            for (int i = 0; i < n; i++) {
                if (sc.hasNextInt()) {
                    a[i] = sc.nextInt();
                }
            }
            int max = a[0];
            int min = a[0];
            int maxPos = 0;
            int minPos = 0;
            for (int i = 0; i < n; i++) {
                if (max < a[i]) {
                    max = a[i];
                    maxPos = i;
                }
                if (min > a[i]) {
                    min = a[i];
                    minPos = i;
                }
            }
            System.out.println("largert numbers is=" + max);
            System.out.println("Smallest numbers is=" + min);
            System.out.println("largert numbers position is=" + maxPos);
            System.out.println("Smallest numbers position is=" + minPos);
        } else {
            System.out.println("Invalid input.");
        }
        sc.close();
    }
}
