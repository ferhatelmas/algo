package page51.q5085;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int l = in.nextInt();
    String s1 = in.next(), s2 = in.next();
    StringBuilder sb = new StringBuilder();
    for(int i=0; i<l; i++)
      sb.append(s1.charAt(i) == s2.charAt(i) ? '0' : '1');
    System.out.println(sb.toString());
  }
}
