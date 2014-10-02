package page51.q5095;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int l1 = in.nextInt(), l2 = in.nextInt();
    String s1 = in.next(), s2 = in.next(), r;
    StringBuilder sb = new StringBuilder();
    if(l1 < l2)
      r = s2.substring(0, l2-l1) + xor(s1, s2.substring(l2-l1));
    else if(l2 < l1)
      r = s1.substring(0, l1-l2) + xor(s2, s1.substring(l1-l2));
    else
      r = xor(s1, s2);
    r = r.replaceFirst("^0+", "");
    System.out.println(r.isEmpty() ? "0" : r);
  }

  private static String xor(String s1, String s2) {
    StringBuilder sb = new StringBuilder();
    for(int i=0, l=s1.length(); i<l; i++)
      sb.append(s1.charAt(i) == s2.charAt(i) ? '0' : '1');
    return sb.toString();
  }
}
