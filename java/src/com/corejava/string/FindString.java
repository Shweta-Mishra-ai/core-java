package com.corejava.string;

import java.util.Scanner;

/**
 * Checks if string1 is a substring of string2.
 */
public class FindString {
    public static boolean isSubstring(String string1, String string2) {
        if (string1 == null || string2 == null) {
            return false;
        }
        return string2.contains(string1);
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Please enter first String: ");
        String string1 = input.next();
        System.out.print("Please enter second String: ");
        String string2 = input.next();
        if (isSubstring(string1, string2)) {
            System.out.println("The first string is a substring of the second.");
        } else {
            System.out.println("The first string is NOT a substring of the second.");
        }
        input.close();
    }
}
