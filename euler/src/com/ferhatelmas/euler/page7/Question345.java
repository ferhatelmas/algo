package com.ferhatelmas.euler.page7;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.HashMap;
import java.util.Scanner;

public class Question345 {

    private static int N = 15;
    private static HashMap<String, Integer> cache = new HashMap<String, Integer>();

    public static void main(String[] args) throws IOException {

        int[][] matrix = new int[N][N];
        Scanner sc = new Scanner(new FileInputStream("matrix"));

        for(int i=0; i<N; i++) {
            for(int j=0; j<N; j++) {
                matrix[i][j] = sc.nextInt();
            }
        }

        int sum = sum(matrix, new boolean[N], 0);
        System.out.println(sum);
    }

    private static int sum(int[][] m, boolean[] c, int i) {
        if(i == N) {
            return 0;
        }

        String hash = getHash(c, i);
        if(cache.containsKey(hash)) return cache.get(hash);

        int max=-1, tmp;
        for(int j=0; j<N; j++) {
            if(!c[j]) {
                c[j] = true;
                tmp = m[i][j] + sum(m, c, i+1);
                if(tmp > max) max = tmp;
                c[j] = false;
            }
        }

        cache.put(getHash(c, i), max);
        return max;
    }

    private static String getHash(boolean[] b, int k) {
        StringBuilder sb = new StringBuilder();
        sb.append(k);
        for(boolean b1 : b) sb.append(b1 ? 'T' : 'F');
        return sb.toString();
    }
}
