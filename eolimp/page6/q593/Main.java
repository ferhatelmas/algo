package page6.q593;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), m = in.nextInt();

    StringBuilder sb = new StringBuilder();
    for(int i=0; i<n; i++) {
      boolean f = i%2 != n%2;
      for(int j=0; j<m; j++) {
        sb.append(f ? '.' : 'X');
        f = !f;
      }
      sb.append('\n');
    }
    System.out.print(sb.toString());
  }
}
