package com.ferhatelmas.euler.page2;

import java.io.File;
import java.util.*;

public class Question98 {

  public static void main(String[] args) throws Exception {

    Scanner in = new Scanner(new File("euler/words.txt"));
    in.useDelimiter("\",\"");

    HashMap<Integer, ArrayList<String>> words = new HashMap<Integer, ArrayList<String>>();

    while(in.hasNext()) {
      String word = in.next();
      int len = word.length();

      if(!words.containsKey(len)) {
        words.put(len, new ArrayList<String>());
      }

      words.get(len).add(word);
    }

    long max = 0;
    for(int len : words.keySet()) {
      ArrayList<String> list = words.get(len);
      int size = list.size();

      for(int i=0; i<size-1; i++) {
        for(int j=i+1; j<size; j++) {
          if(isAnagram(list.get(i), list.get(j))) {
            max = Math.max(max, getPairMax(list.get(i), list.get(j)));
          }
        }
      }
    }

    System.out.println(max);

  }

  private static boolean isAnagram(String s1, String s2) {
    char[] c1 = s1.toCharArray(), c2 = s2.toCharArray();

    Arrays.sort(c1);
    Arrays.sort(c2);

    return Arrays.equals(c1, c2);
  }

  private static long getPairMax(String s1, String s2) {

    ArrayList<Character> chars = new ArrayList<Character>();
    for(char c : s1.toCharArray()) if(!chars.contains(c)) chars.add(c);

    if(chars.size() > 10) return 0;

    ArrayList<Integer> digits = new ArrayList<Integer>();
    for(int i=0; i<10; i++) digits.add(i);
    return replaceLetters(s1, s2, chars, digits, 0);
  }

  private static long replaceLetters(String s1, String s2, ArrayList<Character> chars, ArrayList<Integer> digits, int z) {

    if(z == chars.size()) {
      long is1 = Long.parseLong(s1), is2 = Long.parseLong(s2);
      return isPerfectSquare(is1) && isPerfectSquare(is2) ? Math.max(is1, is2) : 0;
    }

    long max = 0;
    for(int i=0; i<10; i++) {

      if(!digits.contains(i)) continue;

      String ss1 = s1.replace(chars.get(z), (char)(48 + i));
      String ss2 = s2.replace(chars.get(z), (char)(48 + i));
      if(ss1.startsWith("0") || ss2.startsWith("0")) continue;

      digits.remove((Integer)i);
      max = Math.max(max, replaceLetters(ss1, ss2, chars, digits, z+1));
      digits.add(i);
    }

    return max;
  }

  public static boolean isPerfectSquare(long n) {
    if (n < 0) return false;

    long tst = (long)(Math.sqrt(n) + 0.5);
    return tst*tst == n;
  }

}
