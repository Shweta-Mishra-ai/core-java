package com.corejava.math;

import java.util.Scanner;

/**
 * Calculates the area and perimeter of a square.
 */
public class Squa {
    public static void main(String[] ar) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter side of square : ");
        if (sc.hasNextInt()) {
            int s = sc.nextInt();
            if (s < 0) {
                System.out.println("Side length cannot be negative.");
            } else {
                int a = s * s;
                System.out.println("Area is: " + a);
                int p = 4 * s;
                System.out.println("Perimeter is: " + p);
            }
        } else {
            System.out.println("Invalid input.");
        }
        sc.close();
    }
}
