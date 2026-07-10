package com.corejava.math;

import java.util.Scanner;

/**
 * Checks if a number is a Magic number.
 * A Magic number is a number in which the eventual sum of digits (recursively) is equal to 1.
 */
public class MagicNumber {
    public static boolean isMagic(int n) {
        int num = Math.abs(n);
        while (num > 9) {
            int sum = 0;
            while (num != 0) {
                sum += num % 10;
                num /= 10;
            }
            num = sum;
        }
        return num == 1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number to be checked : ");
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            if (isMagic(n)) {
                System.out.println(n + " is a Magic Number.");
            } else {
                System.out.println(n + " is not a Magic Number.");
            }
        } else {
            System.out.println("Invalid input.");
        }
        sc.close();
    }
}
