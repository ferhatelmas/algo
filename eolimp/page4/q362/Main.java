package page4.q362;

import java.util.Scanner;
import java.util.Locale;
import java.text.DecimalFormat;

public class Main {

  public static void main(String[] args) {

    Scanner in=new Scanner(System.in);
    in.useLocale(Locale.US);

    double d, max=0, min=Double.MAX_VALUE;

    while(in.hasNextDouble()) {
      d=in.nextDouble();
      if(d > max) max = d;
      if(d < min) min = d;
    }

    System.out.println(new DecimalFormat("#########0.00").format(max-min).replace(",", "."));
  }

}