package page49.q4815;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    StringBuilder sb = new StringBuilder();
    for(int i=1, k=new Scanner(System.in).nextInt(); i<=k; i++)
      sb.append(i);
    perm("", sb.toString());
  }

  private static void perm(String p, String s) {
    int n = s.length();
    if(n == 0) System.out.println(p);
    else
      for(int i=0; i<n; i++)
        perm(p + s.charAt(i), s.substring(0, i) + s.substring(i+1));
  }
}
