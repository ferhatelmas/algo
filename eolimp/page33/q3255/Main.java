package page33.q3255;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    String s = new Scanner(System.in).nextLine();
    String ns[] = s.split("\\+|\\*");
    int res = Integer.parseInt(ns[0]), j = ns[0].length();
    for(int i=1; i<ns.length; i++) {
      if(s.charAt(j) == '+')
        res += Integer.parseInt(ns[i]);
      else
        res *= Integer.parseInt(ns[i]);
      j += 1 + ns[i].length();
    }

    System.out.println(res);
  }
}
