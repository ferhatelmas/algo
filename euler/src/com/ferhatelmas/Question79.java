package com.ferhatelmas;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.*;

/**
 * Created by IntelliJ IDEA.
 * User: felmas
 * Date: 2/24/12
 * Time: 6:23 PM
 * To change this template use File | Settings | File Templates.
 */
public class Question79 {

    private static String alphabet = "0123456789";

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new FileReader("keylog.txt"));

        List<Integer> chars = new ArrayList<Integer>();
        List<String> keys = new ArrayList<String>();
        
        String line;

        while((line=br.readLine()) != null) {

            if(!keys.contains(line)) keys.add(line);
            
            for(char c : line.toCharArray()) if(!chars.contains((int)c)) chars.add((int)c);
            
        }
        br.close();
        
        StringBuilder sb = new StringBuilder();
        
        while(!keys.isEmpty()) {
            
            char ch = getFirstChar(keys);
            
            if(chars.contains((int)ch)) {
                sb.append(ch);
                keys = removeChar(keys, ch);
            }
            
        }
        
        System.out.println(sb);
    }
    
    private static List<String> removeChar(List<String> keys, char ch) {
        
        List<String> newKeys = new ArrayList<String>();
        
        for(String s : keys) {
            
            if(s.indexOf(ch) == -1) newKeys.add(s);
            else {
                
                if(s.length() != 1) newKeys.add(s.substring(1));
                
            }
            
        }

        return newKeys;
        
    }
    
    private static char getFirstChar(List<String> keys) {
        
        char ch = 0;
        
        for(int i=0; i<alphabet.length(); i++) {
            
            ch = alphabet.charAt(i);
            
            boolean firstCandidate = true;
            
            for(String s : keys) {
                
                if(s.indexOf(ch) > 0) firstCandidate = false;
                
            }
            
            if(firstCandidate) break;
            
        }

        alphabet = alphabet.substring(0, alphabet.indexOf(ch)).concat(alphabet.substring(alphabet.indexOf(ch)+1));

        return ch;
        
    }
    
}
