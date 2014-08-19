package page15.q1457;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), m = in.nextInt(),
        ns[] = new int[n];

    for(int i=0; i<n; i++) ns[i] = in.nextInt();
    for(int i=1; i<n; i++) {
      int j = i, k = ns[i];
      while(j > 0 && ns[j-1] > ns[j]) {
        if(k + ns[j-1] > m) {
          System.out.println("No");
          return;
        }
        ns[j] = ns[j-1];
        j--;
      }
      ns[j] = k;
    }
    System.out.println("Yes");
  }
}
