package page10.q932;

import java.util.Scanner;
import java.text.DecimalFormat;

public class Main {

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);
    int area = in.nextInt();
    int diff = in.nextInt();

    double dis = Math.sqrt(diff*diff+8*area);
    double d1 = (-diff + dis) / 2;

    System.out.println(new DecimalFormat("##########.00")
        .format(d1 < 0 ? (-diff-dis)/2 : d1).replace(",", "."));
  }

}