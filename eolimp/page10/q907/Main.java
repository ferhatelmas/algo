package page10.q907;

import java.util.Scanner;
import java.text.DecimalFormat;

public class Main {

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);

    int n = Integer.parseInt(in.next().trim()), i;
    double tmp;
    for(i=1; i<=n; i++) {

      tmp = Double.parseDouble(in.next().trim());
      if(tmp<=2.5) {
        System.out.println(i + " " + new DecimalFormat("#########0.00").format(tmp).replace(",", "."));
        return;
      }

    }
    System.out.println("Not Found");
  }

}