package page27.q2617;

import java.util.HashSet;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    HashSet<Integer> set = new HashSet<Integer>();
    for(int i=0; i<n; i++) set.add(in.nextInt());
    System.out.println(set.size());
  }
}
