package page3.q260;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), ns[] = new int[n];
    for(int i=0; i<ns.length; i++) ns[i] = in.nextInt();
    Arrays.sort(ns);
    StringBuilder sb = new StringBuilder();
    for(int i=ns.length-1; i>-1; i--) sb.append(' ').append(ns[i]);
    System.out.println(n > 0 ? sb.substring(1) : "");
  }
}
