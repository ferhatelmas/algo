package com.ferhatelmas.euler.page2;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Question51 {

    private static Pattern pattern = Pattern.compile("\\d*(\\d)\\d*(\\1)\\d*(\\1)\\d+");
    
    private static HashMap<String, List<Integer>> map = new HashMap<String, List<Integer>>();

    public static void main(String[] args) {

        for(int i=100000; i<1000000; i++) {
    
            checkRepeats(i);

        }
        
        for(String s : map.keySet()) {

            List<Integer> list = map.get(s);

            if(list.size() == 8) {

                System.out.print(s + ": ");

                for(int i : list) System.out.print(i + " ");

                System.out.println();

            }

        }
    }

    
    private static void checkRepeats(int n) {

        String ss = String.valueOf(n);
        if(isPrime(n)) {
            
            Matcher matcher = pattern.matcher(ss);
            
            if(matcher.matches()) {
                
                int offset = matcher.start(1);
                
                char[] ch = ss.toCharArray();
                char c = ss.charAt(offset);
                
                for(int i=0; i<ch.length; i++) {
                    
                    if(ss.charAt(i) == c) ch[i] = 'x';
                    
                }

                List<String> list = getMatchedStrings(ss, new String(ch));

                for(String s : list) {

                    if(map.containsKey(s)) {
                        List<Integer> tmp = map.get(s);
                        tmp.add(n);
                    } else {
                        List<Integer> tmp = new ArrayList<Integer>();
                        tmp.add(n);
                        map.put(s, tmp);
                    }
    
                }
            }
            
        }
    }
    
    private static List<String> getMatchedStrings(String s, String xxx) {

        List<String> list = new ArrayList<String>();

        for(int i=0; i<xxx.length(); i++) {

            for(int j=i+1; j<xxx.length(); j++) {

                for(int k=j+1; k<xxx.length(); k++) {

                    if(xxx.charAt(i) == 'x' && xxx.charAt(j) == 'x' && xxx.charAt(k) == 'x') {
                        char[] chars = s.toCharArray();
                        chars[i] = 'x';
                        chars[j] = 'x';
                        chars[k] = 'x';
                        String ss = new String(chars);
                        list.add(ss);
                    }
                }

            }

        }

        return list;
    }

    private static boolean isPrime(int n) {

        for(int i=2; i<=Math.sqrt(n); i++) {

            if(n%i == 0) return false;

        }

        return true;

    }
}