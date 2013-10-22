package page13.q1265;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);

    int[] sides = new int[3];

    while(true) {
      for(int i=0; i<sides.length; i++) sides[i] = in.nextInt();
      if(sum(sides) == 0) break;
      Arrays.sort(sides);
      System.out.println(isRight(sides) ? "right" : "wrong");
    }
  }

  private static boolean isRight(int[] ns) {
    return ns[0]*ns[0] + ns[1]*ns[1] == ns[2]*ns[2];
  }

  private static int sum(int[] ns) {
    int n = 0;
    for(int k : ns) n += k;
    return n;
  }
}
