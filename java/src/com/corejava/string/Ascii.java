package com.corejava.string;

import java.util.Scanner;

/**
 * Returns the ASCII value of a character.
 */
public class Ascii {
    public static int getAscii(char ch) {
        return (int) ch;
    }

    public static void main(String[] ar) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the character : ");
        String input = sc.next();
        if (input != null && !input.isEmpty()) {
            char ch = input.charAt(0);
            System.out.println("ascii is: " + getAscii(ch));
        } else {
            System.out.println("Invalid input.");
        }
        sc.close();
    }
}
