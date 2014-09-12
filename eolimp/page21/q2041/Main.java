package page21.q2041;

import java.util.Scanner;

public class Main {

  private static final String seasons[] = {
    "Spring", "Summer", "Autumn", "Winter"
  };
  private static final String months[] = {
    "March", "April", "May", "June", "July", "August", "September",
    "October", "November", "December", "January", "February"
  };

  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt() - 1;
    System.out.println(seasons[n]);
    for(int i=0; i<3; i++)
      System.out.println(months[3*n+i]);
  }
}
