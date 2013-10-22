package page10.q923;

import java.util.Scanner;


public class Main {

  public static void main(String[] args) {
    int r = new Scanner(System.in).nextInt();
    if(r == 1 || r == 2 || r == 12) System.out.println("Winter");
    else if(r == 3 || r == 4 || r == 5) System.out.println("Spring");
    else if(r == 6 || r == 7 || r == 8) System.out.println("Summer");
    else System.out.println("Autumn");
  }

}