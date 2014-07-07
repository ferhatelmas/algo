package page25.q2459;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    String s = new StringBuilder(new Scanner(System.in).nextLine()
                                                       .replaceAll("\\.", "")).reverse().toString();
    int d = Integer.parseInt(s.substring(0, 2)),
        m = Integer.parseInt(s.substring(2, 4)),
        y = Integer.parseInt(s.substring(4));
    if(m >= 1 && m <= 12 && d >= 1 && (
       ((m == 1 || m == 3 || m == 5 || m == 7 || m == 8 || m == 10 || m == 12) && d <= 31) ||
       ((m == 4 || m == 6 || m == 9 || m == 11) && d <= 30) ||
       (m == 2 && (((y%400 == 0 || y%100 != 0 && y%4 == 0) && d <= 29) || d <= 28))
    )) System.out.println("YES");
    else System.out.println("NO");
  }
}
