package page13.q1220;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();

    in.nextLine();
    for(int i=0; i<n; i++) {
      String type = in.next(), num = in.next();
      if("b".equals(type))
        System.out.println("From binary: " + num + " is " + toDecimal(num));
      else
        System.out.println("From decimal: " + num + " is " + toBinary(Integer.parseInt(num)));
    }
  }

  private static int toDecimal(String s) {
    int l = s.length(), n = 0;
    for(int i=l-1; i>-1; i--)
      n += (s.charAt(i) - '0') * Math.pow(-2, l-1-i);
    return n;
  }

  private static String toBinary(int n) {
    if(n == 0) return "0";
    StringBuilder sb = new StringBuilder();
    while(n != 0) {
      int r = n%-2;
      n /= -2;
      if(r < 0) {
        r += 2;
        n++;
      }
      sb.append(r);
    }
    return sb.reverse().toString();
  }
}
