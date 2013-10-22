package page10.q917;

import java.util.Scanner;
import java.text.DecimalFormat;

public class Main {

  public static void main(String[] args) {

    int i, n;
    double d, min = Double.MAX_VALUE;
    Scanner in = new Scanner(System.in);
    n=in.nextInt();
    for(i=0; i<n; i++) {
      d=Double.parseDouble(in.next());
      if(d<min) min=d;
    }

    System.out.println(new DecimalFormat("##########.00").format(2*min).replace(",", "."));
  }

}