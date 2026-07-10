package com.corejava.math;

import java.util.Scanner;

/**
 * Checks if a number is a Disarium number.
 * A Disarium number is a number where the sum of its digits powered to their respective
 * positions is equal to the number itself.
 */
public class Disarium {
    public static boolean isDisarium(int num) {
        if (num < 0) {
            return false; // Disarium numbers are typically positive integers
        }
        int n = num;
        int sum = 0;
        String s = Integer.toString(num);
        int len = s.length();
        while (n > 0) {
            int d = n % 10;
            sum += (int) Math.pow(d, len);
            len--;
            n /= 10;
        }
        return sum == num;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Input a number : ");
        if (sc.hasNextInt()) {
            int num = sc.nextInt();
            if (isDisarium(num)) {
                System.out.println(num + " is a Disarium Number.");
            } else {
                System.out.println(num + " is Not a Disarium Number.");
            }
        } else {
            System.out.println("Invalid input. Please enter an integer.");
        }
        sc.close();
    }
}
