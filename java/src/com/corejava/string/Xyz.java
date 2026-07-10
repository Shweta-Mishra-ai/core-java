package com.corejava.string;

import java.util.Scanner;

/**
 * Checks if the string contains any alphabetical characters.
 */
public class Xyz {
    public static String checkAlphabets(String str) {
        if (str == null || str.isEmpty()) {
            return "string not found";
        }
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            if ((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z')) {
                return str;
            }
        }
        return "string not found";
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter String : ");
        String str = sc.nextLine();
        System.out.println(checkAlphabets(str));
        sc.close();
    }
}
