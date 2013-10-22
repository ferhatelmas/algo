package page14.q1378;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);
    int[] cache = new int[40];
    cache[0] = 0; cache[1] = 1;
    int i=2;
    while(i < cache.length) {
      cache[i] = cache[i-1] + cache[i-2];
      i++;
    }

    int n = in.nextInt();
    StringBuilder sb = new StringBuilder();
    while(n-- > 0) {
      int num = in.nextInt();
      int num2 = num;
      for(i=cache.length-1; i>1; i--) {
        if(num >= cache[i]) {
          sb.append('1');
          num -= cache[i];
        } else if(sb.indexOf("1") != -1)
          sb.append('0');
      }
      System.out.println(num2 + " = " + (num2==0 ? 0 : sb.toString()) + " (fib)");
      sb.delete(0, sb.length());
    }
  }

}
