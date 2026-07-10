package com.corejava.geometry;

import java.util.Scanner;

/**
 * Grouped area and perimeter calculations for Triangles and Rectangles.
 */
public class Areas {
    public static float getTriaArea(float l, float b) {
        return (l * b) * 0.5f;
    }

    public static float getTriaPeri(float l, float b, float h) {
        return l + b + h;
    }

    public static float getRectArea(float l, float b) {
        return l * b;
    }

    public static float getRectPeri(float l, float b) {
        return 2 * (l + b);
    }

    public static void main(String[] ar) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter length, breadth, and height of triangle: ");
        if (sc.hasNextFloat()) {
            float l = sc.nextFloat();
            float b = sc.nextFloat();
            float h = sc.nextFloat();

            System.out.println("AreaTria is:" + getTriaArea(l, b));
            System.out.println("PerimeterTria is:" + getTriaPeri(l, b, h));
            System.out.println("AreaRect is:" + getRectArea(l, b));
            System.out.println("PerimeterRect is:" + getRectPeri(l, b));
        } else {
            System.out.println("Invalid input.");
        }
        sc.close();
    }
}
