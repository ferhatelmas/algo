package page14.q1304;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int ns[] = new int[30000], k = 0, n, j;

    while(in.hasNextInt()) {
      j = k;
      n = in.nextInt();
      ns[k++] = n;
      while(j > 0 && ns[j-1] > n) {
        ns[j] = ns[j-1];
        j--;
      }
      ns[j] = n;
      System.out.println(k%2 == 1 ? ns[k/2] : (ns[k/2] + ns[k/2-1]) / 2);
    }
  }
}
