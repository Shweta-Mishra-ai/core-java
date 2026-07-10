package com.corejava.math;

import java.util.Scanner;

/**
 * Prints all prime numbers in a user-defined range.
 */
public class PrimeRan {
    public static boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] ar) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the start of range : ");
        int start = sc.nextInt();
        System.out.println("Enter the end of range : ");
        int end = sc.nextInt();
        
        System.out.println("Prime numbers in range [" + start + ", " + end + "]:");
        for (int i = start; i <= end; i++) {
            if (isPrime(i)) {
                System.out.print(i + " ");
            }
        }
        System.out.println();
        sc.close();
    }
}
