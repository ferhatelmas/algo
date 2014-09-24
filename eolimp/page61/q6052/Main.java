package page61.q6052;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    String s;

    while(!(s = in.nextLine()).equals("#"))
      System.out.println(quickSum(s));
  }

  private static long quickSum(String s) {
    long sum = 0;
    for(int i=0, l=s.length(); i<l; i++)
      if(s.charAt(i) != ' ')
        sum += (s.charAt(i) - 'A' + 1) * (i+1);
    return sum;
  }
}
