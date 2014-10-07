package page51.q5097;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    char c[] = Integer.toBinaryString(in.nextInt()).toCharArray();

    StringBuilder sb = new StringBuilder();
    for(int i=0; i<n; i++)
      sb.append(i < c.length ? c[c.length-1-i] : '0');
    System.out.println(Integer.parseInt(sb.toString(), 2));
  }
}
