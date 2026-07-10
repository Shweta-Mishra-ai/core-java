package com.corejava.math;

import java.util.Scanner;

/**
 * Checks if a number is a Happy number.
 * A Happy number is defined by a process where replacing the number by the sum of the squares of its digits
 * eventually leads to 1. If the process loops endlessly in a cycle that excludes 1, it is not a Happy number (leads to 4).
 */
public class HappyNumber {
    public static int getSumOfSquares(int num) {
        int sum = 0;
        while (num > 0) {
            int rem = num % 10;
            sum += rem * rem;
            num /= 10;
        }
        return sum;
    }

    public static boolean isHappy(int num) {
        if (num <= 0) {
            return false;
        }
        int result = num;
        while (result != 1 && result != 4) {
            result = getSumOfSquares(result);
        }
        return result == 1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number : ");
        if (sc.hasNextInt()) {
            int num = sc.nextInt();
            if (isHappy(num)) {
                System.out.println(num + " is a happy number");
            } else {
                System.out.println(num + " is not a happy number");
            }
        } else {
            System.out.println("Invalid input. Please enter an integer.");
        }
        sc.close();
    }
}
