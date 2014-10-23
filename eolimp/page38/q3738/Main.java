package page38.q3738;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), ns[] = new int[n];

    for(int i=0; i<n; i++) ns[i] = in.nextInt();
    Arrays.sort(ns);

    StringBuilder sb = new StringBuilder();
    for(int i : ns) sb.append(' ').append(i);
    System.out.println(sb.substring(1));
  }
}
