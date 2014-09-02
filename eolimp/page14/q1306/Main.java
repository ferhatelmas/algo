package page14.q1306;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();

    while(n-- > 0) {
      int k = in.nextInt(), t = in.nextInt(),
          ns[] = new int[t];

      String s[] = new String[t];
      for(int i=0; i<t; i++) {
        s[i] = in.next();
        ns[i] = getSortedness(s[i], k);
        if(i > 0) {
          String tmps = s[i];
          int tmpn = ns[i], j = i;
          while(j > 0 && ns[j-1] > tmpn) {
            s[j] = s[j-1];
            ns[j] = ns[j-1];
            j--;
          }
          s[j] = tmps;
          ns[j] = tmpn;
        }
      }

      for(String ss : s) System.out.println(ss);
      if(n > 0) System.out.println();
    }
  }

  private static int getSortedness(String s, int k) {
    int c = 0;
    for(int i=0; i<k-1; i++) {
      for(int j=i+1; j<k; j++) {
        if(s.charAt(i) > s.charAt(j)) c++;
      }
    }
    return c;
  }
}
