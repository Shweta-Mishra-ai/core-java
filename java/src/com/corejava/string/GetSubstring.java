package com.corejava.string;

import java.util.Scanner;

/**
 * Safely extracts a substring from a string.
 */
public class GetSubstring {
    public static String getSub(String str, int start, int end) {
        if (str == null || start < 0 || end > str.length() || start > end) {
            return "Invalid index parameters";
        }
        return str.substring(start, end);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the string: ");
        String str = sc.next();
        System.out.print("Enter start index: ");
        int startIndex = sc.nextInt();
        System.out.print("Enter end index: ");
        int endIndex = sc.nextInt();
        System.out.print("substring is: " + getSub(str, startIndex, endIndex));
        sc.close();
    }
}
