package com.corejava.string;

import java.util.Scanner;

/**
 * Demonstrates the use of the standard String substring() method.
 */
public class Substring {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the string: ");
        String str = sc.next();
        System.out.print("Enter start index: ");
        int startIndex = sc.nextInt();
        System.out.print("Enter end index: ");
        int endIndex = sc.nextInt();

        if (startIndex < 0 || endIndex > str.length() || startIndex > endIndex) {
            System.out.println("Invalid indices.");
        } else {
            String temp = str.substring(startIndex, endIndex);
            System.out.println("Substring is: " + temp);
        }
        sc.close();
    }
}
