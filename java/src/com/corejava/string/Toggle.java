package com.corejava.string;

import java.util.Scanner;

/**
 * Toggles the casing of all alphabetic characters in a string.
 */
public class Toggle {
    public static String toggleString(String str) {
        if (str == null) return "";
        char[] a = str.toCharArray();
        for (int c = 0; c < a.length; c++) {
            if (a[c] >= 'A' && a[c] <= 'Z') {
                a[c] = (char) (a[c] + 32);
            } else if (a[c] >= 'a' && a[c] <= 'z') {
                a[c] = (char) (a[c] - 32);
            }
        }
        return String.valueOf(a);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the string to be toggled : ");
        String str = sc.nextLine();
        System.out.println("The toggled string is :-");
        System.out.println(toggleString(str));
        sc.close();
    }
}
