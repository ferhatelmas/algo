package page61.q6056;

import java.util.*;

public class Main {

  private static String w[] = new String[100];

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    String s = in.nextLine().trim();
    while(!s.equals("#")) {
      int n = 0;
      while(!s.trim().equals("*")) {
        w[n++] = s;
        s = in.nextLine().trim();
      }

      Arrays.sort(w, 0, n);
      while(!(s = in.nextLine().trim()).equals("**"))
        System.out.println(query(n, s));
      System.out.println("$");
      s = in.nextLine().trim();
    }
  }

  private static String query(int n, String q) {
    List<ArrayList<ArrayList<Character>>> terms = getTerms(q.split("\\|"));
    for(int i=0; i<n; i++)
      if(isMatch(w[i], terms)) return w[i];
    return "NONE";
  }

  private static boolean isMatch(String s, List<ArrayList<ArrayList<Character>>> terms) {
    for(ArrayList<ArrayList<Character>> term : terms)
      if(any(s, term.get(0)) && all(s, term.get(1)) && none(s, term.get(2))) return true;
    return false;
  }

  private static boolean any(String s, ArrayList<Character> ls) {
    for(char c : ls)
      if(s.indexOf(c) > -1)
        return true;
    return false;
  }

  private static boolean all(String s, ArrayList<Character> ls) {
    for(char c : ls)
      if(s.indexOf(c) < 0)
        return false;
    return true;
  }

  private static boolean none(String s, ArrayList<Character> ls) {
    for(char c : ls)
      if(s.indexOf(c) > -1)
        return false;
    return true;
  }

  private static List<ArrayList<ArrayList<Character>>> getTerms(String p[]) {
    List<ArrayList<ArrayList<Character>>> terms = new ArrayList<ArrayList<ArrayList<Character>>>();
    for(String s : p) {
       final ArrayList<Character> a = new ArrayList<Character>(),
                            b = new ArrayList<Character>(),
                            c = new ArrayList<Character>();
       for(int i=0, l=s.length(); i<l; i++) {
         if(s.charAt(i) == '+' || s.charAt(i) == '-') {
           if(s.charAt(i) == '+') b.add(s.charAt(++i));
           else c.add(s.charAt(++i));
         } else {
           a.add(s.charAt(i));
         }
       }
       ArrayList<ArrayList<Character>> term = new ArrayList<ArrayList<Character>>() {{ add(a); add(b); add(c); }};
       terms.add(term);
    }
    return terms;
  }
}
