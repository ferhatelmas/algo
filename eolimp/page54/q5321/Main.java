package page54.q5321;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    String s = new Scanner(System.in).nextLine();
    if(s.charAt(0) == '1') {
      System.out.println(Integer.parseInt(s.substring(1), 2) - (1 << (s.length()-1)));
    } else {
      System.out.println(Integer.parseInt(s, 2));
    }
  }
}
