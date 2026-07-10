package com.corejava.geometry;

import java.util.Scanner;

/**
 * Calculates area and perimeter of a triangle.
 */
public class Tria {
    public static void main(String[] ar) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter side length (base), breadth (height), and side height of triangle : ");
        if (sc.hasNextFloat()) {
            float l = sc.nextFloat();
            float b = sc.nextFloat();
            float h = sc.nextFloat();
            if (l < 0 || b < 0 || h < 0) {
                System.out.println("Dimensions cannot be negative.");
            } else {
                float a = (l * b) * 0.5f;
                System.out.println("Area is:" + a);
                float p = l + b + h;
                System.out.println("Perimeter is:" + p);
            }
        } else {
            System.out.println("Invalid input.");
        }
        sc.close();
    }
}
