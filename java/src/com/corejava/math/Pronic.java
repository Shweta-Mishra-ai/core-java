package com.corejava.math;

import java.util.Scanner;

/**
 * Checks if a number is a Pronic number (oblong number).
 * A Pronic number is a number which is the product of two consecutive integers: n * (n + 1) = number.
 */
public class Pronic {
    public static boolean isPronic(int num) {
        if (num < 0) {
            return false;
        }
        for (int n = 0; n <= Math.sqrt(num); n++) {
            if (n * (n + 1) == num) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] ar) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number : ");
        if (sc.hasNextInt()) {
            int num = sc.nextInt();
            if (isPronic(num)) {
                System.out.println("yes its pronic");
            } else {
                System.out.println("no its not pronic");
            }
        } else {
            System.out.println("Invalid input.");
        }
        sc.close();
    }
}
