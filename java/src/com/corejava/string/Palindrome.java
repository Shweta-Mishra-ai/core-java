package com.corejava.string;

import java.util.Scanner;

/**
 * Checks if a string is a palindrome.
 */
public class Palindrome {
    public static boolean isPalindrome(String str) {
        if (str == null) return false;
        String clean = str.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        int len = clean.length();
        for (int i = 0; i < len / 2; i++) {
            if (clean.charAt(i) != clean.charAt(len - i - 1)) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a string : ");
        String str = sc.nextLine();
        if (isPalindrome(str)) {
            System.out.println(str + " is a palindrome.");
        } else {
            System.out.println(str + " is not a palindrome.");
        }
        sc.close();
    }
}
