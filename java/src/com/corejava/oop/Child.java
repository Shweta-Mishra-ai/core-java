package com.corejava.oop;

interface NewInterface1 {
    int a = 1000;
    void expend();
}

interface NewInterface2 {
    int a = 2000;
    void expend();
}

/**
 * Demonstrates multiple inheritance of interfaces in Java.
 */
public class Child implements NewInterface1, NewInterface2 {
    @Override
    public void expend() {
        int combined = NewInterface1.a + NewInterface2.a;
        System.out.println("Combined Interface Constants sum: " + combined);
    }

    public static void main(String[] ar) {
        Child c = new Child();
        c.expend();
    }
}
