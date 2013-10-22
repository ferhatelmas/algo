package page5.q490;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    String s = "0" + new Scanner(System.in).next();
    for(int i=0; i<s.length()-1; i++)
      System.out.print(s.charAt(i) == s.charAt(i+1) ? "0" : "1");
    System.out.println();
  }
}
