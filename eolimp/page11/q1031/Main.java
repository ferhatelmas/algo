package page11.q1031;

import java.util.Scanner;
import java.util.TreeMap;

public class Main {

  public static void main(String[] args) {
    int N = new Scanner(System.in).nextInt();

    TreeMap<Double, String> map = new TreeMap<Double, String>();

    System.out.println("0/1");
    for(int i=2; i<=N; i++)
      for(int j=1; j<i; j++) {
        double d = ((double)j)/i;
        if(!map.containsKey(d))
          map.put(d, j + "/" + i);
      }

    for(double d : map.navigableKeySet())
      System.out.println(map.get(d));
    System.out.println("1/1");

  }

}
