package page17.q1609;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int cnt = 0;
    Scanner in = new Scanner(System.in);
    String s = in.next();
    char c = in.next().charAt(0);
    for(char ch : s.toCharArray()) if(ch == c) cnt++;
    System.out.println(cnt);
  }
}
