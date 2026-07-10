package com.corejava.string;

import java.util.Scanner;

/**
 * Searches for a substring within a string (alternative interface).
 */
public class FindSub {
    public static boolean isSub(String str, String str1) {
        if (str == null || str1 == null) {
            return false;
        }
        return str.contains(str1);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the string : ");
        String str = sc.next();
        System.out.println("Enter the string to find : ");
        String str1 = sc.next();
        if (isSub(str, str1)) {
            System.out.println("yes");
        } else {
            System.out.println("No");
        }
        sc.close();
    }
}
