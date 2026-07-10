package com.corejava.math;

import java.util.Scanner;

/**
 * Checks if a number is a Duck number.
 * A Duck number is a number which has zero in it, but not at the start.
 */
public class Duck {
    public static boolean isDuck(String nstr) {
        if (nstr == null || nstr.isEmpty()) {
            return false;
        }
        // Remove leading spaces
        nstr = nstr.trim();
        if (nstr.startsWith("-") || nstr.startsWith("+")) {
            nstr = nstr.substring(1);
        }
        if (nstr.isEmpty()) {
            return false;
        }
        char f = nstr.charAt(0);
        if (f == '0') {
            return false;
        }
        for (int i = 1; i < nstr.length(); i++) {
            if (nstr.charAt(i) == '0') {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Input a number : ");
        String nstr = sc.nextLine();
        if (isDuck(nstr)) {
            System.out.println("Duck number");
        } else {
            System.out.println("Not a duck number");
        }
        sc.close();
    }
}
