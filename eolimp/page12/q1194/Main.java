package page12.q1194;

import java.util.HashMap;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    HashMap<String, Integer> dict = new HashMap<String, Integer>();
    for(int i=0, t=in.nextInt(); i<t; i++) {
      addToDict(dict, in.next());
      for(int j=0, w=in.nextInt(); j<w; j++)
        System.out.println(isWritable(dict, in.next()) ? "YES" : "NO");
      dict.clear();
    }
  }

  private static void addToDict(HashMap<String, Integer> d, String s) {
    for(int i=0, l=s.length(); i<l; i++) {
      String sub = s.substring(i, i+1);
      if(d.containsKey(sub)) d.put(sub, d.get(sub) + 1);
      else d.put(sub, 1);
    }
  }

  private static boolean isWritable(HashMap<String, Integer> d, String s) {
    HashMap<String, Integer> ds = new HashMap<String, Integer>();
    addToDict(ds, s);
    for(String ss : ds.keySet())
      if(!d.containsKey(ss) || ds.get(ss) > d.get(ss)) return false;
    return true;
  }
}
