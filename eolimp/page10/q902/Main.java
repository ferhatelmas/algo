package page10.q902;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    int r = new Scanner(System.in).nextInt();

    if(r <= 3) System.out.println("Initial");
    else if(r <= 6) System.out.println("Average");
    else if(r <= 9)System.out.println("Sufficient");
    else System.out.println("High");

  }

}