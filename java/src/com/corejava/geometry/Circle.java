package com.corejava.geometry;

import java.util.Scanner;

/**
 * Calculates area and circumference of a circle.
 */
public class Circle {
    public static void main(String[] ar) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Radius of circle : ");
        if (sc.hasNextFloat()) {
            float r = sc.nextFloat();
            if (r < 0) {
                System.out.println("Radius cannot be negative.");
            } else {
                double a = Math.PI * r * r;
                System.out.println("Area is:" + a);
                double c = 2 * Math.PI * r;
                System.out.println("Circumference is:" + c);
            }
        } else {
            System.out.println("Invalid input.");
        }
        sc.close();
    }
}
