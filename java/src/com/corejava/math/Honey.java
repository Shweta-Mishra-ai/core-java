package com.corejava.math;

import java.util.Scanner;

/**
 * Simple calculation of total and average of three marks.
 */
public class Honey {
    public static void main(String[] ar) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter three marks : ");
        if (sc.hasNextInt()) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();
            int sum = a + b + c;
            double avg = (double) sum / 3.0;
            System.out.println("Total is: " + sum);
            System.out.println("Average is: " + avg);
        } else {
            System.out.println("Invalid input.");
        }
        sc.close();
    }
}
