package page10.q901;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

  public static void main(String[] args) throws Exception{

    String line = new BufferedReader(new InputStreamReader(System.in)).readLine();
    int cnt=0;
    char c;
    boolean flag=false;
    for(int i=0; i<line.length(); i++) {
      c = line.charAt(i);
      if(c != '+' && c != '*' && c != '-') flag = true;
      else if(flag) {
        flag = false;
        cnt++;
      }
    }
    System.out.println(cnt);
  }

}