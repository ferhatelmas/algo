package vol9.p1806;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();

    for(int i=1; i<=n; i++) {
      System.out.println("Scenario #" + i + ":");
      for(int j=0, k=2*Math.min(9, in.nextInt())+1; j<k; j++) {
        System.out.println("slice #" + (j+1) + ":");
        System.out.print(getSlice(k/2, Math.abs(j-k/2)));
      }
      if(i < n)
        System.out.println();
    }
  }

  private static String getSlice(int k, int n) {
    StringBuilder sb = new StringBuilder();
    for(int i=0, m=2*k+1; i<m; i++) {
      int c = Math.abs(i - k), b = Math.max(0, m-2*n-2*c);

      if(b > 0) {
        for(int j=0; j<(m-b)/2; j++) sb.append('.');
        for(int j=k; j>k-b/2; j--) sb.append(j);
        for(int j=k-b/2; j<=k; j++) sb.append(j);
        for(int j=0; j<(m-b)/2; j++) sb.append('.');
      } else {
        for(int j=0; j<m; j++) sb.append('.');
      }
      sb.append('\n');
    }
    return sb.toString();
  }
}
