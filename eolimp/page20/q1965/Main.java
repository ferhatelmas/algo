package page20.q1965;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int ns[] = new int[in.nextInt()];
    for(int i=0; i<ns.length; i++) ns[i] = in.nextInt();
    for(int i=0, n=in.nextInt(); i<ns.length; i++) {
      if(n > ns[i]) {
        System.out.println(i + 1);
        return;
      }
    }
    System.out.println(ns.length+1);
  }
}
