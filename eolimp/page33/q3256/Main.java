package page33.q3256;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), ns[] = new int[n],
        min = Integer.MAX_VALUE, sum = 0;

    for(int i=0; i<n; i++) {
      sum += in.nextInt();
      ns[i] = sum;
    }

    for(int i=0; i<n; i++)
      for(int j=i; j<n; j++)
        min = Math.min(min, ns[j] - (i == 0 ? 0 : ns[i-1]));

    System.out.println(min);
  }
}
