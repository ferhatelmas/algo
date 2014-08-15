package page14.q1346;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), ns[] = new int[n], sum = 0;
    for(int i=0; i<n; i++) ns[i] = in.nextInt();
    Arrays.sort(ns);
    for(int  i=1; i<n; i++) sum += ns[i];
    System.out.println(sum);
  }
}
