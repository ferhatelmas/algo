package page10.q929;

import java.util.Scanner;
import java.util.Locale;

public class Main {

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);
    in.useLocale(Locale.US);

    double a=in.nextDouble();
    double b=in.nextDouble();
    double c=in.nextDouble();
    double d=in.nextDouble();

    if(a==b && c==d) System.out.println("YES");
    else if(a==c && b==d) System.out.println("YES");
    else if(a==d && b==c) System.out.println("YES");
    else System.out.println("NO");
  }

}