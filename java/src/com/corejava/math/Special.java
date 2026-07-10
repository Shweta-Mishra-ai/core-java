package com.corejava.math;

import java.util.Scanner;

/**
 * Checks if a number is a Special number (Krishnamurthy number).
 * A Special number is a number where the sum of factorials of its digits equals the number itself.
 * Example: 145 = 1! + 4! + 5! = 1 + 24 + 120 = 145.
 */
public class Special {
    public static long factorial(int d) {
        long fact = 1;
        for (int a = 1; a <= d; a++) {
            fact *= a;
        }
        return fact;
    }

    public static boolean isSpecial(int n) {
        if (n <= 0) {
            return false;
        }
        int temp = n;
        long sum = 0;
        while (temp != 0) {
            int d = temp % 10;
            sum += factorial(d);
            temp /= 10;
        }
        return sum == n;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number : ");
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            if (isSpecial(n)) {
                System.out.println("Special Number");
            } else {
                System.out.println("Not a Special Number");
            }
        } else {
            System.out.println("Invalid input.");
        }
        sc.close();
    }
}
