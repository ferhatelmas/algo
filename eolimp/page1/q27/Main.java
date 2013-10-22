package page1.q27;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    int n = new Scanner(System.in).nextInt(), max = 0;

    String s = bin(n);
    for(int i=0; i<s.length(); i++) {
      int l = getVal(s);
      if(l > max) max = l;
      s = s.substring(1) + s.substring(0, 1);
    }

    System.out.println(max);
  }

  private static int  getVal(String s) {
    int mul=1, val=0;
    for(int i=0; i<s.length(); i++) {
      if(s.charAt(i) == '1') val += mul;
      mul *= 2;
    }
    return val;
  }

  private static String bin(int n) {

    StringBuilder sb = new StringBuilder();
    while(n > 0) {
      if(n%2 == 0) sb.append('0');
      else sb.append('1');
      n /= 2;
    }
    return sb.toString();
  }

}