package com.corejava.math;

import java.util.Scanner;

/**
 * Prints all factors of a number.
 */
public class Factor {
    public static void printFactors(int n) {
        int val = Math.abs(n);
        for (int i = 1; i <= val; i++) {
            if (val % i == 0) {
                System.out.println("factor is: " + i);
            }
        }
    }

    public static void main(String[] ar) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number to find factors : ");
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            printFactors(n);
        } else {
            System.out.println("Invalid input.");
        }
        sc.close();
    }
}
