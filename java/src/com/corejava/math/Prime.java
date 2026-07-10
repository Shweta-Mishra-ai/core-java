package com.corejava.math;

import java.util.Scanner;

/**
 * Checks if a number is a prime number.
 */
public class Prime {
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
        System.out.println("Enter the number : ");
        if (sc.hasNextInt()) {
            int num = sc.nextInt();
            if (isPrime(num)) {
                System.out.println("yes its prime ");
            } else {
                System.out.println("no its not prime");
            }
        } else {
            System.out.println("Invalid input.");
        }
        sc.close();
    }
}
