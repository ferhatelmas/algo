package page51.q5098;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int t = in.nextInt(), ns[] = new int[t];

    StringBuilder sb = new StringBuilder();
    for(int i=0; i<t; i++) {
      int n = in.nextInt(), j = i;

      while(j > 0 && ns[j-1] > n) {
        ns[j] = ns[j-1];
        j--;
      }
      ns[j] = n;
      sb.append(' ')
        .append(i%2 == 0 ? ns[i/2] : Math.min(ns[i/2], ns[i/2+1]));
    }
    System.out.println(sb.substring(1));
  }
}
