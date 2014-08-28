package page18.q1703;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), c = 0;

    while(n-- > 0) {
      String parts[] = in.next().split("->");
      if(parts[1].startsWith(parts[0])) c++;
    }
    System.out.println(c);
  }
}
