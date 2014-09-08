package page48.q4724;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    String s = new Scanner(System.in).next();
    int l = s.length();
    System.out.println(s.charAt(2));
    System.out.println(s.charAt(l-2));
    System.out.println(s.substring(0, 5));
    System.out.println(s.substring(0, l-2));
    for(int i=0; i<l; i+=2) System.out.print(s.charAt(i));
    System.out.println();
    for(int i=1; i<l; i+=2) System.out.print(s.charAt(i));
    System.out.println();
    System.out.println(new StringBuilder(s).reverse().toString());
    for(int i=l-1; i>-1; i-=2) System.out.print(s.charAt(i));
    System.out.println();
    System.out.println(l);
  }
}
