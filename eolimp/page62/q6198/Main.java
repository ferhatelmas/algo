package page62.q6198;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    long n1[] = new long[n], n2[] = new long[n], sum = 0;

    for(int i=0; i<n; i++) n1[i] = in.nextInt();
    for(int i=0; i<n; i++) n2[i] = in.nextInt();
    Arrays.sort(n1);
    Arrays.sort(n2);
    for(int i=0; i<n; i++) sum += n1[i] * n2[n-i-1];
    System.out.println(sum);
  }
}
