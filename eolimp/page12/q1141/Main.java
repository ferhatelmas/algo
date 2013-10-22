package page12.q1141;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);
    ArrayList<Integer> buf = new ArrayList<Integer>();
    while(in.hasNextInt())
      buf.add(in.nextInt());

    if(buf.size()%2 == 0) System.out.println(-1);
    else {
      Collections.sort(buf);
      System.out.println(buf.get(buf.size()/2));
    }
  }

}
