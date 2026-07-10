package com.corejava.file;

import java.io.File;
import java.io.IOException;
import java.util.Scanner;

/**
 * Safe directory creator.
 */
public class Folder {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter the Foldername : ");
        String fname = sc.nextLine();
        if (fname == null || fname.trim().isEmpty()) {
            System.out.println("Invalid folder name.");
            sc.close();
            return;
        }
        try {
            File f = new File(fname.trim());
            if (!f.exists()) {
                if (f.mkdir()) {
                    System.out.println("Folder created successfully.");
                } else {
                    System.out.println("Failed to create folder.");
                }
            } else {
                System.out.println("Folder already exists.");
            }
        } catch (SecurityException ex) {
            System.out.println("Permission denied: " + ex.getMessage());
        }
        sc.close();
    }
}
