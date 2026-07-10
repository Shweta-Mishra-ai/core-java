package com.corejava.string;

import java.util.Scanner;

/**
 * Converts lowercase characters to uppercase, and uppercase to lowercase.
 */
public class LowerToUpper {
    public static String toggleCase(String str) {
        if (str == null) return null;
        char[] ch = str.toCharArray();
        StringBuilder sb = new StringBuilder();
        for (char c : ch) {
            if (c >= 'a' && c <= 'z') {
                sb.append((char) (c - 32));
            } else if (c >= 'A' && c <= 'Z') {
                sb.append((char) (c + 32));
            } else {
                sb.append(c);
            }
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter String : ");
        String str = sc.nextLine();
        System.out.print(toggleCase(str));
        sc.close();
    }
}
