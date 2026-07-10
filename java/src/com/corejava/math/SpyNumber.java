package com.corejava.math;

import java.util.Scanner;

/**
 * Checks if a number is a Spy number.
 * A Spy number is a number where the sum of its digits equals the product of its digits.
 */
public class SpyNumber {
    public static boolean isSpy(int no) {
        int pro = 1;
        int sum = 0;
        int temp = Math.abs(no);
        if (temp == 0) {
            return false;
        }
        while (temp != 0) {
            int digit = temp % 10;
            pro *= digit;
            sum += digit;
            temp /= 10;
        }
        return sum == pro;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number to check spy number : ");
        if (sc.hasNextInt()) {
            int no = sc.nextInt();
            if (isSpy(no)) {
                System.out.println("Spy Number");
            } else {
                System.out.println("Not Spy Number");
            }
        } else {
            System.out.println("Invalid input.");
        }
        sc.close();
    }
}
