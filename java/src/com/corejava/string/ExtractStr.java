package com.corejava.string;

import java.util.Scanner;

/**
 * Extracts a substring between two indices using getChars().
 */
public class ExtractStr {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a string : ");
        String inputString = scanner.nextLine();
        System.out.println("Enter the first index of the substring : ");
        int startIndex = scanner.nextInt();
        System.out.println("Enter the second index of the substring : ");
        int endIndex = scanner.nextInt();

        if (startIndex < 0 || endIndex >= inputString.length() || startIndex > endIndex) {
            System.out.println("Invalid indices for substring extraction.");
        } else {
            char[] ch = new char[endIndex - startIndex + 1];
            inputString.getChars(startIndex, endIndex + 1, ch, 0);
            System.out.println("Output : " + String.valueOf(ch));
        }
        scanner.close();
    }
}
