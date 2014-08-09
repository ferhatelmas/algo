package page15.q1462;

import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    Integer ns[] = new Integer[n];
    for(int i=0; i<n; i++) ns[i] = in.nextInt();
    Arrays.sort(ns, new Comparator<Integer>() {
      @Override
      public int compare(Integer o1, Integer o2) {
        int r = o1 % 10 - o2 % 10;
        return r != 0 ? r : o1 - o2;
      }
    });
    StringBuilder sb = new StringBuilder();
    for(int i : ns) sb.append(' ').append(i);
    System.out.println(sb.substring(1));
  }
}
