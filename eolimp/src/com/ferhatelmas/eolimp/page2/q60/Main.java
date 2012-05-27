package com.ferhatelmas.eolimp.page2.q60;

import java.util.Locale;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        in.useLocale(new Locale("US"));
        int n = in.nextInt();

        double x1 = in.nextDouble(), y1 = in.nextDouble(), px = x1, py = y1;

        double area = 0;
        for(int i=0; i<n-1; i++) {
            double x = in.nextDouble(), y = in.nextDouble();
            area += px*y - py*x;
            px = x;
            py = y;
        }

        area += px*y1 - py*x1;
        System.out.format(Locale.US, "%.3f\n", Math.abs(area/2));

    }

}
