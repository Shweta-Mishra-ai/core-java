package com.corejava.math;

/**
 * Demonstrates abstract class implementation and polymorphism.
 */
public abstract class MyAbs {
    public abstract void calc(int a);

    public void myprint() {
        System.out.println("Abstract class print method called");
    }
}

class Shweta extends MyAbs {
    @Override
    public void calc(int a) {
        System.out.println("Square is: " + (a * a));
    }

    @Override
    public void myprint() {
        System.out.println("Shweta implementation of myprint");
    }
}

class Ram extends MyAbs {
    @Override
    public void calc(int a) {
        System.out.println("Cube is: " + (a * a * a));
    }

    public static void main(String[] ar) {
        Shweta s = new Shweta();
        Ram r = new Ram();
        s.myprint();
        s.calc(4);
        r.myprint();
        r.calc(4);
    }
}
