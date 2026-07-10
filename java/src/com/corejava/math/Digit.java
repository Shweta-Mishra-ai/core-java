package com.corejava.math;

import java.util.Scanner;

/**
 * Calculates the sum of digits of a number.
 */
public class Digit {
    public static int sumDigits(int num) {
        int sum = 0;
        int temp = Math.abs(num);
        while (temp > 0) {
            sum += temp % 10;
            temp /= 10;
        }
        return sum;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number: ");
        if (sc.hasNextInt()) {
            int m = sc.nextInt();
            System.out.println("Sum of Digits: " + sumDigits(m));
        } else {
            System.out.println("Invalid input.");
        }
        sc.close();
    }
}
