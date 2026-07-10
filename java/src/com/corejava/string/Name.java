package com.corejava.string;

import java.util.Scanner;

/**
 * Checks if a string (name) starts, ends, or contains character 'a'.
 */
public class Name {
    public static String analyzeName(String str) {
        if (str == null || str.trim().isEmpty()) {
            return "Empty name";
        }
        String clean = str.trim().toLowerCase();
        boolean startsWithA = clean.startsWith("a");
        boolean endsWithA = clean.endsWith("a");

        if (startsWithA && endsWithA) {
            return "Name starts and ends with a";
        } else if (startsWithA) {
            return "Name starts with a";
        } else if (endsWithA) {
            return "Name ends with a";
        } else if (clean.contains("a")) {
            return "Anywhere a";
        } else {
            return "No 'a' found in the name";
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter String : ");
        String str = sc.nextLine();
        System.out.println(analyzeName(str));
        sc.close();
    }
}
