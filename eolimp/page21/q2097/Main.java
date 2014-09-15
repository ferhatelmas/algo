package page21.q2097;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
  private static boolean b[] = new boolean[10];

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    boolean f = true;
    for(int i=in.nextInt(), m=in.nextInt(); i<=m; i++)
      if(isDistinct(i)) {
        f = false;
        System.out.println(i);
      }
    if(f) System.out.println();
  }

  private static boolean isDistinct(int n) {
    Arrays.fill(b, false);
    for(char c : String.valueOf(n).toCharArray())
      if(b[c-'0']) return false;
      else b[c-'0'] = true;
    return true;
  }
}
