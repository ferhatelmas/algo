package page27.q2619;

import java.util.Scanner;

// java: a bit slow for this problem
public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), sum = 0,
        ns[] = new int[n];

    for(int i=0; i<n; i++) {
      ns[i] = in.nextInt();
      sum += ns[i];
    }

    if(sum%2 == 0) {
      int c = 0;
      for (int i = 0; i < n; i++) {
        sum -= ns[i];
        c += ns[i];
        if (sum == c) {
          System.out.println(i + 1);
          return;
        } else if (sum < c)
          break;
      }
    }
    System.out.println(-1);
  }
}
