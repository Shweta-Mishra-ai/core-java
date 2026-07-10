package com.corejava.string;

import java.util.Scanner;

/**
 * Checks if a number is a palindrome number.
 */
public class PalindromeNum {
    public static boolean isPalindromeNumber(int number) {
        int temp = Math.abs(number);
        int rev = 0;
        while (temp > 0) {
            int lastDigit = temp % 10;
            rev = (rev * 10) + lastDigit;
            temp /= 10;
        }
        return rev == Math.abs(number);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number to check palindrome: ");
        if (sc.hasNextInt()) {
            int inputNumber = sc.nextInt();
            if (isPalindromeNumber(inputNumber)) {
                System.out.println(inputNumber + " is a palindrome ");
            } else {
                System.out.println(inputNumber + " is not a palindrome");
            }
        } else {
            System.out.println("Invalid number.");
        }
        sc.close();
    }
}
