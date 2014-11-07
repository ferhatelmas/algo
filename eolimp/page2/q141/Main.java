package page2.q141;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int min =Integer.MAX_VALUE, c = 0, k;
    for(int i=in.nextInt(), j=in.nextInt(); i<=j; i++) {
      k = getSum(i);
      if(k < min) {
        min = k;
        c = 1;
      } else if(k == min)
        c++;
    }
    System.out.println(c);
  }

  private static int getSum(int n) {
    int s = 0;
    for(char c : String.valueOf(n).toCharArray())
      s += c - '0';
    return s;
  }
}
