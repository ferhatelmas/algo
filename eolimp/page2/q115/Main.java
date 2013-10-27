package page2.q115;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt();
    int ns[] = new int[n];

    System.out.println(count(ns, 0));
  }

  private static int count(int[] ns, int o) {
    if(o == ns.length) return 1;

    int sum = 0;
    if(o > 1 && ns[o-1] == ns[o-2]) {
      ns[o] = (ns[o-1] == 5 ? 9 : 5);
      sum += count(ns, o+1);
    } else {
      ns[o] = 5;
      sum += count(ns, o+1);
      ns[o] = 9;
      sum += count(ns, o+1);
    }
    return sum;
  }
}
