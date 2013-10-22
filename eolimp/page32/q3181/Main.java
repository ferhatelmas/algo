package page32.q3181;

import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);

    for(int t=in.nextInt(); t>0; t--) {
      String s = in.next();
      for(int i=in.nextInt(); i>0; i--) {
        Matcher m = Pattern.compile(".*?(" + in.next() + ").*?").matcher(s);
        if(m.matches()) System.out.println(m.group(1));
        else System.out.println(-1);
      }
    }
  }
}
