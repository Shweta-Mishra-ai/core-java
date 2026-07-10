package com.corejava.oop;

import java.util.Scanner;

/**
 * Calculates Simple Interest based on Principal, Rate, and Time.
 */
public class MyClass {
    public static double getSimpleInterest(double p, double r, double t) {
        if (p < 0 || r < 0 || t < 0) {
            throw new IllegalArgumentException("Inputs cannot be negative.");
        }
        return (p * r * t) / 100.0;
    }

    public static void main(String[] ar) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the principal, rate, and time : ");
        if (sc.hasNextFloat()) {
            float p = sc.nextFloat();
            float r = sc.nextFloat();
            float t = sc.nextFloat();
            try {
                double si = getSimpleInterest(p, r, t);
                System.out.println("simple interst is:" + si);
            } catch (IllegalArgumentException ex) {
                System.out.println(ex.getMessage());
            }
        } else {
            System.out.println("Invalid input.");
        }
        sc.close();
    }
}
