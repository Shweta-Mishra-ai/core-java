package com.corejava.string;

import java.util.Scanner;

/**
 * Converts a string to Title Case by traversing indices.
 */
public class TitleCase {
    public static String makeTitleCase(String s) {
        if (s == null || s.isEmpty()) {
            return "";
        }
        StringBuilder str = new StringBuilder();
        boolean capitalizeNext = true;
        for (int i = 0; i < s.length(); i++) {
            char a = s.charAt(i);
            if (a == ' ') {
                str.append(' ');
                capitalizeNext = true;
            } else {
                if (capitalizeNext) {
                    str.append(Character.toUpperCase(a));
                    capitalizeNext = false;
                } else {
                    str.append(Character.toLowerCase(a));
                }
            }
        }
        return str.toString();
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Enter string: ");
        String s = in.nextLine();
        System.out.println(makeTitleCase(s));
        in.close();
    }
}
