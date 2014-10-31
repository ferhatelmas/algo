package page10.q973;

import java.util.Arrays;
import java.util.Scanner;

// Java is again slow for this problem
public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), ns[] = new int[101];
    Arrays.fill(ns, 0);

    for(int i=0; i<n; i++) ns[in.nextInt()]++;

    StringBuilder sb = new StringBuilder();
    for(int i=1; i<101; i++)
      for(int j=ns[i]; j>0; j--)
        sb.append(' ').append(i);

    System.out.println(sb.substring(1));
  }
}
