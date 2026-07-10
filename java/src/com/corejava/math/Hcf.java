package com.corejava.math;

import java.util.Scanner;

/**
 * Calculates the HCF (Highest Common Factor) / GCD of two integers.
 */
public class Hcf {
    public static int gcd(int u, int v) {
        u = Math.abs(u);
        v = Math.abs(v);
        while (u != 0) {
            int r = v % u;
            v = u;
            u = r;
        }
        return v;
    }

    public static void main(String[] ar) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter two numbers : ");
        if (sc.hasNextInt()) {
            int u = sc.nextInt();
            if (sc.hasNextInt()) {
                int v = sc.nextInt();
                int n = gcd(u, v);
                System.out.println("HCF is: " + n);
            }
        } else {
            System.out.println("Invalid input.");
        }
        sc.close();
    }
}
