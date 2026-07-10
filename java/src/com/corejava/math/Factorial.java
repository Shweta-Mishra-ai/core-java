package com.corejava.math;

import java.util.Scanner;

/**
 * Calculates the factorial of a number.
 */
public class Factorial {
    public static long calculateFactorial(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("Factorial is not defined for negative numbers.");
        }
        long num = 1;
        for (int i = 1; i <= n; i++) {
            num *= i;
        }
        return num;
    }

    public static void main(String[] ar) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number to find factorial : ");
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            try {
                long fact = calculateFactorial(n);
                System.out.println("Factorial is " + fact);
            } catch (IllegalArgumentException ex) {
                System.out.println(ex.getMessage());
            }
        } else {
            System.out.println("Invalid input.");
        }
        sc.close();
    }
}
