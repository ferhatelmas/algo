package page4.q378;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;

public class Main {

  public static void main(String[] args) throws Exception {

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    String message = br.readLine();
    String encodeAlphabet = br.readLine();

    HashMap<Integer, Integer> map=new HashMap<Integer, Integer>();
    for(int i=0; i<encodeAlphabet.length(); i++)
      map.put('A'+i, (int)encodeAlphabet.charAt(i));

    StringBuilder sb = new StringBuilder();
    for(int i=0; i<message.length(); i++) {
      char c = message.charAt(i);
      if(c == ' ') sb.append(c);
      else sb.append((char)map.get((int)c).intValue());
    }

    System.out.println(sb.toString());
  }

}