package page29.q2814;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    StringBuilder sb = new StringBuilder();
    String s = Integer.toBinaryString(new Scanner(System.in).nextInt());
    for(int i=1, l=s.length(); i<l; i++) {
      sb.append('S');
      if(s.charAt(i) == '1') sb.append('X');
    }
    System.out.println(sb.toString());
  }
}
