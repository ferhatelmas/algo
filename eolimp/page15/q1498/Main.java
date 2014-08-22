package page15.q1498;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    String s = in.nextLine(), sub = in.nextLine();

    StringBuilder sb = new StringBuilder();
    int i = s.indexOf(sub);
    while(i != -1) {
      sb.append(' ').append(i);
      i = s.indexOf(sub, i+1);
    }
    System.out.println(sb.length() > 0 ? sb.substring(1) : sb.toString());
  }
}
