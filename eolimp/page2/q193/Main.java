package page2.q193;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), m = in.nextInt();
    System.out.println(getSmallest(n, m) + " " + getLargest(n, m));
  }

  private static String getSmallest(int n, int m) {
    int x = m/9;
    if(x < n-1) m--;
    StringBuilder sb = new StringBuilder();
    for(int i=0, t=m/9; i<t; i++) sb.append('9');
    if(m%9 > 0) sb.append(m%9);
    if(x < n-1) {
      for(int i=0, l=n-sb.length()-1; i<l; i++) sb.append('0');
      sb.append('1');
    }
    return sb.reverse().toString();
  }

  private static String getLargest(int n, int m) {
    StringBuilder sb = new StringBuilder();
    for(int i=0, t=m/9; i<t; i++) sb.append('9');
    if(m%9 > 0) sb.append(m%9);
    for(int i=0, l=n-sb.length(); i<l; i++) sb.append('0');
    return sb.toString();
  }
}
