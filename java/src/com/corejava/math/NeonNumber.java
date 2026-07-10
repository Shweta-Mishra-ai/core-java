package com.corejava.math;

import java.util.Scanner;

/**
 * Checks if a number is a Neon number.
 * A Neon number is a number where the sum of digits of its square is equal to the number itself.
 */
public class NeonNumber {
    public static boolean isNeon(int n) {
        if (n < 0) {
            return false;
        }
        int square = n * n;
        int sum = 0;
        while (square > 0) {
            sum += square % 10;
            square /= 10;
        }
        return sum == n;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number: ");
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            if (isNeon(n)) {
                System.out.println("Its a Neon number.");
            } else {
                System.out.println("Its not a Neon number.");
            }
        } else {
            System.out.println("Invalid input.");
        }
        sc.close();
    }
}
