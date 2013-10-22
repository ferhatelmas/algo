package page15.q1461;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    Scanner in=new Scanner(System.in);

    int n = in.nextInt(), k = in.nextInt(),
        diff = Integer.MAX_VALUE, val, i, j, abs, res=0, mul;
    String s;

    for(i=0; i<n; i++) {
      val = in.nextInt();

      s = String.valueOf(val);
      mul = 1;
      for(j=0; j<s.length(); j++) {
        mul*=(s.charAt(j)-'0');
      }
      abs = Math.abs(mul-k);
      if(abs<diff) {
        res=val;
        diff=abs;
      }
    }

    System.out.println(res);
  }

}