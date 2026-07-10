package com.corejava.array;

import java.util.Scanner;

/**
 * Checks if a string array is a palindrome (i.e. characters match from start to end).
 */
public class PalindromeArray {
    public static boolean isPalindrome(String s) {
        if (s == null) return false;
        char[] str = s.toCharArray();
        int n = str.length;
        for (int i = 0; i < n / 2; i++) {
            if (str[i] != str[n - i - 1]) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the string : ");
        String s = sc.nextLine();
        System.out.println("Is the string a palindrome?\n");
        if (isPalindrome(s)) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
        sc.close();
    }
}
