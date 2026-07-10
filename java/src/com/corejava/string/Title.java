package com.corejava.string;

import java.util.Scanner;

/**
 * Converts a sentence to title case using a scanner to parse words.
 */
public class Title {
    public static String toTitleCase(String line) {
        if (line == null || line.trim().isEmpty()) {
            return "";
        }
        StringBuilder titleCase = new StringBuilder();
        Scanner wordScan = new Scanner(line);
        while (wordScan.hasNext()) {
            String word = wordScan.next();
            if (!word.isEmpty()) {
                titleCase.append(Character.toUpperCase(word.charAt(0)))
                         .append(word.substring(1).toLowerCase())
                         .append(" ");
            }
        }
        wordScan.close();
        return titleCase.toString().trim();
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("Input a Sentence: ");
        String line = in.nextLine();
        System.out.println(toTitleCase(line));
        in.close();
    }
}
