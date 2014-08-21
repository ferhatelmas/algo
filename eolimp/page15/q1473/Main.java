package page15.q1473;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n[] = new int[3];
    for(int i=0; i<n.length; i++) n[i] = in.nextInt();
    Arrays.sort(n);
    System.out.println(n[1] + n[2]);
  }
}
