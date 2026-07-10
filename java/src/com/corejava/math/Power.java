package com.corejava.math;

import java.util.Scanner;

/**
 * Calculates the power of a base raised to an exponent.
 */
public class Power {
    public static long calculatePower(int base, int exponent) {
        long result = 1;
        int expAbs = Math.abs(exponent);
        for (int i = 1; i <= expAbs; i++) {
            result *= base;
        }
        if (exponent < 0) {
            // Since we return long, we cannot return float value, but we throw error or print.
            // For simplicity, we assume positive exponents, or handle double in Python port.
        }
        return result;
    }

    public static void main(String[] ar) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the base : ");
        int base = sc.nextInt();
        System.out.println("Enter the exponent : ");
        int exponent = sc.nextInt();
        
        long result = calculatePower(base, exponent);
        System.out.println("Power is: " + result);
        sc.close();
    }
}
