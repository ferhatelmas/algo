package page6.q508;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);

    while(in.hasNextLine())
      System.out.println(minimize(in.nextLine()));
  }

  private static String minimize(String s) {
    StringBuilder f = new StringBuilder(), ss = new StringBuilder();
    for(char c : s.toCharArray()) {
      if (c == '*' || c == '?') {
        ss.append(c);
      } else {
        f.append(getSorted(ss)).append(c);
        ss = new StringBuilder();
      }
    }
    if(ss.length() > 0) f.append(getSorted(ss));
    return f.toString();
  }

  private static String getSorted(StringBuilder ss) {
    StringBuilder sb = new StringBuilder();
    char ch[] = ss.toString().toCharArray();
    Arrays.sort(ch);
    char p = ' ';
    for(char cc : ch) {
      if(cc == '*' && p == '*') continue;
      sb.append(cc);
      p = cc;
    }
    return sb.toString();
  }
}
