package page21.q2044;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    String[] months = {"January", "February", "March", "April",
                       "May", "June", "July", "August",
                       "September", "October", "November", "December"};
    System.out.println(months[new Scanner(System.in).nextInt()-1]);
  }
}
