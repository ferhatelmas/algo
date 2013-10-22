package page10.q920;

import java.util.Scanner;
import java.text.DecimalFormat;

public class Main {

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);

    double x = Double.parseDouble(in.next());
    double y = Double.parseDouble(in.next());
    double z = Double.parseDouble(in.next());

    System.out.println(new DecimalFormat("#########0.00")
        .format(Math.min(Math.min(Math.max(x, y), Math.max(y, z)), x+y+z)).replace(",", "."));
  }

}