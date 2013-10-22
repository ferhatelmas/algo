package page17.q1686;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int c = in.nextInt(), n = in.nextInt() - 1;
    int time = Math.max(n/c + 1, c-n/c) + Math.max(n%c+1, c-n%c) - 1;
    System.out.println(time/60 + " " + time%60);
  }
}
