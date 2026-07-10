package com.corejava.geometry;

import java.util.Scanner;

/**
 * Calculates area and perimeter of a rectangle.
 */
public class Rect {
    public static void main(String[] ar) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter length and breadth of Rectangle : ");
        if (sc.hasNextInt()) {
            int l = sc.nextInt();
            if (sc.hasNextInt()) {
                int b = sc.nextInt();
                if (l < 0 || b < 0) {
                    System.out.println("Dimensions cannot be negative.");
                } else {
                    int a = l * b;
                    System.out.println("Area is:" + a);
                    int p = 2 * (l + b);
                    System.out.println("Perimeter is:" + p);
                }
            }
        } else {
            System.out.println("Invalid input.");
        }
        sc.close();
    }
}
