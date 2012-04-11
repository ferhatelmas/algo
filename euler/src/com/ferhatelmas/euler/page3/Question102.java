package com.ferhatelmas.euler.page3;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Question102 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new FileReader("triangles.txt"));
        int cnt = 0;
        String line;
        while((line=br.readLine()) != null) {
            String[] points = line.split(",");
            if(isIn(points)) cnt++;
        }
        br.close();

        System.out.println(cnt);
    }
    
    private static boolean isIn(String[] s) {
        int[] p = new int[s.length];
        
        for(int i=0; i<p.length; i++) {
            p[i] = Integer.parseInt(s[i]);
        }

        return calcArea(p, true) == calcArea(p, false);
    }
    
    private static double calcArea(int[] p, boolean flag) {
        double area = 0;
        if(flag) {
            area = 0.5 * Math.abs((p[0]-p[4])*(p[3]-p[1]) - (p[0]-p[2])*(p[5]-p[1]));
        } else {
            area += 0.5 * Math.abs(p[0]*p[3] - p[2]*p[1]);
            area += 0.5 * Math.abs(p[0]*p[5] - p[4]*p[1]);
            area += 0.5 * Math.abs(p[2]*p[5] - p[4]*p[3]);
        }
        return area;
    }
    
}
