package page11.q1004;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    String s = Integer.toBinaryString(new Scanner(System.in).nextInt());
    int max = 0;
    for(int i=s.length(); i>0; i--)
      max = Math.max(max, Integer.parseInt(s.substring(i) + s.substring(0, i), 2));
    System.out.println(max);
  }
}
