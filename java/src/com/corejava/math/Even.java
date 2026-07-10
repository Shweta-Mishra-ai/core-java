package com.corejava.math;

/**
 * Computes the sum of even and odd integers in range [12, 72]
 * and displays the final results.
 */
public class Even {
    public static void main(String[] ar) {
        int evenSum = 0;
        int oddSum = 0;
        for (int i = 12; i <= 72; i++) {
            if (i % 2 == 0) {
                evenSum += i;
            } else {
                oddSum += i;
            }
        }
        System.out.println("The final sum of even numbers is = " + evenSum);
        System.out.println("The final sum of odd numbers is = " + oddSum);
    }
}
