package vol1.p1004;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    double sum = 0;
    for(int i=0; i<12; i++) sum += in.nextDouble();
    System.out.format("$%.2f\n", sum/12);
  }

}
