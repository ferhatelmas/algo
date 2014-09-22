package page29.q2817;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int t = in.nextInt(), n;

    StringBuilder sb = new StringBuilder();
    while(t-- > 0) {
      char chars[] = Integer.toBinaryString(in.nextInt()).toCharArray();
      sb.setLength(0);
      for(int i=1; i<=chars.length; i++)
        if(chars[chars.length-i] == '1')
          sb.append(' ').append(i-1);
      System.out.println(sb.length() > 0 ? sb.substring(1) : "");
    }
  }
}
