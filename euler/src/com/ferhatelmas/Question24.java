package com.ferhatelmas;

public class Question24 {

    private static int cnt = 0;

    public  static void perm(String s) { perm("", s); }

    private static void perm(String prefix, String s) {
        int N = s.length();
        if (N == 0){
            cnt++;
            if(cnt == 1000000) System.out.println(prefix);
        } else {
            for (int i = 0; i < N; i++)
               perm(prefix + s.charAt(i), s.substring(0, i) + s.substring(i+1, N));
        }

    }

    private static void swap(char[] a, int i, int j) {
        char c;
        c = a[i]; a[i] = a[j]; a[j] = c;
    }

    public static void main(String[] args) {

       String elements = "0123456789";
       perm(elements);
    }
}
