package com.corejava.string;

import java.util.Scanner;

/**
 * Counts vowels, consonants, digits, spaces, and special characters in a string.
 */
public class Count {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter sentence : ");
        String s = sc.nextLine();
        if (s == null) {
            System.out.println("Invalid string.");
            sc.close();
            return;
        }

        int vowels = 0, consonants = 0, digits = 0, spaces = 0, specialCharacters = 0;
        char[] str = s.toCharArray();
        for (char ch : str) {
            if ("aeiouAEIOU".indexOf(ch) != -1) {
                vowels++;
            } else if ((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z')) {
                consonants++;
            } else if (ch >= '0' && ch <= '9') {
                digits++;
            } else if (ch == ' ') {
                spaces++;
            } else {
                specialCharacters++;
            }
        }
        System.out.println("Vowels = " + vowels);
        System.out.println("Consonants = " + consonants);
        System.out.println("Digits = " + digits);
        System.out.println("White spaces = " + spaces);
        System.out.println("Special characters = " + specialCharacters);
        sc.close();
    }
}
