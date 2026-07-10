package com.corejava.math;

import java.util.Scanner;

/**
 * Checks if a number is a Niven (Harshad) number.
 * A Niven number is an integer that is divisible by the sum of its digits.
 */
public class Niven {
    public static boolean isNiven(int num) {
        if (num <= 0) {
            return false;
        }
        int x = num;
        int sum = 0;
        while (x > 0) {
            sum += x % 10;
            x /= 10;
        }
        if (sum == 0) {
            return false; // Avoid division by zero
        }
        return num % sum == 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Input a number : ");
        if (sc.hasNextInt()) {
            int num = sc.nextInt();
            if (isNiven(num)) {
                System.out.println(num + " is a Niven Number.");
            } else {
                System.out.println(num + " is not a Niven Number.");
            }
        } else {
            System.out.println("Invalid input.");
        }
        sc.close();
    }
}
