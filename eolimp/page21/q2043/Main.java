package page21.q2043;

import java.util.Scanner;

public class Main {
  private static final String months[] = {
      "January", "February", "March", "April", "May", "June", "July",
      "August", "September", "October", "November", "December"
  };

  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt()-1;
    for(int i=0; i<3; i++)
      System.out.println(months[3*n+i]);
  }
}
