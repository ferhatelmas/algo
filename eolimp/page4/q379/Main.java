package page4.q379;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    String s = new Scanner(System.in).next();

    int cnt = 0;
    for(int i=0; i<s.length(); i++) if(s.charAt(i)=='1') cnt++;

    if((cnt%2==0 && s.charAt(s.length()-1)=='e') ||
        (cnt%2==1 && s.charAt(s.length()-1)=='o'))
      s=s.subSequence(0, s.length()-1) + "0";
    else
      s=s.subSequence(0, s.length()-1) + "1";

    System.out.println(s);
  }

}